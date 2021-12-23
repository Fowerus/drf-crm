from bson.objectid import ObjectId

from rest_framework import serializers
from restapi.atomic_exception import MyCustomError

from .models import *
from Organizations.serializers import Organization_memberSerializer, OrganizationSerializer
from restapi.views import get_userData, get_orgId, get_organizationData, get_authorData, get_productsData, get_organization_memberData



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
		_id = serializers.CharField()
		price = serializers.DecimalField(max_digits = 10, decimal_places = 2, initial = 0)
		organization = OrganizationSerializer.OrganizationMarketplaceSerializer()
		done = serializers.BooleanField(default = False)

		class Meta:
			model = MProduct
			# fields = ['_id', 'name', 'count', 'price', 'price_opt', 'url_product', 'url_photo', 'address', 'provider_site', 'done', 'organization']
			fields = ['_id', 'name', 'count', 'price', 'organization']

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
		products = serializers.JSONField()
		author = serializers.JSONField(read_only = True)
		price = serializers.DecimalField(max_digits = 10, decimal_places = 2, read_only = True)
		count = serializers.IntegerField(read_only = True)

		def create(self, validated_data):
			author_user_id = get_userData(self.context['request'])['user_id']
			organization_id = get_orgId(self.context.get("request"))

			mbusket = MBusket.objects.filter(organization = {'id':organization_id})
			if mbusket.exists():
				raise MyCustomError(f'The busket is already created ({mbusket.first()._id})', 200)
			try:
				validated_data['organization'] = OrganizationSerializer.OrganizationMarketplaceSerializer(get_organizationData(organization_id)).data
				validated_data['author'] = Organization_memberSerializer.Organization_memberMarketplaceSerializer(get_authorData(author_user_id, organization_id)).data
				validated_data['products'] = MProductSerializer.MProductMBusketSerializer(get_productsData(validated_data.get('products')),many = True).data
				mbusket = MBusket(**validated_data)
				mbusket.calculate_price
				mbusket.calculate_count
				mbusket.save()
				return mbusket
			except:
				raise MyCustomError('Creating organization busket error', 500)


		class Meta:
			model = MBusket
			fields = ['products', 'author', 'organization', 'price', 'count']

	class MBusketUSerializer(serializers.ModelSerializer):
		organization = serializers.JSONField(read_only = True)
		products = serializers.JSONField()
		author = serializers.JSONField(read_only = True)
		price = serializers.DecimalField(max_digits = 10, decimal_places = 2, read_only = True)
		count = serializers.IntegerField(read_only = True)

		def update(self, instance, validated_data):
			
			instance.products = MProductSerializer.MProductMBusketSerializer(get_productsData(validated_data.get('products')),many = True).data
			instance.calculate_price
			instance.calculate_count
			instance.save()

			validated_data.pop('products')
			return super().update(instance, validated_data)



		class Meta:
			model = MBusket
			fields = ['products', 'author', 'organization', 'price', 'count']

	class Meta:
		model = MBusket
		fields = ['_id', 'products', 'price', 'count', 'author', 'organization', 'created_at', 'updated_at']




class MCourierSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer.OrganizationMarketplaceSerializer()
	courier = Organization_memberSerializer.Organization_memberMarketplaceSerializer()

	class MCourierCSerializer(serializers.ModelSerializer):
		organization = serializers.JSONField(read_only = True)
		courier = serializers.JSONField()

		def create(self, validated_data):
			organization_id = get_orgId(self.context.get("request"))
			validated_data['organization'] = OrganizationSerializer.OrganizationMarketplaceSerializer(get_organizationData(organization_id)).data
			validated_data['courier'] = Organization_memberSerializer.Organization_memberMarketplaceSerializer(get_organization_memberData(validated_data.get('courier'), organization_id)).data

			return super().create(validated_data)

		class Meta:
			model = MCourier
			fields = ['courier', 'organization']

	class MCourierUSerializer(serializers.ModelSerializer):
		courier = serializers.JSONField()

		def update(self, instance, validated_data):
			organization_id = get_orgId(self.context.get("request"))
			validated_data['courier'] = Organization_memberSerializer.Organization_memberMarketplaceSerializer(get_organization_memberData(validated_data.get('courier'), organization_id)).data
			return super().update(instance, validated_data)

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
		organization = serializers.JSONField()
		products = serializers.JSONField()
		author = serializers.JSONField(read_only = True)
		courier = serializers.JSONField(allow_null = True)
		price = serializers.DecimalField(max_digits = 10, decimal_places = 2, read_only = True)
		count = serializers.IntegerField(read_only = True)

		def create(self, validated_data):
			author_user_id = get_userData(self.context['request'])['user_id']
			organization_id = get_orgId(self.context.get("request"))

			validated_data['organization'] = OrganizationSerializer.OrganizationMarketplaceSerializer(get_organizationData(organization_id)).data
			validated_data['author'] = Organization_memberSerializer.Organization_memberMarketplaceSerializer(get_authorData(author_user_id, organization_id)).data
			validated_data['products'] = MProductSerializer.MProductMOrderSerializer(get_productsData(validated_data.get('products'), is_order = True),many = True).data

		class Meta:
			model = MOrder
			fields = ['price', 'address', 'description', 'comment', 'products', 'courier', 'author', 'organization']

	class MOrderUSerializer(serializers.ModelSerializer):
		courier = MCourierSerializer()
		done_list = serializers.JSONField(allow_null = True)

		class Meta:
			model = MOrder
			fields = ['done_list', 'address', 'description', 'comment', 'courier']

	class Meta:
		model = MOrder
		fields = ['_id', 'price', 'address', 'description', 'comment', 'products', 'courier', 'author', 'organization']
