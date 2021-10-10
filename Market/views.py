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




class SaleListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class SaleCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer.SaleCSerializer


class SaleRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer


class SaleUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionCheckRelated],
	lookup_field = 'id'
	queryset = Sale.objects.all()
	serializer_class = SaleSerializer.SaleUSerializer




class WorkDoneListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = WorkDone.objects.all()
	serializer_class = WorkDoneSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class WorkDoneCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	queryset = WorkDone.objects.all()
	serializer_class = WorkDoneSerializer.WorkDoneCSerializer


class WorkDoneRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = WorkDone.objects.all()
	serializer_class = WorkDoneSerializer


class WorkDoneUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionCheckRelated],
	lookup_field = 'id'
	queryset = WorkDone.objects.all()
	serializer_class = WorkDoneSerializer.WorkDoneUSerializer




class ProductOrderListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = ProductOrder.objects.all()
	serializer_class = ProductOrderSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class ProductOrderCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	queryset = ProductOrder.objects.all()
	serializer_class = ProductOrderSerializer.ProductOrderCSerializer


class ProductOrderRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = ProductOrder.objects.all()
	serializer_class = ProductOrderSerializer


class ProductOrderUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionCheckRelated],
	lookup_field = 'id'
	queryset = ProductOrder.objects.all()
	serializer_class = ProductOrderSerializer.ProductOrderUDSerializer