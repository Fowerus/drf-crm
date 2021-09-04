from rest_framework import generics
from crm.customPerm import CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation
from .models import Order
from .serializers import OrderSerializer



class OrderListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class OrderCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = OrderSerializer.OrderCSerializer


class OrderRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


class OrderUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = Order.objects.all()
	serializer_class = OrderSerializer.OrderUSerializer