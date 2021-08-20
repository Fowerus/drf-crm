import jwt
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, RefreshToken
from rest_framework_simplejwt.settings import api_settings

from .models import User



class UserRegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=128, min_length=8, write_only=True)

	def create(self, validated_data):
		
		return User.objects.create_user(**validated_data)


	class Meta:
		model = User
		fields = ['email','surname','name','patronymic', 'address', 'password']





# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
# 	@classmethod
# 	def get_token(cls, user):
# 		token = super().get_token(user)

# 		return token



class MyTokenRefreshSerializer(serializers.Serializer):
	refresh = serializers.CharField()
	access = serializers.ReadOnlyField()

	@classmethod
	def get_token(cls, user):
		return RefreshToken.for_user(user)

	def validate(self, attrs):
		data = super().validate(attrs)

		refresh_decode = jwt.decode(attrs['refresh'], settings.SECRET_KEY, algorithms = [settings.SIMPLE_JWT['ALGORITHM']])
		print(refresh_decode)
		user = get_user_model().objects.get(id = refresh_decode['user_id'])

		refresh = self.get_token(user)

		data['refresh'] = str(refresh)
		data['access'] = str(refresh.access_token)

		if api_settings.UPDATE_LAST_LOGIN:
			update_last_login(None, self.user)

		return data



# class UserLoginSerializer(serializers.Serializer):
# 	email = serializers.EmailField(write_only=True)
# 	password = serializers.CharField(max_length=128, write_only=True)

# 	access = serializers.CharField(max_length = 250, read_only = True)
# 	refresh = serializers.CharField(max_length = 250, read_only = True)
# 	expire = serializers.IntegerField(read_only = True)


# 	def validate(self, data):
# 		email = data.get('email',None)
# 		password = data.get('password',None)

# 		if email is None:
# 			return Response(status = status.HTTP_404_NOT_FOUND)

# 		if password is None:
# 			return Response(status = status.HTTP_404_NOT_FOUND)

# 		user = authenticate(email = email, password = password)

# 		if user is None:
# 			return Response(status = status.HTTP_404_NOT_FOUND)

# 		if not user.is_active:
# 			return Response(status = status.HTTP_404_NOT_FOUND)


# 		return {
# 			"expire":settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds,
# 			"refresh": user.token['refresh'],
# 			"access": user.token['access']
# 		}



class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['surname', 'name', 'patronymic', 'address', 'email', 'small_image']