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