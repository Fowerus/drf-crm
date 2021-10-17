from django.db import transaction
from rest_framework import serializers


from Users.serializers import UserSerializer
from Organizations.serializers import ServiceSerializer, OrganizationSerializer
from Clients.serializers import ClientSerializer
from Handbook.serializers import ServicePriceSerializer, OrderHistorySerializer
from Orders.serializers import OrderSerializer
from .models import *
from Handbook.models import OrderHistory

from crm.atomic_exception import MyCustomError
from crm.views import get_viewName



class ProductCategorySerializer(serializers.ModelSerializer):

	class Meta:
		model = ProductCategory
		fields = ['id', 'name', 'created_at', 'updated_at']



class TransactionCSerializer(serializers.ModelSerializer):

	def create(self, validated_data):
		transaction = Transaction.objects.create(**validated_data)

		return transaction

	class Meta:
		model = Transaction
		fields = ['cashbox','purchase', 'organization']



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



class ProductSerializer(serializers.ModelSerializer):
	service = ServiceSerializer()
	organization = OrganizationSerializer()
	category = ProductCategorySerializer()


	class Meta:
		model = Product
		fields = ['id', 'name', 'code', 'barcode', 'purchase_price', 'sale_price', 'count',
		'supplier', 'irreducible_balance', 'organization', 'service', 'category', 'created_at', 'updated_at']


	class ProductCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			product = Product.objects.create(**validated_data)

			return product

		class Meta:
			model = Product
			fields = ['name', 'code', 'barcode', 'purchase_price', 'sale_price', 'count',
			'supplier', 'irreducible_balance', 'organization', 'service', 'category']

	class ProductUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Product
			fields = ['name', 'purchase_price', 'sale_price', 'count',
			'supplier', 'irreducible_balance', 'service', 'category']



class PurchaseSerializer(serializers.ModelSerializer):
	cashbox = CashboxSerializer()
	service = ServiceSerializer()
	organization = OrganizationSerializer()
	product = ProductSerializer()


	class Meta:
		model = Purchase
		fields = ['id', 'price', 'organization', 'cashbox', 'service', 'is_deferred', 'product', 'created_at', 'updated_at']

	class PurchaseCSerializer(serializers.ModelSerializer):
		is_cash = serializers.BooleanField(default = False)

		@transaction.atomic
		def create(self, validated_data):

			is_cash = validated_data.pop('is_cash')
			purchase = Purchase.objects.create(**validated_data)
			if is_cash:
				purchase.cashbox.cash -= purchase.price
			else:
				purchase.cashbox.account_money -= purchase.price

			if purchase.cashbox.calculate_min_money < 0:
				raise MyCustomError('Insufficient money at the cashbox', 400)

			purchase.cashbox.save()
			purchase.save()

			transaction_data = {
				"cashbox":validated_data['cashbox'].id,
				"purchase":purchase.id,
				"organization":validated_data['organization'].id
			}

			transaction = TransactionCSerializer(data = transaction_data)
			transaction.is_valid()
			transaction.save()

			return purchase

		class Meta:
			model = Purchase
			fields = ['price', 'organization', 'cashbox', 'service', 'product', 'is_deferred', 'is_cash']

	class PurchaseUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Purchase
			fields = ['price', 'cashbox', 'service', 'is_deferred']



class SaleSerializer(serializers.ModelSerializer):
	cashbox = CashboxSerializer()
	service = ServiceSerializer()
	organization = OrganizationSerializer()
	client = ClientSerializer()
	product = ProductSerializer()


	class Meta:
		model = Sale
		fields = ['id', 'cash', 'card', 'bank_transfer', 'discount', 'client', 
		'organization', 'cashbox', 'product', 'service', 'is_deferred', 'created_at', 'updated_at']

	class SaleCSerializer(serializers.ModelSerializer):

		@transaction.atomic
		def create(self, validated_data):
			sale = Sale.objects.create(**validated_data)
			sale.cashbox.cash += sale.cash*(1 + discount)
			sale.cashbox.card += (sale.card + sale.bank_transfer)*(1 + discount)

			sale.cashbox.save()
			sale.save()

			transaction_data = {
				"cashbox":validated_data['cashbox'].id,
				"sale":sale.id,
				"organization":validated_data['organization'].id
			}

			transaction = TransactionCSerializer(data = transaction_data)
			transaction.is_valid()
			transaction.save()

			return sale

		class Meta:
			model = Sale
			fields = ['cash', 'card', 'bank_transfer', 'discount', 'client', 
		'organization', 'cashbox', 'product', 'service', 'is_deferred']


	class SaleUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Sale
			fields = ['cash', 'card', 'bank_transfer', 'discount', 'client', 
			'cashbox', 'service', 'is_deferred']



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

		@transaction.atomic
		def create(self, validated_data):
			product_order = ProductOrder.objects.create(**validated_data)
			product_order.product.count -= 1

			if product_order.product.count < 0:
				raise MyCustomError("The product's quantity is no enough")

			product_order.product.save()
			product_order.save()

			return product_order

		class Meta:
			model = ProductOrder
			fields = ['name', 'price', 'organization', 'product', 
			'order', 'service']

	class ProductOrderUDSerializer(serializers.ModelSerializer):

		@transaction.atomic
		def delete(self, instance, validated_data):

			instance.product.count += 1
			instance.product.save()

			return super().delete(instance, validated_data)


		class Meta:
			model = ProductOrder
			fields = ['name', 'price', 'organization', 'product', 
			'order', 'service']



class TransactionSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()
	cashbox = CashboxSerializer()
	sale = SaleSerializer()
	purchase = PurchaseSerializer()

	class Meta:
		model = Transaction
		fields = ['id', 'cashbox','purchase', 'sale', 'organization']