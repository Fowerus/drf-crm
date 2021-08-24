from django.contrib.auth import get_user_model

from rest_framework import serializers

from .models import Client
from Users.serializers import UserSerializer
from Organizations.serializers import OrganizationSerializer



class ClientSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	organization = OrganizationSerializer()

	class Meta:
		model = Client
		fields = ['id','organizaion', 'user']


	class ClientCSerializer(serializers.ModelSerializer):

		address = serializers.CharField(write_only = True)
		number = serializers.CharField(write_only = True)

		surname = serializers.CharField(write_only = True)
		name = serializers.CharField(write_only = True)
		patronymic = serializers.CharField(write_only = True)

		def create(self, validated_data):

			client_data = validated_data.pop('organizaion')

			new_user = get_user_model().objects.create_user(**validated_data)
			new_user.confirmed_email = True
			new_user.save()
			client_data['user'] = new_user.id

			client = Client.objects.create(**client_data)

			return client


		class Meta:
			model = Client
			fields = ['organizaion', 'user']