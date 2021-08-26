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
		fields = ['id','organization', 'user']


	class ClientCSerializer(serializers.ModelSerializer):
		password = serializers.CharField(max_length=128, min_length=8, write_only=True)
		email = serializers.CharField(write_only = True)
		address = serializers.CharField(write_only = True)

		surname = serializers.CharField(write_only = True)
		name = serializers.CharField(write_only = True)
		patronymic = serializers.CharField(write_only = True)

		def create(self, validated_data):

			client_data = {'organization': validated_data.pop('organization')}

			new_user = get_user_model().objects.create_user(**validated_data)
			new_user.confirmed_email = True
			new_user.save()

			client = Client.objects.create(user = new_user, organization = client_data['organization'])

			return client


		class Meta:
			model = Client
			fields = ['organization', 'password', 'email', 'surname', 'name', 'patronymic', 'address']