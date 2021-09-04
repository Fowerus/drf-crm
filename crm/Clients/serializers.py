from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.response import Response

from rest_framework_simplejwt import exceptions

from .models import Client
from Users.serializers import UserSerializer, UserRegistrationSerializer
from Organizations.serializers import OrganizationSerializer
from Sessions.models import Session_client



class ClientSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer(many = True)

	class ClientCUSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			try:
				client = Client.objects.get(number = validated_data['number'])
				client.add(validated_data['organization'][0])
				client.save()
				return Client
			except:
				organization = validated_data.pop('organization')
				password = validated_data['password']
				client = Client.objects.create(**validated_data)
				client.set_password(password)
				client.organization.add(organization[0])
				client.save()

				return client


		def update(self, instance, validated_data):
			password = serializers.CharField(max_length = 128, write_only = True)

			validated_data.pop('organization')

			if 'number' in validated_data:
				instance.number = validated_data['number']
				instance.confirmed_number = False
				validated_data.pop('number')

			if 'password' in validated_data:
				instance.set_password(validated_data['password'])
				validated_data.pop('password')

			return super().update(instance, validated_data)


		class Meta:
			model = Client
			fields = ['surname', 'name', 'patronymic', 'number', 'address', 'organization', 'links', 'password']
			

	class Meta:
		model = Client
		fields = ['id', 'surname', 'name', 'patronymic', 'number', 'address', 'confirmed_number', 'organization', 'created_at', 'updated_at']



class ClientLoginSerializer(serializers.Serializer):
	number = serializers.CharField(write_only=True)
	password = serializers.CharField(max_length=128, write_only=True)
	detail = serializers.CharField(read_only = True)
	token = serializers.ReadOnlyField()
	device = serializers.CharField(write_only = True)

	token = serializers.CharField(max_length=255, read_only=True)


	def validate(self, data):
		number = data.get('number',None)
		password = data.get('password',None)
		device = data.get('device', None)

		if number is None:
			return Response(status = status.HTTP_404_NOT_FOUND)

		if password is None:
			return Response(status = status.HTTP_404_NOT_FOUND)

		if device is None:
			return Response(status = status.HTTP_404_NOT_FOUND)

		try:
			client = Client.objects.get(number = number)

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