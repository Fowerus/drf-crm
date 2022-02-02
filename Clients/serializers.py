import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers
from rest_framework.response import Response

from rest_framework_simplejwt import exceptions

from .models import Client, ClientCard
from Users.serializers import UserSerializer, UserRegistrationSerializer
from Organizations.serializers import OrganizationSerializer
from Sessions.models import Session_client

from core.utils.atomic_exception import MyCustomError


class ClientSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer(many=True)

    class ClientUSerializer(serializers.ModelSerializer):

        def update(self, instance, validated_data):
            if 'password' in validated_data:
                instance.set_password(validated_data['password'])
                validated_data.pop('password')
            if 'phone' in validated_data:
                instance.phone = validated_data['phone']
                instance.confirmed_phone = False
                validated_data.pop('phone')

            return super().update(instance, validated_data)

        class Meta:
            model = Client
            fields = ['surname', 'first_name',
                      'second_name', 'phone', 'address', 'logo']

    class Meta:
        model = Client
        fields = ['id', 'surname', 'first_name', 'second_name', 'phone',
                  'address', 'confirmed_phone', 'organization', 'created_at', 'updated_at']


class ClientCardSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    client = ClientSerializer()

    class ClientCardCSerializer(serializers.ModelSerializer):
        password = serializers.CharField(max_length=128, write_only=True)

        @transaction.atomic
        def create(self, validated_data):
            organization = validated_data.pop('organization')
            try:
                client = Client.objects.get(phone=validated_data['phone'])
                client.organization.add(organization)
                client.save()

            except Exception as e:
                password = validated_data['password']
                client = Client.objects.create(
                    **validated_data, phone=validated_data('phone'))
                client.set_password(password)
                client.organization.add(organization)
                client.save()

            try:
                client_card = ClientCard.objects.select_related('organization').filter(
                    organization=organization).get(phone=validated_data['phone'])

            except Exception as e:
                validated_data.pop('password')
                client_card = ClientCard.objects.create(
                    organization=organization, client=client, **validated_data)

            return client_card

        class Meta:
            model = ClientCard
            fields = ['surname', 'first_name', 'second_name',
                      'phone', 'address', 'organization']

    class ClientCardUSerializer(serializers.ModelSerializer):

        class Meta:
            model = ClientCard
            fields = ['surname', 'first_name',
                      'second_name', 'phone', 'address', 'links']

    class Meta:
        model = ClientCard
        fields = ['id', 'surname', 'first_name', 'second_name', 'phone',
                  'address', 'organization', 'client', 'created_at', 'updated_at']


class ClientLoginSerializer(serializers.Serializer):
    phone = serializers.CharField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    detail = serializers.CharField(read_only=True)
    token = serializers.ReadOnlyField()
    device = serializers.CharField(write_only=True)

    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        phone = data.get('phone', None)
        password = data.get('password', None)
        device = data.get('device', None)

        if phone is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if password is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if device is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            client = Client.objects.get(phone=phone)

            if client.check_password(password):
                try:
                    Session_client.objects.select_related('client').filter(
                        client=client.id).get(device=device)
                    return {"detail": "Already authorized"}
                except Exception as e:
                    session = Session_client.objects.create(
                        client=client, device=device)
                    token_encode = jwt.encode({
                        'client_id': client.id,
                        'surname': client.surname,
                        'first_name': client.first_name,
                        'second_name': str(client.second_name),
                        'phone': client.phone.raw_input,
                        'session': session.id
                    }, settings.SECRET_KEY, algorithm='HS256')
                    validated_data = {'token': token_encode}

                    return validated_data

        except Exception as e:
            raise MyCustomError(
                'No active account found with the given credentials', 400)

        raise MyCustomError(
            'No active account found with the given credentials', 400)
