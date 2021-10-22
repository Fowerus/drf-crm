import jwt

from django.contrib.auth import authenticate, get_user_model
from django.conf import settings

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainSerializer, PasswordField
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt import exceptions

from .models import User
from Sessions.models import Session_user



class MyTokenObtainForEmailSerializer(TokenObtainSerializer):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields[self.username_field] = serializers.CharField(write_only = True)
		self.fields['password'] = PasswordField()



class MyTokenObtainForPhoneSerializer(TokenObtainSerializer):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['email'] = serializers.CharField(write_only = True)
		self.fields['phone'] = serializers.CharField(write_only = True)
		self.fields['password'] = PasswordField()


	def validate(self, attrs):
		authenticate_kwargs = {
			'phone': attrs['phone'],
			'password': attrs['password'],
		}
		try:
			authenticate_kwargs['request'] = self.context['request']
		except KeyError:
			pass
		try:
			self.user = get_user_model().objects.get(phone = authenticate_kwargs['phone'])
			if not self.user.check_password(authenticate_kwargs['password']):
				self.user = None
		except:
			return {"detail": "No active account found with the given credentials"}

		if not api_settings.USER_AUTHENTICATION_RULE(self.user):
			raise exceptions.AuthenticationFailed(
				self.error_messages['no_active_account'],
				'no_active_account',
			)

		return {}



class MyTokenObtainPairPhoneSerializer(MyTokenObtainForPhoneSerializer):
	refresh = serializers.CharField(read_only = True)
	detail = serializers.CharField(read_only = True)
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
			Session_user.objects.filter(user = self.user.id).get(device = device)

			return {'detail':'Already authorized'}

		except:
			try:
				Session_user.objects.create(user = self.user, device = device)
				refresh = self.get_token(self.user)

				refresh['name'] = self.user.name
				refresh['surname'] = self.user.surname
				refresh['second_name'] = self.user.second_name

				refresh['email'] = self.user.email
				refresh['phone'] = self.user.phone

				data['refresh'] = str(refresh)
				data['access'] = str(refresh.access_token)

				if api_settings.UPDATE_LAST_LOGIN:
					update_last_login(None, self.user)

				return data
			except:
				return {"detail": "No active account found with the given credentials"}




class MyTokenObtainPairEmailSerializer(MyTokenObtainForEmailSerializer):
	refresh = serializers.CharField(read_only = True)
	detail = serializers.CharField(read_only = True)
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
			Session_user.objects.filter(user = self.user.id).get(device = device)

			return {'detail':'Already authorized'}

		except:
			try:
				Session_user.objects.create(user = self.user, device = device)
				refresh = self.get_token(self.user)

				refresh['name'] = self.user.name
				refresh['surname'] = self.user.surname
				refresh['second_name'] = self.user.second_name

				refresh['email'] = self.user.email
				refresh['phone'] = self.user.phone

				data['refresh'] = str(refresh)
				data['access'] = str(refresh.access_token)

				if api_settings.UPDATE_LAST_LOGIN:
					update_last_login(None, self.user)

				return data
			except:
				return {"detail": "No active account found with the given credentials"}



class MyTokenRefreshSerializer(serializers.Serializer):
	refresh = serializers.CharField(write_only = True)
	detail = serializers.CharField(read_only = True)
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
			return {'detail':'Refresh token expired or not exist'}

		try:
			current_session = Session_user.objects.filter(user = user.id).get(device = device)
			refresh = self.get_token(user)

			refresh['name'] = user.name
			refresh['surname'] = user.surname
			refresh['second_name'] = user.second_name

			refresh['email'] = user.email
			refresh['phone'] = user.phone

			data['refresh'] = str(refresh)
			data['access'] = str(refresh.access_token)

			if api_settings.UPDATE_LAST_LOGIN:
				update_last_login(None, user)

			return data

		except:
			return {'detail':'Unauthorized'}
			



class UserRegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=128, min_length=8, write_only=True)
	phone = serializers.CharField()
	email = serializers.CharField()


	def create(self, validated_data):
		user = User.objects.create_user(**validated_data)

		return user

	
	class UserRegistrationForPhone(serializers.ModelSerializer):
		password = serializers.CharField(max_length=128, min_length=8, write_only=True)
		phone = serializers.CharField()

		def create(self, validated_data):
			user = User.objects.create_user(**validated_data)

			return user

		class Meta:
			model = User
			fields = ['surname','name','second_name', 'address', 'phone', 'password']


	class UserRegistrationForEmail(serializers.ModelSerializer):
		password = serializers.CharField(max_length=128, min_length=8, write_only=True)
		email = serializers.CharField()

		def create(self, validated_data):
			user = User.objects.create_user(**validated_data)

			return user

		class Meta:
			model = User
			fields = ['surname','name','second_name', 'address', 'email', 'password']


	class Meta:
		model = User
		fields = ['surname','name','second_name', 'address', 'email','phone', 'password']



class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['id', 'surname', 'name', 'second_name', 'address', 'email', 'phone', 'image', 'confirmed_email', 'confirmed_phone', 'created_at', 'updated_at']

	class UserUSerializer(serializers.ModelSerializer):
		password = serializers.CharField(write_only = True)

		def update(self, instance, validated_data):
			try:
				if 'password' in validated_data:
					instance.set_password(validated_data['password'])
					validated_data.pop('password')
			except:
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
			fields = ['surname', 'name', 'second_name','address', 'email', 'phone', 'image', 'password']
			