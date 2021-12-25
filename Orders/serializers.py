import uuid
from rest_framework import serializers
from django.db import transaction


from Users.serializers import UserSerializer
from Organizations.serializers import ServiceSerializer, OrganizationSerializer
from .models import Order, OrderStatus



class OrderSerializer(serializers.ModelSerializer):
	creator = UserSerializer()
	executor = UserSerializer()
	service = ServiceSerializer()
	organization = OrganizationSerializer()

	class Meta:
		model = Order
		fields = ['id', 'order_code', 'description', 
		'creator', 'executor', 'organization', 'client', 
		'done', 'service', 'order_status', 'created_at', 'updated_at',
		'device_type', 'device_maker', 'device_model', 'device_kit', 'device_appearance',
		'device_defect']


	class OrderCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			order = Order.objects.create(**validated_data)
			order.calculate_order_code
			order.order_status = Organization.objects.organization_order_status.all().get(is_default = True)
			order.save()

			create_orderHistory(order = instance.order, model = '3', organization = instance.organization, method = 'create')

			return order

		class Meta:
			model = Order
			fields = ['description', 
		'creator', 'executor', 'organization', 'client', 
		'done', 'service',
		'device_type', 'device_maker', 'device_model', 'device_kit', 'device_appearance',
		'device_defect']


	class OrderUSerializer(serializers.ModelSerializer):

		@transaction.atomic
		def update(self, instance, validated_data):
			if 'order_status' in validated_data:
				order.order_status = validated_data['order_status']
				order.save()
				create_orderHistory(order = instance.order, model = '3', organization = instance.organization, method = 'create', body = instance.order.order_status)

				validated_data.pop('order_status')

			return super().update(instance, validated_data)


		class Meta:
			model = Order
			fields = ['description', 'executor', 'order_status',
		'device_type', 'device_maker', 'device_model', 'device_kit', 'device_appearance',
		'device_defect']




class OrderStatusSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class OrderStatusCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			order_status = OrderStatus.objects.create(**validated_data)

			return order_status

		class Meta:
			model = OrderStatus
			fields = ['name', 'color', 'description', 'type', 'organization', 'is_default']


	class OrderStatusUSerializer(serializers.ModelSerializer):

		class Meta:
			model = OrderStatus
			fields = ['name', 'color', 'description', 'type', 'is_default']


	class Meta:
		model = OrderStatus
		fields = ['id', 'name', 'color', 'description', 'type', 'organization', 'is_default',
		'is_payment_required', 'is_payment_comment', 'updated_at', 'created_at']
			