import jwt

from django.contrib.auth import authenticate
from django.conf import settings

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from .models import *
from Users.serializers import UserSerializer


class OrganizationSerializer(serializers.ModelSerializer):
	creator = UserSerializer()

	class Meta:
		model = Organization
		fields = ['id','name','description', 'address', 'creator', 'created_at', 'updated_at']


	class OrganizationCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			organization = Organization.objects.create(**validated_data)

			return organization


		class Meta:
			model = Organization
			fields = ['name','description', 'address', 'creator']



class Organization_numberSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class Meta:
		model = Organization_number
		fields = ['id','number','organization', 'created_at', 'updated_at']


	class Organization_numberCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			organization_number = Organization_number.objects.create(**validated_data)

			return organization_number


		class Meta:
			model = Organization_number
			fields = ['number','organization']



class Organization_linkSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class Meta:
		model = Organization_link
		fields = ['id','link','organization', 'created_at', 'updated_at']


	class Organization_linkCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			organization_link = Organization_link.objects.create(**validated_data)

			return organization_link


		class Meta:
			model = Organization_link
			fields = ['link','organization']



class PermissionSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomPermission
		fields = ['id', 'official_perm_name', 'name']



class RoleSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class Meta:
		model = Role
		fields = ['id','name','permissions', 'organization', 'created_at', 'updated_at']


	class RoleCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			role = Role(name = validated_data['name'], organization = validated_data['organization'])
			role.set(validated_data['permissions'])
			role.save()

			return role


		class Meta:
			model = Role
			fields = ['name', 'permissions', 'organization']


class Organization_memberSerializer(serializers.ModelSerializer):
	user = OrganizationSerializer()
	role = RoleSerializer()
	organization = OrganizationSerializer()

	class Meta:
		model = Organization_member
		fields = ['id', 'user','role', 'organization', 'created_at', 'updated_at']


	class Organization_memberCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			organization_member = Organization_member.objects.create(**validated_data)

			return organization_member


		class Meta:
			model = Organization_member
			fields = ['user','role', 'organization']



class ServiceSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class Meta:
		model = Service
		fields = ['id', 'name', 'address', 'number', 'organization', 'created_at', 'updated_at']


	class ServiceCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			service = Service.objects.create(**validated_data)

			return service


		class Meta:
			model = Service
			fields = ['name', 'address', 'number', 'organization']


class OrderSerializer(serializers.ModelSerializer):
	creator = UserSerializer()
	executor = UserSerializer()
	service = ServiceSerializer

	class Meta:
		model = Order
		fields = ['id', 'order_code', 'description', 'creator', 'executor', 'client', 'done', 'blocked', 'service', 'created_at', 'updated_at']


	class OrderCSerializer(serializers.ModelSerializer):

		class Meta:
			model = Order
			fields = ['order_code', 'description', 'creator', 'executor', 'client', 'service']