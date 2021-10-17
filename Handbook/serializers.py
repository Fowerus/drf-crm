from rest_framework import serializers

from .models import *
from crm.atomic_exception import MyCustomError
from Organizations.serializers import OrganizationSerializer
from Orders.serializers import OrderSerializer



class DeviceTypeSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class Meta:
		model = DeviceType
		fields = ['id','name','organization','description', 'created_at', 'updated_at']


	class DeviceTypeCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			device_type = DeviceType.objects.create(**validated_data)

			return device_type


		class Meta:
			model = DeviceType
			fields = ['name','description', 'organization']


	class DeviceTypeUSerializer(serializers.ModelSerializer):

		class Meta:
			model = DeviceType
			fields = ['name','description']



class DeviceMakerSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class Meta:
		model = DeviceMaker
		fields = ['id','name','organization', 'created_at', 'updated_at']


	class DeviceMakerCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			device_maker = DeviceMaker.objects.create(**validated_data)

			return device_maker


		class Meta:
			model = DeviceMaker
			fields = ['name', 'organization']


	class DeviceMakerUSerializer(serializers.ModelSerializer):

		class Meta:
			model = DeviceMaker
			fields = ['name']



class DeviceModelSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class Meta:
		model = DeviceModel
		fields = ['id','name','organization', 'created_at', 'updated_at']


	class DeviceModelCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			device_model = DeviceMaker.objects.create(**validated_data)

			return device_model


		class Meta:
			model = DeviceModel
			fields = ['name', 'organization']


	class DeviceModelUSerializer(serializers.ModelSerializer):

		class Meta:
			model = DeviceModel
			fields = ['name']



class DeviceKitSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()
	device_type = DeviceTypeSerializer()

	class Meta:
		model = DeviceKit
		fields = ['id','name','organization', 'device_type', 'created_at', 'updated_at']


	class DeviceKitCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			device_kit = DeviceKit.objects.create(**validated_data)

			return device_kit


		class Meta:
			model = DeviceKit
			fields = ['name', 'organization', 'device_type']


	class DeviceKitUSerializer(serializers.ModelSerializer):

		class Meta:
			model = DeviceKit
			fields = ['name', 'device_type']



class DeviceAppearanceSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class Meta:
		model = DeviceAppearance
		fields = ['id','name','organization', 'created_at', 'updated_at']


	class DeviceAppearanceCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			device_appearance = DeviceAppearance.objects.create(**validated_data)

			return device_appearance


		class Meta:
			model = DeviceAppearance
			fields = ['name', 'organization']


	class DeviceAppearanceUSerializer(serializers.ModelSerializer):

		class Meta:
			model = DeviceAppearance
			fields = ['name']



class DeviceDefectSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class Meta:
		model = DeviceDefect
		fields = ['id','name','organization', 'created_at', 'updated_at']


	class DeviceDefectCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			device_defect = DeviceDefect.objects.create(**validated_data)

			return device_defect


		class Meta:
			model = DeviceDefect
			fields = ['name', 'organization']


	class DeviceDefectUSerializer(serializers.ModelSerializer):

		class Meta:
			model = DeviceDefect
			fields = ['name']



class ServicePriceSerializer(serializers.ModelSerializer):
	organization = OrganizationSerializer()

	class Meta:
		model = ServicePrice
		fields = ['id','name','organization','price', 'created_at', 'updated_at']


	class ServicePriceCSerializer(serializers.ModelSerializer):

		def create(self, validated_data):
			service_price = ServicePrice.objects.create(**validated_data)

			return service_price


		class Meta:
			model = ServicePrice
			fields = ['name', 'organization', 'price']


	class ServicePriceUSerializer(serializers.ModelSerializer):

		class Meta:
			model = ServicePrice
			fields = ['name', 'price']



class ActionHistorySerializer(serializers.ModelSerializer):
	class Meta:
		model = ActionHistory
		fields = ['id', 'method', 'process', 'model', 'updated_at', 'created_at']



class OrderHistorySerializer(serializers.ModelSerializer):
	order = OrderSerializer()
	organization = OrganizationSerializer()
	action_history = ActionHistorySerializer()

	class OrderHistoryCSerializerer(serializers.ModelSerializer):
		model = serializers.CharField(max_length = 150, read_only = True)
		method = serializers.CharField(max_length = 150, read_only = True)
		
		def create(self, validated_data):
			order_history_data = {
				'organization':validated_data['organization'],
				'action_history':ActionHistory.objects.filter(organization = validated_data['organization'].id).filter(
					model = validated_data['model']).get(method = validated_data['method']),
			}
			order_history = OrderHistory.objects.create(**order_history_data)

			return order_history

		class Meta:
			model = OrderHistory
			fields = ['organization', 'model', 'method']


	class OrderHistoryUSerializer(serializers.ModelSerializer):

		def update(self, instance, validated_data):
			if instance.order.order_status.is_comment_required and 'comment' not in validated_data:
				raise MyCustomError('Comment is required', 400)
			elif instance.order.order_status.is_payment_required:
				raise MyCustomError('Payment is required', 400)

			return super().update(self, instance, validated_data) 

		class Meta:
			model = OrderHistory
			fields = ['comment', 'body']


	class Meta:
		model = OrderHistory
		fields = ['id', 'order', 'comment', 'action_history', 'body', 'organization']