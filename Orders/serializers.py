import uuid
from rest_framework import serializers


from Users.serializers import UserSerializer
from Organizations.serializers import ServiceSerializer, OrganizationSerializer
from .models import Order



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
			validated_data['order_code'] = int(str(uuid.uuid1().int)[:15])
			order = Order.objects.create(**validated_data)

			return order

		class Meta:
			model = Order
			fields = ['description', 
		'creator', 'executor', 'organization', 'client', 
		'done', 'service', 'order_status',
		'device_type', 'device_maker', 'device_model', 'device_kit', 'device_appearance',
		'device_defect']


	class OrderUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Order
			fields = ['description', 'executor', 'order_status',
		'device_type', 'device_maker', 'device_model', 'device_kit', 'device_appearance',
		'device_defect']
			