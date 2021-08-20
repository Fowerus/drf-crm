import jwt
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User



class UserRegistrationSerializer(serializers.ModelSerializer):
	password = serializers.CharField(max_length=128, min_length=8, write_only=True)

	def create(self, validated_data):
		
		return User.objects.create_user(**validated_data)


	class Meta:
		model = User
		fields = ['email','surname','name','patronymic', 'address', 'password']





class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
	@classmethod
	def get_token(cls, user):
		token = super().get_token(user)

		# Add custom claims
		token['name'] = user.name
  
		# ...

		return token



class TokenObtainPairSerializer(TokenObtainSerializer):
	@classmethod
	def get_token(cls, user):
		return RefreshToken.for_user(user)

	def validate(self, attrs):
		data = super().validate(attrs)

		refresh = self.get_token(self.user)

		data['refresh'] = str(refresh)
		data['access'] = str(refresh.access_token)

		if api_settings.UPDATE_LAST_LOGIN:
			update_last_login(None, self.user)

		return data

class TokenRefreshSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.ReadOnlyField()

    def validate(self, attrs):
        refresh = RefreshToken(attrs['refresh'])

        data = {'access': str(refresh.access_token)}

        if api_settings.ROTATE_REFRESH_TOKENS:
            if api_settings.BLACKLIST_AFTER_ROTATION:
                try:
                    # Attempt to blacklist the given refresh token
                    refresh.blacklist()
                except AttributeError:
                    # If blacklist app not installed, `blacklist` method will
                    # not be present
                    pass

            refresh.set_jti()
            refresh.set_exp()

            data['refresh'] = str(refresh)

        return data


class MyTokenRefreshSerializer(TokenObtainPairSerializer, TokenRefreshSerializer):
	refresh = serializers.CharField()



class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField(write_only=True)
	password = serializers.CharField(max_length=128, write_only=True)

	access = serializers.CharField(max_length = 250, read_only = True)
	refresh = serializers.CharField(max_length = 250, read_only = True)
	expire = serializers.IntegerField(read_only = True)


	def validate(self, data):
		email = data.get('email',None)
		password = data.get('password',None)

		if email is None:
			return Response(status = status.HTTP_404_NOT_FOUND)

		if password is None:
			return Response(status = status.HTTP_404_NOT_FOUND)

		user = authenticate(email = email, password = password)

		if user is None:
			return Response(status = status.HTTP_404_NOT_FOUND)

		if not user.is_active:
			return Response(status = status.HTTP_404_NOT_FOUND)


		return {
			"expire":settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds,
			"refresh": user.token['refresh'],
			"access": user.token['access']
		}



class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['surname', 'name', 'patronymic', 'address', 'email', 'small_image']