from rest_framework import serializers


from Users.serializers import UserSerializer
from Organizations.serializers import ServiceSerializer
from Orders.models import Order



class OrderSerializer(serializers.ModelSerializer):
	creator = UserSerializer()
	executor = UserSerializer()
	service = ServiceSerializer()

	class Meta:
		model = Order
		fields = ['id', 'order_code', 'description', 'creator', 'executor', 'client', 'done', 'service', 'created_at', 'updated_at']


	class OrderCSerializer(serializers.ModelSerializer):
		order_code = serializers.IntegerField(read_only = True)

		def create(self, validated_data):
			validated_data['order_code'] = int(str(uuid.uuid1().int)[:20])
			order = Order.objects.create(**validated_data)

			return order

		class Meta:
			model = Order
			fields = ['description', 'creator', 'executor', 'client', 'service']


	class OrderUSerializer(serializers.ModelSerializer):

		class Meta:
			model = Order
			fields = ['description', 'executor', 'service']