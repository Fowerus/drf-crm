import jwt
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from Users.serializers import UserSerializer
from Sessions.models import Session



class SessionSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Session
		fields = ['id', 'user', 'device']
