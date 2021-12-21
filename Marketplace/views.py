import jwt
from bson.objectid import ObjectId

from django.contrib.auth import get_user_model

from rest_framework import status, permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
from restapi.customPerm import *



class MProductListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = MProduct.objects.all()
	serializer_class = MProductSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = {'id':self.kwargs.get('organization')})


class MProductCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = MProductSerializer.MProductCSerializer


class MProductRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionMarketplaceHelper]
	lookup_field = '_id'
	queryset = MProduct.objects.all()
	serializer_class = MProductSerializer


class MProductUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionMarketplaceHelper]
	lookup_field = '_id'
	queryset = MProduct.objects.all()
	serializer_class = MProductSerializer.MProductUSerializer




class MBusketListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = MBusket.objects.all()
	serializer_class = MBusketSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = {'id':self.kwargs.get('organization')})


class MBusketCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = MBusketSerializer.MBusketCSerializer


class MBusketRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionMarketplaceHelper]
	lookup_field = '_id'
	queryset = MBusket.objects.all()
	serializer_class = MBusketSerializer


class MBusketUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionMarketplaceHelper]
	lookup_field = '_id'
	queryset = MBusket.objects.all()
	serializer_class = MBusketSerializer.MBusketUSerializer




class MCourierListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = MCourier.objects.all()
	serializer_class = MCourierSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = {'id':self.kwargs.get('organization')})


class MCourierMOrderListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]



class MCourierCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = MCourierSerializer.MCourierCSerializer


class MCourierUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionMarketplaceHelper]
	lookup_field = '_id'
	queryset = MCourier.objects.all()
	serializer_class = MCourierSerializer.MCourierUSerializer




class MOrderListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = MOrder.objects.all()
	serializer_class = MOrderSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = {'id':self.kwargs.get('organization')})


class MOrderCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = MOrderSerializer.MOrderCSerializer


class MOrderRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionMarketplaceHelper]
	lookup_field = '_id'
	queryset = MOrder.objects.all()
	serializer_class = MOrderSerializer


class MOrderUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionMarketplaceHelper]
	lookup_field = '_id'
	queryset = MOrder.objects.all()
	serializer_class = MOrderSerializer.MOrderUSerializer