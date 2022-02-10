from rest_framework import generics
from core.utils.customPerm import CustomPermissionVerificationRole, \
CustomPermissionGetUser, CustomPermissionCheckRelated
from .models import Order
from .serializers import OrderSerializer

from core.utils.customViewMethods import *



class OrderListAPIView(CustomFilterQueryset, generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	filterset_fields = ['service__id']



class OrderCreatorListAPIView(CustomFilterQueryset, generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	filterset_fields = ['service__id']



class OrderExecutorListAPIView(CustomFilterQueryset, generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = Order.objects.all()
	serializer_class = OrderSerializer
	filterset_fields = ['service__id']



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
	