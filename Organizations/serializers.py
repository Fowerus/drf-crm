from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

from .models import *
from Users.serializers import UserSerializer
from core.views import get_userData


class OrganizationSerializer(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = Organization
        fields = ['id', 'name', 'description', 'address', 'creator',
                  'numbers', 'links', 'logo', 'created_at', 'updated_at']

    class OrganizationCSerializer(serializers.ModelSerializer):

        @transaction.atomic
        def create(self, validated_data):
            creator = get_user_model().objects.get(
                id=get_userData(self.context['request'])['user_id'])
            validated_data['creator'] = creator

            organization = Organization.objects.create(**validated_data)

            Organization_member.objects.create(
                user=organization.creator,
                organization=organization,
                surname=organization.creator.surname,
                first_name=organization.creator.first_name,
                second_name=organization.creator.second_name,
                email=organization.creator.email,
                address=organization.creator.address,
                phone=organization.creator.phone,
                avatar=organization.creator.avatar
            )

            return organization

        class Meta:
            model = Organization
            fields = ['name', 'description',
                      'address', 'links', 'numbers', 'logo']

    class OrganizationUSerializer(serializers.ModelSerializer):

        class Meta:
            model = Organization
            fields = ['name', 'description',
                      'address', 'links', 'numbers', 'logo']

    class OrganizationMarketplaceSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField()
        name = serializers.CharField(allow_null=True)
        address = serializers.CharField(allow_null=True)
        logo = serializers.CharField(allow_null=True)

        class Meta:
            model = Organization
            fields = ['id', 'name', 'address', 'numbers', 'links', 'logo']


class Organization_memberSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    organization = OrganizationSerializer()

    class Meta:
        model = Organization_member
        fields = ['id', 'user', 'first_name', 'surname', 'second_name',
                  'address', 'phone', 'email', 'avatar', 'pass_series', 'pass_number', 'organization', 'created_at', 'updated_at']

    class Organization_memberCSerializer(serializers.ModelSerializer):

        def create(self, validated_data):
            user_data = {
                "first_name": validated_data['user'].first_name,
                "surname": validated_data['user'].surname,
                "second_name": validated_data['user'].second_name,
                "phone": validated_data['user'].phone,
                "email": validated_data['user'].email,
                "address": validated_data['user'].address,
                "avatar": validated_data['user'].avatar
            }
            organization_member = Organization_member.objects.create(
                **validated_data, **user_data)

            return organization_member

        class Meta:
            model = Organization_member
            fields = ['user', 'organization']

    class Organization_memberUSerializer(serializers.ModelSerializer):
        user = UserSerializer(read_only = True)
        class Meta:
            model = Organization_member
            fields = ['user', 'first_name', 'surname', 'second_name', 'address',
                      'phone', 'email', 'avatar', 'pass_series', 'pass_number']

    class Organization_memberMarketplaceSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField()
        surname = serializers.CharField(allow_null=True)
        first_name = serializers.CharField(allow_null=True)
        second_name = serializers.CharField(allow_null=True)
        address = serializers.CharField(allow_null=True)
        phone = serializers.CharField(allow_null=True)
        email = serializers.CharField(allow_null=True)
        avatar = serializers.CharField(allow_null=True)
        pass_series = serializers.CharField(allow_null=True)
        pass_number = serializers.CharField(allow_null=True)

        class Meta:
            model = Organization_member
            fields = ['id', 'first_name', 'surname', 'second_name', 'address',
                      'phone', 'email', 'avatar', 'pass_series', 'pass_number']


class ServiceSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Service
        fields = ['id', 'name', 'address', 'phone',
                  'organization', 'created_at', 'updated_at']

    class ServiceCSerializer(serializers.ModelSerializer):

        @transaction.atomic
        def create(self, validated_data):
            service = Service.objects.create(**validated_data)
            members = Organization.objects.get(id = validated_data.get('organization').id).organization_members.all()

            for m in members:

                m.user.services = list(set(m.user.services + [service.id]))
                m.user.save()

            return service

        class Meta:
            model = Service
            fields = ['name', 'address', 'phone', 'organization']

    class ServiceUSerializer(serializers.ModelSerializer):

        class Meta:
            model = Service
            fields = ['name', 'address', 'phone']


    class ServiceMarketplaceSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField()
        name = serializers.CharField(allow_null=True)
        address = serializers.CharField(allow_null=True)
        phone = serializers.CharField(allow_null = True)

        class Meta:
            model = Service
            fields = ['id', 'name', 'address', 'phone']


class MProviderSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    service = ServiceSerializer()

    class MProviderCSerializer(serializers.ModelSerializer):
        token = serializers.CharField(max_length=300, read_only=True)

        def create(self, validated_data):
            mprovider = MProvider.objects.create(**validated_data)

            validated_data['token'] = mprovider.generate_token

            return validated_data

        class Meta:
            model = MProvider
            fields = ['token', 'site', 'service', 'organization']

    class Meta:
        model = MProvider
        fields = ['id', 'site', 'service',
                  'organization', 'created_at', 'updated_at']
