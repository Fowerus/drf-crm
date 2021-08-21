import jwt
from django.conf import settings
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.settings import api_settings

from .models import User
from Sessions.models import Session



class UserRegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=128, min_length=8, write_only=True)

	def create(self, validated_data):
		
		return User.objects.create_user(**validated_data)


	class Meta:
		model = User
		fields = ['email','surname','name','patronymic', 'address', 'password']



class MyTokenRefreshSerializer(serializers.Serializer):
	refresh = serializers.CharField()
	access = serializers.ReadOnlyField()

	@classmethod
	def get_token(cls, user):
		return RefreshToken.for_user(user)

	def validate(self, attrs):
		device = attrs['device']
		attrs.pop('device')
		data = super().validate(attrs)

		refresh_decode = jwt.decode(attrs['refresh'], settings.SECRET_KEY, algorithms = [settings.SIMPLE_JWT['ALGORITHM']])
		user = get_user_model().objects.get(id = refresh_decode['user_id'])

		try:
			current_session = Session.objects.filter(id = user.id).get(device = attrs)
			refresh = self.get_token(user)

			data['refresh'] = str(refresh)
			data['access'] = str(refresh.access_token)

			if api_settings.UPDATE_LAST_LOGIN:
				update_last_login(None, self.user)

			return data

		except:
			return {'error':'Unauthorized'}


class MyTokenObtainPairSerializer(TokenObtainSerializer):
	@classmethod
	def get_token(cls, user):
		return RefreshToken.for_user(user)

	def validate(self, attrs):
		device = attrs['device']
		attrs.pop('device')

		data = super().validate(attrs)

		try:
			Session.objects.filter(user = self.user.id).get(device = device)

			return Response({'error':'Already authorized'})

		except:
			Session.objects.create(user = self.user, device = device)
			refresh = self.get_token(self.user)

			data['refresh'] = str(refresh)
			data['access'] = str(refresh.access_token)

			if api_settings.UPDATE_LAST_LOGIN:
				update_last_login(None, self.user)

			return data



class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['surname', 'name', 'patronymic', 'address', 'email', 'image', 'created_at', 'updated_at']