from bson.objectid import ObjectId
from rest_framework import serializers

from .models import *
from Organizations.serializers import Organization_memberSerializer, OrganizationSerializer
from restapi.views import get_userData, get_organizationData, get_authorData, get_productsData



class MProductSerializer(serializers.ModelSerializer):

	class MProductCSerializer(serializers.ModelSerializer):
		organization = OrganizationSerializer.OrganizationMarketplaceSerializer()

		class Meta:
			model = MProduct
			fields = ['name', 'count', 'price', 'price_opt', 'url_product', 'url_photo', 'address', 'provider_site', 'organization']

	class MProductUSerializer(serializers.ModelSerializer):

		class Meta:
			model = MProduct
			fields = ['name', 'count', 'price', 'price_opt', 'url_product', 'url_photo', 'address', 'provider_site']

	class MProductMOrderSerializer(serializers.ModelSerializer):
		organization = OrganizationSerializer.OrganizationMarketplaceSerializer()
		price_opt = serializers.DecimalField(max_digits = 10, decimal_places = 2, initial = 0)
		done = serializers.BooleanField(default = False)

		class Meta:
			model = MProduct
			fields = ['_id', 'name', 'count', 'price', 'price_opt', 'url_product', 'url_photo', 'address', 'provider_site', 'done', 'organization']

	class MProductMBusketSerializer(serializers.ModelSerializer):
		organization = OrganizationSerializer.OrganizationMarketplaceSerializer()

		class Meta:
			model = MProduct
			fields = ['name', 'count', 'price', 'url_product', 'url_photo', 'address', 'provider_site', 'organization']

	class Meta:
		model = MProduct
		fields = ['_id', 'name', 'count', 'price', 'price_opt', 'url_product', 'url_photo', 'address', 'provider_site', 'organization']




class MBusketSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer.OrganizationMarketplaceSerializer()
	products = MProductSerializer.MProductMBusketSerializer(many = True)
	author = Organization_memberSerializer.Organization_memberMarketplaceSerializer()

	class MBusketCSerializer(serializers.ModelSerializer):
		organization = serializers.JSONField()
		products = serializers.ListField(child = serializers.JSONField())
		author = serializers.JSONField(read_only = True)

		def create(self, validated_data):
			author_user_id = get_userData(self.context['request'])['user_id']
			organization_id = validated_data.get('organization').get('id')
			validated_data['organization'] = get_organizationData(organization_id)
			validated_data['author'] = get_authorData(author_user_id, organization_id)
			validated_data['products'] = get_productsData(validated_data.get('products'))
			mbusket = MBusket.objects.create(**validated_data)
			mbusket.calculate_price
			mbusket.calculate_count
			mbusket.save()

			return mbusket

		class Meta:
			model = MBusket
			fields = fields = ['products', 'author', 'organization']

	class MBusketUSerializer(serializers.ModelSerializer):
		products = serializers.ListField(child = serializers.JSONField())

		def update(self, instance, validated_data):
			validated_data['products'] = MProductSerializer.MProductMBusketSerializer(get_productsBusketData(validated_data.get('products')), many = True)
			return super(instance, validated_data)

		class Meta:
			model = MBusket
			fields = ['products']

	class Meta:
		model = MBusket
		fields = ['_id', 'products', 'author', 'organization']




class MCourierSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer.OrganizationMarketplaceSerializer()
	courier = Organization_memberSerializer.Organization_memberMarketplaceSerializer()

	class MCourierCSerializer(serializers.ModelSerializer):
		organization = OrganizationSerializer.OrganizationMarketplaceSerializer()
		courier = Organization_memberSerializer.Organization_memberMarketplaceSerializer()

		class Meta:
			model = MCourier
			fields = ['courier', 'organization']

	class MCourierUSerializer(serializers.ModelSerializer):
		courier = Organization_memberSerializer.Organization_memberMarketplaceSerializer()

		class Meta:
			model = MCourier
			fields = ['courier']

	class Meta:
		model = MCourier
		fields = ['_id', 'courier', 'organization']



class MOrderSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer.OrganizationMarketplaceSerializer()
	courier = MCourierSerializer()
	author = Organization_memberSerializer.Organization_memberMarketplaceSerializer()
	products = MProductSerializer.MProductMOrderSerializer(many = True)

	class MOrderCSerializer(serializers.ModelSerializer):
		organization = OrganizationSerializer.OrganizationMarketplaceSerializer()
		courier = MCourierSerializer()
		author = Organization_memberSerializer.Organization_memberMarketplaceSerializer()
		products = MProductSerializer.MProductMOrderSerializer(many = True)

		class Meta:
			model = MOrder
			fields = ['price', 'address', 'description', 'comment', 'products', 'courier', 'author', 'organization']

	class MOrderUSerializer(serializers.ModelSerializer):
		courier = MCourierSerializer()

		class Meta:
			model = MOrder
			fields = ['address', 'description', 'comment', 'courier']

	class Meta:
		model = MOrder
		fields = ['_id', 'price', 'address', 'description', 'comment', 'products', 'courier', 'author', 'organization']
