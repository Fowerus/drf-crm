from rest_framework import serializers
from Users.serializers import UserSerializer
from Organizations.serializers import OrganizationSerializer
from .models import Client


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

			new_user = User.objects.create_user(**validated_data)
			client_data['user'] = new_user.id

			client = Client.objects.create(**client_data)

			return client


		class Meta:
			model = Client
			fields = ['organizaion', 'user']