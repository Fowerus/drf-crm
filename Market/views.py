from rest_framework import status, permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import *

from Handbook.models import *
from crm.customPerm import *



class ProductCategoryListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = ProductCategory.objects.all()
	serializer_class = ProductCategorySerializer




class ProductListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class ProductCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	queryset = Product.objects.all()
	serializer_class = ProductSerializer.ProductCSerializer


class ProductRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class ProductUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionCheckRelated]
	lookup_field = 'id'
	queryset = Product.objects.all()
	serializer_class = ProductSerializer.ProductUSerializer




class CashboxListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = Cashbox.objects.all()
	serializer_class = CashboxSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class CashboxCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	queryset = Cashbox.objects.all()
	serializer_class = CashboxSerializer.CashboxCSerializer


class CashboxRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = Cashbox.objects.all()
	serializer_class = CashboxSerializer


class CashboxUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionCheckRelated]
	lookup_field = 'id'
	queryset = Cashbox.objects.all()
	serializer_class = CashboxSerializer.CashboxUSerializer




class PurchaseListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = Purchase.objects.all()
	serializer_class = PurchaseSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class PurchaseCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	queryset = Purchase.objects.all()
	serializer_class = PurchaseSerializer.PurchaseCSerializer


class PurchaseRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = Purchase.objects.all()
	serializer_class = PurchaseSerializer


class PurchaseUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionCheckRelated],
	lookup_field = 'id'
	queryset = Purchase.objects.all()
	serializer_class = PurchaseSerializer.PurchaseUSerializer