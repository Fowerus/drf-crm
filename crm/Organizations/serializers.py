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
		fields = ['id','name','description', 'address', 'creator']


	class OrganizationCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			new_organization = Organization.objects.create(**validated_data)

			return new_organization


		class Meta:
			model = Organization
			fields = ['name','description', 'address', 'creator']



class Organization_numberSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class Meta:
		model = Organization_number
		fields = ['id','number','organization']


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
		fields = ['id','link','organization']


	class Organization_linkCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			organization_link = Organization_link.objects.create(**validated_data)

			return organization_link


		class Meta:
			model = Organization_link
			fields = ['link','organization']



class PermissionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Permission
		fields = ['id', 'official_perm_name', 'name']



class RoleSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class Meta:
		model = Role
		fields = ['id''name','permissions', 'organization']


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
	organization = OrganizationSerializer()
	role = RoleSerializer()
	organization = OrganizationSerializer()

	class Meta:
		model = Organization_member
		fields = ['id''user','role', 'organization']


	class Organization_memberCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			organization_member = Organization_member.objects.create(**validated_data)

			return organization_member


		class Meta:
			model = Organization_member
			fields = ['name','permissions', 'organization']