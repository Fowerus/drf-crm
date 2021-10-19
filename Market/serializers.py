import uuid

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
from crm.views import get_viewName, create_orderHistory



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
		fields = ['cashbox','purchase', 'sale_product', 'sale_order', 'organization']



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
			validated_data['code'] = str(uuid.uuid1().int)[:15]
			validated_data['barcode'] = str(uuid.uuid1().int)[:15]
			product = Product.objects.create(**validated_data)

			return product

		class Meta:
			model = Product
			fields = ['name', 'purchase_price', 'sale_price', 'count',
			'supplier', 'irreducible_balance', 'organization', 'service', 'category']


	class ProductUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Product
			fields = ['name', 'purchase_price', 'sale_price', 'count',
			'supplier', 'irreducible_balance', 'service', 'category']




class PurchaseRequestSerializer(serializers.ModelSerializer):
	cashbox = CashboxSerializer()
	service = ServiceSerializer()
	organization = OrganizationSerializer()
	product = ProductSerializer()


	class Meta:
		model = PurchaseRequest
		fields = ['id', 'price', 'organization', 'cashbox', 'service', 'is_deferred','product', 'count', 'created_at', 'updated_at']

	class PurchaseRequestCSerializer(serializers.ModelSerializer):
		is_cash = serializers.BooleanField(default = False)

		@transaction.atomic
		def create(self, validated_data):

			if validated_data['product'].organization.id == validated_data['organization'].id:
				raise MyCustomError('You cannot purchase your organization product', 400)

			is_cash = validated_data.pop('is_cash')
			purchase_request = PurchaseRequest.objects.create(**validated_data)

			if is_cash:
				purchase_request.cashbox.cash -= validated_data['count']*purchase_request.price
			else:
				purchase_request.cashbox.account_money -= validated_data['count']*purchase_request.price

			if purchase_request.cashbox.calculate_min_money < 0:
				raise MyCustomError('Insufficient money at the cashbox', 400)


			purchase_accept = PurchaseAccpet.objects.create(purchase_request = purchase_request, is_cash = validated_data['is_cash'],
				organization = validated_data['product'].organization)

			return purchase_request

		class Meta:
			model = PurchaseRequest
			fields = ['price', 'organization', 'cashbox', 'service', 'product', 'count', 'is_deferred', 'is_cash']
			



class PurchaseAcceptSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()
	purchase_request = PurchaseRequestSerializer()


	class PurchaseAcceptUSerializer(serializers.ModelSerializer):

		@transaction.atomic
		def update(self, instance, validated_data):

			if not instance.accept:

				instance.purchase_request.product.count -= instance.count

				if instance.purchase_request.product.count < 0:
					raise MyCustomError('The quantity of product is not enough', 400)

				if is_cash:
					instance.purchase_request.cashbox.cash -= instance.purchase_request.count*instance.purchase_request.price
				else:
					instance.purchase_request.cashbox.account_money -= instance.purchase_request.count*instance.purchase_request.price

				if instance.purchase_request.cashbox.calculate_min_money < 0:
					instance.purchase_request.delete()
					raise MyCustomError('Insufficient money at the buyer cashbox. The proposal deleted', 400)



				product_data = {
					"name":instance.purchase_request.product.name,
					"purchase_price":instance.purchase_request.product.purchase_price,
					"sale_price": instance.purchase_request.product.sale_price,
					"count":instance.purchase_request.count,
					"supplier":instance.purchase_request.product.organization.name,
					"irreducible_balance":instance.purchase_request.product.irreducible_balance,
					"organization": instance.purchase_request.organization,
					"category": instance.purchase_request.product.category,
					"service":instance.purchase_request.service
				}
				product = ProductSerializer(data = product_data)

				if product.is_valid() != True:
					raise MyCustomError('There is error on the server', 500)

				instance.accept = True
				product.save()
				instance.save()

				transaction_data = {
					"cashbox":instance.purchase_request.cashbox.id,
					"purchase":instance.purchase_request.id,
					"organization":instance.purchase_request.organization.id
				}

				transaction = TransactionCSerializer(data = transaction_data)
				if transaction.is_valid() != True:
					raise MyCustomError('There is some error on the server', 500)
					
				transaction.save()

			return instance


		class Meta:
			model = PurchaseAccept
			fields = ['is_cash', 'accept']


	class Meta:
		model = PurchaseAccept
		fields = ['id', 'purchase_request', 'organization', 'is_cash', 'accept', 'updated_at', 'created_at']




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
			create_orderHistory(order = validated_data['order'], model = 'WorkDone', organization = validated_data['organization'], method = 'create')

			return work_done

		class Meta:
			model = WorkDone
			fields = ['name', 'price', 'organization', 'service_price', 
			'user', 'order', 'service']

	class WorkDoneUSerializer(serializers.ModelSerializer):

		def delete(self, instance, validated_data):
			create_orderHistory(order = instance.order, model = 'WorkDone', organization = validated_data['organization'], method = 'delete')
			return super().delete(instance, validated_data)

		class Meta:
			model = WorkDone
			fields = ['name', 'price', 'service_price', 'service']
			



class ProductOrderSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()
	product = ProductSerializer(many = True)
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
			product_order.calculate_price

			for item in validated_data['product']:
				if item.count < 1:
					raise MyCustomError(f"The quantity of product with id: {item.id} is not enough", 400)
				item.count -= 1
				item.save()

			product_order.product.set(set(validated_data['product']))
			product_order.save()
			create_orderHistory(order = validated_data['order'], model = 'ProductOrder', organization = validated_data['organization'], method = 'create')

			return product_order


		class Meta:
			model = ProductOrder
			fields = ['name', 'organization', 'product', 
			'order', 'service']

	class ProductOrderUDSerializer(serializers.ModelSerializer):

		@transaction.atomic
		def update(self, instance, validated_data):
			if 'product' in validated_data:
				old_product = set(instance.product.all())
				instance.permissions.set(set(validated_data['product']))
				add_remove_product = set(instance.product.all())
				new_product = old_product ^ add_remove_product
				instance.product.set(new_product)
				validated_data.pop('product')

				instance.save()

			return super().update(instance, validated_data)



		@transaction.atomic
		def delete(self, instance, validated_data):

			for item in instance.product.all():
				item.count += 1
				item.save()

			create_orderHistory(order = instance.order, model = 'ProductOrder', organization = validated_data['organization'], method = 'delete')
			return super().delete(instance, validated_data)


		class Meta:
			model = ProductOrder
			fields = ['name', 'price', 'product', 'service']




class SaleProductSerializer(serializers.ModelSerializer):
	cashbox = CashboxSerializer()
	service = ServiceSerializer()
	organization = OrganizationSerializer()
	client = ClientSerializer()
	product = ProductSerializer()


	class Meta:
		model = SaleProduct
		fields = ['id', 'cash', 'card', 'bank_transfer', 'discount', 'client', 
		'organization', 'cashbox', 'product', 'service', 'created_at', 'updated_at']

	class SaleProductCSerializer(serializers.ModelSerializer):

		@transaction.atomic
		def create(self, validated_data):
			sale_product = SaleProduct.objects.create(**validated_data)
			sale_product.cashbox.cash += sale_product.cash*(1 + sale_product.discount)
			sale_product.cashbox.account_money += (sale_product.card + sale_product.bank_transfer)*(1 + sale_product.discount)

			if sale_product.product.count < 1:
				raise MyCustomError("The quantity of product is not enough", 400)

			sale_product.product.count =- 1
			sale_product.product.save()
			sale_product.cashbox.save()
			sale_product.save()

			transaction_data = {
				"cashbox":validated_data['cashbox'].id,
				"sale_product":sale_product.id,
				"organization":validated_data['organization'].id
			}

			transaction = TransactionCSerializer(data = transaction_data)
			if transaction.is_valid() != True:
				raise MyCustomError('There is some error on the sever', 500)

			transaction.save()

			return sale_product

		class Meta:
			model = SaleProduct
			fields = ['cash', 'card', 'bank_transfer', 'discount', 'client', 
		'organization', 'cashbox', 'product', 'service']


	class SaleProductUSerializer(serializers.ModelSerializer):

		class Meta:
			model = SaleProduct
			fields = ['cash', 'card', 'bank_transfer', 'discount', 'client', 
			'cashbox', 'service']




class SaleOrderSerializer(serializers.ModelSerializer):
	cashbox = CashboxSerializer()
	service = ServiceSerializer()
	organization = OrganizationSerializer()
	client = ClientSerializer()
	product_order = ProductOrderSerializer()


	class Meta:
		model = SaleOrder
		fields = ['id', 'cash', 'card', 'bank_transfer', 'discount', 'client', 
		'organization', 'cashbox', 'product_order', 'service', 'created_at', 'updated_at']

	class SaleOrderCSerializer(serializers.ModelSerializer):

		@transaction.atomic
		def create(self, validated_data):
			sale_order = SaleOrder.objects.create(**validated_data)
			sale_order.cashbox.cash += sale_order.cash*(1 + sale_order.discount)
			sale_order.cashbox.account_money += (sale_order.card + sale_order.bank_transfer)*(1 + sale_order.discount)

			sale_order.cashbox.save()
			sale_order.save()

			transaction_data = {
				"cashbox":validated_data['cashbox'].id,
				"sale_order":sale_order.id,
				"organization":validated_data['organization'].id
			}

			transaction = TransactionCSerializer(data = transaction_data)
			if transaction.is_valid() != True:
				raise MyCustomError('There is some error on the sever', 500)

			transaction.save()
			create_orderHistory(order = validated_data['product_order'].order, model = 'SaleOrder', organization = validated_data['organization'], method = 'create')

			return sale_order

		class Meta:
			model = SaleOrder
			fields = ['cash', 'card', 'bank_transfer', 'discount', 'client', 
		'organization', 'cashbox', 'product_order', 'service']


	class SaleOrderUSerializer(serializers.ModelSerializer):

		class Meta:
			model = SaleOrder
			fields = ['cash', 'card', 'bank_transfer', 'discount', 'client', 
			'cashbox', 'service']



class TransactionSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()
	cashbox = CashboxSerializer()
	sale_product = SaleProductSerializer()
	sale_order = SaleOrderSerializer()
	purchase = PurchaseRequestSerializer()


	class Meta:
		model = Transaction
		fields = ['id', 'cashbox','purchase', 'sale_product', 'sale_order', 'organization']