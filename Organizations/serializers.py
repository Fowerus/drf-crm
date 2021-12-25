from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import *
from Users.serializers import UserSerializer
from restapi.views import get_userData


class OrganizationSerializer(serializers.ModelSerializer):
	creator = UserSerializer()

	class Meta:
		model = Organization
		fields = ['id','name','description', 'address', 'creator', 'numbers','links', 'logo', 'created_at', 'updated_at']


	class OrganizationCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			creator = get_user_model().objects.get(id = get_userData(self.context['request'])['user_id'])
			validated_data['creator'] = creator

			organization = Organization.objects.create(**validated_data)

			Organization_member.objects.create(
				user = organization.creator,
				organization = organization,
				surname = organization.creator.surname,
				first_name = organization.creator.first_name,
				second_name = organization.creator.second_name,
				email = organization.creator.email,
				address = organization.creator.address,
				phone = organization.creator.phone,
				avatar = organization.creator.avatar
			)

			return organization


		class Meta:
			model = Organization
			fields = ['name','description', 'address', 'links', 'numbers', 'logo']


	class OrganizationUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Organization
			fields = ['name','description', 'address', 'links', 'numbers', 'logo']


	class OrganizationMarketplaceSerializer(serializers.ModelSerializer):
		id = serializers.IntegerField()
		name = serializers.CharField(allow_null = True)
		address = serializers.CharField(allow_null = True)


		class Meta:
			model = Organization
			fields = ['id', 'name','address', 'numbers', 'links']



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
			role = Role.objects.create(name = validated_data['name'], organization = validated_data['organization'])
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
					validated_data.pop('permissions')
				except:
					pass

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
		fields = ['id', 'user','role', 'first_name', 'surname', 'second_name',
		'address', 'phone', 'email', 'avatar', 'pass_series', 'pass_number', 'organization', 'created_at', 'updated_at']


	class Organization_memberCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			user_data = {
				"first_name": validated_data['user'].first_name,
				"surname":validated_data['user'].surname,
				"second_name":validated_data['user'].second_name,
				"phone":validated_data['user'].phone,
				"email":validated_data['user'].email,
				"address":validated_data['user'].address,
				"avatar":validated_data['user'].avatar
			}
			organization_member = Organization_member.objects.create(**validated_data, **user_data)

			return organization_member


		class Meta:
			model = Organization_member
			fields = ['user','role', 'organization']


	class Organization_memberUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Organization_member
			fields = ['role', 'first_name', 'surname', 'second_name', 'address', 'phone', 'email', 'avatar', 'pass_series', 'pass_number']


	class Organization_memberMarketplaceSerializer(serializers.ModelSerializer):
		id = serializers.IntegerField()
		surname = serializers.CharField(allow_null = True)
		first_name = serializers.CharField(allow_null = True)
		second_name = serializers.CharField(allow_null = True)
		address = serializers.CharField(allow_null = True)
		phone = serializers.CharField(allow_null = True)
		email = serializers.CharField(allow_null = True)
		avatar = serializers.CharField(allow_null = True)
		pass_series = serializers.CharField(allow_null = True)
		pass_number = serializers.CharField(allow_null = True)


		class Meta:
			model = Organization_member
			fields = ['id', 'first_name', 'surname', 'second_name', 'address', 'phone', 'email', 'avatar', 'pass_series', 'pass_number']



class ServiceSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class Meta:
		model = Service
		fields = ['id', 'name', 'address', 'phone', 'organization', 'created_at', 'updated_at']


	class ServiceCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			service = Service.objects.create(**validated_data)

			return service


		class Meta:
			model = Service
			fields = ['name', 'address', 'phone', 'organization']


	class ServiceUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Service
			fields = ['name', 'address', 'phone']



class MProviderSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()


	class MProviderCSerializer(serializers.ModelSerializer):
		token = serializers.CharField(max_length = 300, read_only = True)

		def create(self, validated_data):
			mprovider = MProvider.objects.create(**validated_data)

			validated_data['token'] = mprovider.generate_token

			return validated_data


		class Meta:
			model = MProvider
			fields = ['token', 'site', 'organization']


	class Meta:
		model = MProvider
		fields = ['id', 'token', 'site', 'organization', 'created_at', 'updated_at']
			