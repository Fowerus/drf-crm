import jwt
from django.contrib.auth import authenticate
from django.conf import settings
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from .models import *


class OrganizationSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		new_organization = Organization.objects.create(**validated_data)

		return new_organization


	class Meta:
		model = Organization
		fields = ['name','description', 'address', 'creator']