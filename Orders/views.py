from rest_framework import generics
from core.utils.customPerm import CustomPermissionVerificationRole, \
CustomPermissionGetUser, CustomPermissionCheckRelated
from .models import Order
from .serializers import OrderSerializer

from core.utils.customViewMethods import *



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


class OrderRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = Order.objects.all()
	serializer_class = OrderSerializer


class OrderUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	lookup_field = 'id'
	queryset = Order.objects.all()
	serializer_class = OrderSerializer.OrderUSerializer
	