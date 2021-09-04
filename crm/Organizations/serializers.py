import uuid

from rest_framework import serializers

from .models import *
from Users.serializers import UserSerializer


class OrganizationSerializer(serializers.ModelSerializer):
	creator = UserSerializer()

	class Meta:
		model = Organization
		fields = ['id','name','description', 'address', 'creator', 'created_at', 'numbers','links', 'updated_at']


	class OrganizationCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			organization = Organization.objects.create(**validated_data)

			return organization


		class Meta:
			model = Organization
			fields = ['name','description', 'address', 'links', 'numbers' 'creator']


	class OrganizationUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Organization
			fields = ['name','description', 'address', 'links', 'numbers']




class PermissionSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomPermission
		fields = ['id', 'name', 'codename']



class RoleSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()
	permissions = PermissionSerializer(many = True)

	class Meta:
		model = Role
		fields = ['id','name','permissions', 'organization', 'created_at', 'updated_at']


	class RoleCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			role = Role(name = validated_data['name'], organization = validated_data['organization'])
			role.permissions.set(set(validated_data['permissions']))
			role.save()

			return role

		class Meta:
			model = Role
			fields = ['name', 'permissions', 'organization']


	class RoleUSerializer(serializers.ModelSerializer):

		def update(self, instance, validated_data):
			if 'permissions' in validated_data:
				try:
					old_perms = set(instance.permissions.all())
					instance.permissions.set(set(validated_data['permissions']))
					add_remove_perms = set(instance.permissions.all())
					new_perms = old_perms ^ add_remove_perms
					instance.permissions.set(new_perms)
				except:
					pass

			validated_data.pop('permissions')
			return super().update(instance, validated_data)


		class Meta:
			model = Role
			fields = ['name', 'permissions']


class Organization_memberSerializer(serializers.ModelSerializer):
	user = UserSerializer()
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


	class Organization_memberUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Organization_member
			fields = ['role']



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


	class ServiceUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Service
			fields = ['name', 'address', 'number']