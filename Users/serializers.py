import jwt

from django.contrib.auth import authenticate, get_user_model
from django.utils import timezone
from django.db import transaction
from django.conf import settings

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainSerializer, PasswordField
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt import exceptions

from core.utils.atomic_exception import MyCustomError
from core.views import extend_tokenFields, user_code_verification
from .models import User



class MyTokenObtainSerializer(TokenObtainSerializer):
    refresh = serializers.CharField(read_only=True)
    detail = serializers.CharField(read_only=True)
    access = serializers.ReadOnlyField()
    device = serializers.CharField(write_only=True)


    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs.get(self.username_field, None),
            'password': attrs['password'],
            'code': attrs.get('code', None),
            'phone': attrs.get('phone', None)
        }

        if authenticate_kwargs.get(self.username_field) != '@':
            self.user = get_user_model().objects.get(
                email=authenticate_kwargs[self.username_field])
            field = 'email'

        elif authenticate_kwargs.get('phone') != '+':
            self.user = get_user_model().objects.get(
                phone=authenticate_kwargs['phone'])
            field = 'phone'


        user_code_verification(self.user, field, authenticate_kwargs.get('code'), 
            authenticate_kwargs.get('password'))


        if not api_settings.USER_AUTHENTICATION_RULE(self.user):
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )


        device = attrs.pop('device')
        session = {'date':timezone.now().__str__(), 'user-agent':device}
        data = {}

        self.user.set_session(device, session)

        refresh = self.get_token(self.user)
        refresh = extend_tokenFields(refresh, self.user, device, session)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class MyTokenObtainPairSerializer(MyTokenObtainSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'] = serializers.CharField(write_only=True)
        self.fields['phone'] = serializers.CharField(write_only=True)
        self.fields['code'] = serializers.IntegerField(write_only=True, required = False)
        self.fields['password'] = PasswordField()


class MyTokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField(write_only=True)
    detail = serializers.CharField(read_only=True)
    access = serializers.ReadOnlyField()

    device = serializers.CharField(write_only=True)

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        device = attrs['device']
        attrs.pop('device')
        data = super().validate(attrs)

        try:
            refresh_decode = jwt.decode(attrs['refresh'], settings.SECRET_KEY, algorithms=[
                                        settings.SIMPLE_JWT['ALGORITHM']])
            user = get_user_model().objects.get(id=refresh_decode['user_id'])
        except Exception as e:
            raise MyCustomError('Refresh token expired or not exist', 400)


        try:
            for item in user.sessions:
                if item['user-agent'] == device:
                    session = item

            refresh = self.get_token(user)
            refresh = extend_tokenFields(refresh, user, device, session)

            data['refresh'] = str(refresh)
            data['access'] = str(refresh.access_token)

            if api_settings.UPDATE_LAST_LOGIN:
                update_last_login(None, user)

            return data

        except Exception as e:
            raise MyCustomError('Unauthorized or session does not exist', 400)


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True)
    phone = serializers.CharField()
    email = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.send_code('email')

        return user

    class UserRegistrationForPhone(serializers.ModelSerializer):
        password = serializers.CharField(
            max_length=128, min_length=8, write_only=True)
        phone = serializers.CharField()

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            user.send_code('phone')

            return user

        class Meta:
            model = User
            fields = ['surname', 'first_name', 'second_name',
                      'address', 'phone', 'password']

    class UserRegistrationForEmail(serializers.ModelSerializer):
        password = serializers.CharField(
            max_length=128, min_length=8, write_only=True)
        email = serializers.CharField()

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            user.send_code('email')

            return user

        class Meta:
            model = User
            fields = ['surname', 'first_name', 'second_name',
                      'address', 'email', 'password']

    class Meta:
        model = User
        fields = ['surname', 'first_name', 'second_name',
                  'address', 'email', 'phone', 'password']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'surname', 'first_name', 'second_name',
                  'address', 'email', 'phone', 'avatar', 'confirmed_email', 'confirmed_phone', 'created_at', 'updated_at']

    class UserMarketplaceSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ['id', 'surname', 'first_name',
                      'second_name', 'email', 'phone']

    class UserUSerializer(serializers.ModelSerializer):
        password = serializers.CharField(write_only=True)
        surname = serializers.CharField()
        first_name = serializers.CharField()
        second_name = serializers.CharField(required=False)
        address = serializers.CharField()
        email = serializers.CharField()
        phone = serializers.CharField()
        avatar = serializers.CharField(allow_null=True)

        def update(self, instance, validated_data):
            try:
                if 'password' in validated_data:
                    instance.set_password(validated_data['password'])
                    validated_data.pop('password')
            except Exception as e:
                pass

            if 'phone' in validated_data:
                instance.phone = validated_data['phone']
                instance.confirmed_phone = False
                validated_data.pop('phone')
            if 'email' in validated_data:
                instance.email = validated_data['email']
                instance.confirmed_email = False
                validated_data.pop('email')

            return super().update(instance, validated_data)

        class Meta:
            model = User
            fields = ['surname', 'first_name', 'second_name',
                      'address', 'email', 'phone', 'avatar', 'password']