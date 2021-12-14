import jwt
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from Users.serializers import UserSerializer
from Clients.serializers import ClientSerializer
from Sessions.models import Session_user, Session_client



class Session_userSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Session_user
		fields = ['id', 'user', 'device', 'created_at', 'updated_at']



class Session_clientSerializer(serializers.ModelSerializer):
	client = ClientSerializer()

	class Meta:
		model = Session_client
		fields = ['id', 'client', 'device', 'created_at', 'updated_at']
		
