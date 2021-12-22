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
		_id = serializers.CharField()
		price = serializers.DecimalField(max_digits = 10, decimal_places = 2, initial = 0)
		organization = OrganizationSerializer.OrganizationMarketplaceSerializer()

		class Meta:
			model = MProduct
			# fields = ['name', 'count', 'price', 'url_product', 'url_photo', 'address', 'provider_site', 'organization']
			fields = ['_id', 'name', 'count', 'price', 'organization']

	class Meta:
		model = MProduct
		fields = ['_id', 'name', 'count', 'price', 'price_opt', 'url_product', 'url_photo', 'address', 'provider_site', 'organization']




class MBusketSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer.OrganizationMarketplaceSerializer()
	products = MProductSerializer.MProductMBusketSerializer(many = True)
	author = Organization_memberSerializer.Organization_memberMarketplaceSerializer()

	class MBusketCSerializer(serializers.ModelSerializer):
		organization = serializers.JSONField()
		products = MProductSerializer.MProductMBusketSerializer(many = True)
		author = serializers.JSONField(read_only = True)

		def create(self, validated_data):
			author_user_id = get_userData(self.context['request'])['user_id']
			organization_id = validated_data.get('organization').get('id')
			validated_data['organization'] = OrganizationSerializer.OrganizationMarketplaceSerializer(get_organizationData(organization_id)).data
			validated_data['author'] = Organization_memberSerializer.Organization_memberMarketplaceSerializer(get_authorData(author_user_id, organization_id)).data
			mbusket = MBusket.objects.create(**validated_data)
			mbusket.calculate_price
			mbusket.calculate_count
			mbusket.save()
			return mbusket

		class Meta:
			model = MBusket
			fields = fields = ['products', 'author', 'organization']

	class MBusketUSerializer(serializers.ModelSerializer):
		products = MProductSerializer.MProductMBusketSerializer(many = True)

		class Meta:
			model = MBusket
			fields = ['products']

	class Meta:
		model = MBusket
		fields = ['_id', 'products', 'price', 'count', 'author', 'organization', 'created_at', 'updated_at']




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
