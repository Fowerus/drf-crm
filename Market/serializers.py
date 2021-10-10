from rest_framework import serializers
from django.db import transaction


from Users.serializers import UserSerializer
from Organizations.serializers import ServiceSerializer, OrganizationSerializer
from Clients.serializers import ClientSerializer
from Handbook.serializers import ServicePriceSerializer
from Orders.serializers import OrderSerializer
from .models import *



class ProductCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductCategory
		fields = ['id', 'name', 'created_at', 'updated_at']



class CashboxSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()
	service = ServiceSerializer()

	class Meta:
		model = Cashbox
		fields = ['id', 'name', 'cash', 'account_money', 'organization', 'service', 'created_at', 'updated_at']

	class CashboxCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			cashbox = Cashbox.objects.create(**validated_data)

			return cashbox

		class Meta:
			model = Cashbox
			fields = ['name', 'cash', 'account_money', 'organization', 'service']

	class CashboxUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Cashbox
			fields = ['name', 'cash', 'account_money', 'service']



class PurchaseSerializer(serializers.ModelSerializer):
	cashbox = CashboxSerializer()
	service = ServiceSerializer()
	organization = OrganizationSerializer()


	class Meta:
		model = Purchase
		fields = ['id', 'price', 'organization', 'cashbox', 'service', 'is_deferred', 'created_at', 'updated_at']

	class PurchaseCSerializer(serializers.ModelSerializer):

		@transaction.atomic
		def create(self, validated_data):
			purchase = Purchase.objects.create(**validated_data)
			purchase.cashbox.cash -= purchase.price
			purchase.save()

			return purchase

		class Meta:
			model = Purchase
			fields = ['price', 'organization', 'cashbox', 'service', 'is_deferred']

	class PurchaseUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Purchase
			fields = ['price', 'cashbox', 'service', 'is_deferred']



class SaleSerializer(serializers.ModelSerializer):
	cashbox = CashboxSerializer()
	service = ServiceSerializer()
	organization = OrganizationSerializer()
	client = ClientSerializer()


	class Meta:
		model = Sale
		fields = ['id', 'cash', 'card', 'bank_transfer', 'discount', 'client', 
		'organization', 'cashbox', 'service', 'is_deferred', 'created_at', 'updated_at']

	class SaleCSerializer(serializers.ModelSerializer):

		@transaction.atomic
		def create(self, validated_data):
			sale = Sale.objects.create(**validated_data)
			sale.cashbox.cash += sale.cash + sale.card
			sale.save()

			return sale

		class Meta:
			model = Sale
			fields = ['cash', 'card', 'bank_transfer', 'discount', 'client', 
		'organization', 'cashbox', 'service', 'is_deferred']


	class SaleUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Sale
			fields = ['cash', 'card', 'bank_transfer', 'discount', 'client', 
			'cashbox', 'service', 'is_deferred']



class ProductSerializer(serializers.ModelSerializer):
	service = ServiceSerializer()
	organization = OrganizationSerializer()
	sale = SaleSerializer()
	purchase = PurchaseSerializer()
	category = ProductCategorySerializer()


	class Meta:
		model = Product
		fields = ['id', 'name', 'code', 'barcode', 'purchase_price', 'sale_price', 'count',
		'supplier', 'irreducible_balance', 'organization', 'purchase', 'sale', 'service', 'category', 'created_at', 'updated_at']

	class ProductCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			product = Product.objects.create(**validated_data)

			return product

		class Meta:
			model = Product
			fields = ['name', 'code', 'barcode', 'purchase_price', 'sale_price', 'count',
			'supplier', 'irreducible_balance', 'organization', 'purchase', 'sale', 'service', 'category']

	class ProductUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Product
			fields = ['name', 'purchase_price', 'sale_price', 'count',
			'supplier', 'irreducible_balance', 'purchase', 'sale', 'service', 'category']



class WorkDoneSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()
	service_price = ServicePriceSerializer()
	user = UserSerializer()
	order = OrderSerializer()
	service = ServiceSerializer()


	class Meta:
		model = WorkDone
		fields = ['id', 'name', 'price', 'organization', 'service_price', 
		'user', 'order', 'service', 'created_at', 'updated_at']

	class WorkDoneCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			work_done = WorkDone.objects.create(**validated_data)

			return work_done

		class Meta:
			model = WorkDone
			fields = ['name', 'price', 'organization', 'service_price', 
			'user', 'order', 'service']

	class WorkDoneUSerializer(serializers.ModelSerializer):

		class Meta:
			model = WorkDone
			fields = ['name', 'price', 'service_price', 
			'user', 'order', 'service']
			


class ProductOrderSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()
	product = ProductSerializer()
	order = OrderSerializer()
	service = ServiceSerializer()


	class Meta:
		model = ProductOrder
		fields = ['id', 'name', 'price', 'organization', 'product', 
		'order', 'service', 'created_at', 'updated_at']

	class ProductOrderCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			product_order = ProductOrder.objects.create(**validated_data)

			return product_order

		class Meta:
			model = ProductOrder
			fields = ['name', 'price', 'organization', 'product', 
			'order', 'service']

	class ProductOrderUSerializer(serializers.ModelSerializer):

		class Meta:
			model = ProductOrder
			fields = ['name', 'price', 'organization', 'product', 
			'order', 'service']