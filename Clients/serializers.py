from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.response import Response

from rest_framework_simplejwt import exceptions

from .models import Client, ClientCard
from Users.serializers import UserSerializer, UserRegistrationSerializer
from Organizations.serializers import OrganizationSerializer
from Sessions.models import Session_client



class ClientSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer(many = True)


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
		fields = ['id', 'surname', 'name', 'patronymic', 'phone', 'address', 'confirmed_phone', 'organization', 'created_at', 'updated_at']



class ClientCardSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()
	client = ClientSerializer()

	class ClientCardCSerializer(serializers.ModelSerializer):
		password = serializers.CharField(max_length = 128, write_only = True)

		def create(self, validated_data):
			organization = validated_data.pop('organization')[0]
			try:
				client = Client.objects.get(phone = validated_data['phone'])
				client.add(organization)
				client.save()

			except:
				password = validated_data['password']
				client = Client.objects.create(**validated_data)
				client.set_password(password)
				client.organization.add(organization)
				client.save()

			try:
				client_card = ClientCard.objects.filter(organization__id = organization).get(phone = validated_data['phone'])

			except:

				client_card = ClientCard.objects.create(organization = organization, client = client, **validated_data)

			return client_card


		class Meta:
			model = ClientCard
			fields = ['surname', 'name', 'patronymic', 'phone', 'address', 'organization', 'password']



	class ClientCardUSerializer(serializers.ModelSerializer):
		password = serializers.CharField(max_length = 128, write_only = True)

		def update(self, instance, validated_data):

			if 'phone' in validated_data:
				instance.phone = validated_data['phone']
				instance.confirmed_phone = False
				validated_data.pop('phone')

			if 'password' in validated_data:
				instance.client.set_password(validated_data['password'])
				validated_data.pop('password')

			return super().update(instance, validated_data)


		class Meta:
			model = Client
			fields = ['surname', 'name', 'patronymic', 'phone', 'address', 'links', 'password']
			

	class Meta:
		model = Client
		fields = ['id', 'surname', 'name', 'patronymic', 'phone', 'address', 'confirmed_phone', 'organization', 'client', 'created_at', 'updated_at']



class ClientLoginSerializer(serializers.Serializer):
	phone = serializers.CharField(write_only=True)
	password = serializers.CharField(max_length=128, write_only=True)
	detail = serializers.CharField(read_only = True)
	token = serializers.ReadOnlyField()
	device = serializers.CharField(write_only = True)

	token = serializers.CharField(max_length=255, read_only=True)


	def validate(self, data):
		phone = data.get('phone',None)
		password = data.get('password',None)
		device = data.get('device', None)

		if phone is None:
			return Response(status = status.HTTP_404_NOT_FOUND)

		if password is None:
			return Response(status = status.HTTP_404_NOT_FOUND)

		if device is None:
			return Response(status = status.HTTP_404_NOT_FOUND)

		try:
			client = Client.objects.get(phone = phone)

			if client.check_password(password):
				try:
					Session_client.objects.filter(client = client.id).get(device = device)
					return {"detail": "Already authorized"}
				except:
					Session_client.objects.create(client = client, device = device)

					validated_data = {'token':client.token}

					return validated_data

		except:
			self.error_messages.clear()
			raise exceptions.AuthenticationFailed(self.error_messages['detail'], 'No active account found with the given credentials')

		self.error_messages.clear()
		raise exceptions.AuthenticationFailed(self.error_messages['detail'], 'No active account found with the given credentials')
		