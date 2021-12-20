from rest_framework import serializers

from .models import *
from Users.serializers import UserSerializer
from restapi.views import get_userData



class MProductSerializer(serializers.ModelSerializer):

	class MProductCSerializer(serializers.ModelSerializer):
		organization = serializers.JSONField()

		class Meta:
			model = MProduct
			fields = ['name', 'count', 'price', 'price_opt', 'url_product', 'url_photo', 'address', 'provider_site', 'organization']

	class MProductUSerializer(serializers.ModelSerializer):
		organization = serializers.JSONField(read_only = True)

		class Meta:
			model = MProduct
			fields = ['name', 'count', 'price', 'price_opt', 'url_product', 'url_photo', 'address', 'provider_site', 'organization']

	class Meta:
		model = MProduct
		fields = ['_id', 'name', 'count', 'price', 'price_opt', 'url_product', 'url_photo', 'address', 'provider_site', 'organization']




class MOrderSerializer(serializers.ModelSerializer):

	class MOrderCSerializer(serializers.ModelSerializer):
		organization = serializers.JSONField()

		class Meta:
			model = MOrder
			fields = ['price', 'address', 'description', 'comment', 'products', 'courier', 'author', 'organization']

	class MOrderUSerializer(serializers.ModelSerializer):
		organization = serializers.JSONField(write_only = True)

		class Meta:
			model = MOrder
			fields = ['price', 'address', 'description', 'comment', 'products', 'courier', 'author', 'organization']

	class Meta:
		model = MOrder
		fields = ['_id', 'price', 'address', 'description', 'comment', 'products', 'courier', 'author', 'organization']




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