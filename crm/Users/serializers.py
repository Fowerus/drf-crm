import jwt
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainSerializer, PasswordField
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings

from .models import User
from Sessions.models import Session



class MyTokenObtainSerializer(TokenObtainSerializer):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields[self.username_field] = serializers.CharField(write_only = True)
		self.fields['password'] = PasswordField()



class MyTokenRefreshSerializer(serializers.Serializer):
	refresh = serializers.CharField(write_only = True)
	error = serializers.CharField(read_only = True)
	access = serializers.ReadOnlyField()

	device = serializers.CharField(write_only = True)

	@classmethod
	def get_token(cls, user):
		return RefreshToken.for_user(user)

	def validate(self, attrs):
		device = attrs['device']
		attrs.pop('device')
		data = super().validate(attrs)

		try:
			refresh_decode = jwt.decode(attrs['refresh'], settings.SECRET_KEY, algorithms = [settings.SIMPLE_JWT['ALGORITHM']])
			user = get_user_model().objects.get(id = refresh_decode['user_id'])
		except:
			return {'error':'Signature expired'}

		try:
			current_session = Session.objects.filter(user = user.id).get(device = device)
			refresh = self.get_token(user)

			data['refresh'] = str(refresh)
			data['access'] = str(refresh.access_token)

			if api_settings.UPDATE_LAST_LOGIN:
				update_last_login(None, self.user)

			return data

		except:
			return {'error':'Unauthorized'}



class MyTokenObtainPairSerializer(MyTokenObtainSerializer):
	refresh = serializers.CharField(read_only = True)
	error = serializers.CharField(read_only = True)
	access = serializers.ReadOnlyField(read_only = True)
	device = serializers.CharField(write_only = True)

	@classmethod
	def get_token(cls, user):
		return RefreshToken.for_user(user)

	def validate(self, attrs):
		device = attrs['device']
		attrs.pop('device')

		data = super().validate(attrs)

		try:
			Session.objects.filter(user = self.user.id).get(device = device)

			return {'error':'Already authorized'}

		except:
			Session.objects.create(user = self.user, device = device)
			refresh = self.get_token(self.user)

			data['refresh'] = str(refresh)
			data['access'] = str(refresh.access_token)

			if api_settings.UPDATE_LAST_LOGIN:
				update_last_login(None, self.user)

			return data



class UserRegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=128, min_length=8, write_only=True)

	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)
		return user


	class Meta:
		model = User
		fields = ['email','surname','name','patronymic', 'address', 'number', 'password']



class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['surname', 'name', 'patronymic', 'address', 'email', 'image', 'created_at', 'updated_at']