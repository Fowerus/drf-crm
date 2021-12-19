from rest_framework import serializers

from .models import *
from Users.serializers import UserSerializer
from restapi.views import get_userData



class MCourierSerializer(serializers.ModelSerializer):

	class MCourierCSerializer(serializers.ModelSerializer):
		organization = serializers.JSONField()
		courier = serializers.JSONField()

		class Meta:
			model = MCourier
			fields = ['courier', 'organization']

	class Meta:
		model = MCourier
		fields = ['_id', 'courier', 'organization']