from rest_framework import generics
from core.utils.customPerm import CustomPermissionVerificationRole, \
CustomPermissionVerificationAffiliation, CustomPermissionGetUser, CustomPermissionCheckRelated
from .models import Order
from .serializers import OrderSerializer



class OrderListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))



class OrderCreatorListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionGetUser, CustomPermissionVerificationRole]
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization')).filter(creator = self.kwargs.get('id'))



class OrderExecutorListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionGetUser, CustomPermissionVerificationRole]
	queryset = Order.objects.all()
	serializer_class = OrderSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization')).filter(creator = self.kwargs.get('id'))



class OrderCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	serializer_class = OrderSerializer.OrderCSerializer


class OrderRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


class OrderUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionCheckRelated]
	lookup_field = 'id'
	queryset = Order.objects.all()
	serializer_class = OrderSerializer.OrderUSerializer
	