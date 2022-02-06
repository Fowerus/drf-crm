from django.db import transaction
from rest_framework import status, permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import *

from Handbook.models import *
from core.utils.customPerm import *
from core.utils.customGet_object import *


class ProductCategoryListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer


class TransactionListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return self.queryset.select_related('organization').filter(organization=self.kwargs.get('organization'))


class ProductListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.queryset.select_related('organization').filter(organization=self.kwargs.get('organization'))


class ProductCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer.ProductCSerializer


class ProductRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    lookup_field = 'id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.queryset.select_related('organization').filter(organization=self.kwargs.get('organization'))


class ProductUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer.ProductUSerializer


class CashboxListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = Cashbox.objects.all()
    serializer_class = CashboxSerializer

    def get_queryset(self):
        return self.queryset.select_related('organization').filter(organization=self.kwargs.get('organization'))


class CashboxCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    queryset = Cashbox.objects.all()
    serializer_class = CashboxSerializer.CashboxCSerializer


class CashboxRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    lookup_field = 'id'
    queryset = Cashbox.objects.all()
    serializer_class = CashboxSerializer


class CashboxUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = Cashbox.objects.all()
    serializer_class = CashboxSerializer.CashboxUSerializer


class PurchaseRequestListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = PurchaseRequest.objects.all()
    serializer_class = PurchaseRequestSerializer

    def get_queryset(self):
        return self.queryset.select_related('organization').filter(organization=self.kwargs.get('organization'))


class PurchaseRequestCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    queryset = PurchaseRequest.objects.all()
    serializer_class = PurchaseRequestSerializer.PurchaseRequestCSerializer


class PurchaseRequestRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    lookup_field = 'id'
    queryset = PurchaseRequest.objects.all()
    serializer_class = PurchaseRequestSerializer


class PurchaseRequestDestroyAPIView(CustomGetObject, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    lookup_field = 'id'
    queryset = PurchaseRequest.objects.all()
    serializer_class = PurchaseRequestSerializer


class PurchaseAcceptListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = PurchaseAccept.objects.all()
    serializer_class = PurchaseAcceptSerializer

    def get_queryset(self):
        return self.queryset.select_related('organization').filter(organization=self.kwargs.get('organization'))


class PurchaseAcceptRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    lookup_field = 'id'
    queryset = PurchaseAccept.objects.all()
    serializer_class = PurchaseAcceptSerializer()


class PurchaseAcceptUpdateAPIView(CustomGetObject, generics.UpdateAPIView):
    permission_classes = [CustomPermissionVerificationRole,CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = PurchaseAccept.objects.all()
    serializer_class = PurchaseAcceptSerializer.PurchaseAcceptUSerializer


class SaleProductListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer

    def get_queryset(self):
        return self.queryset.filter(organization=self.kwargs.get('organization'))


class SaleProductCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer.SaleProductCSerializer


class SaleProductRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    lookup_field = 'id'
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer


class SaleProductUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer.SaleProductUSerializer


class SaleOrderListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer

    def get_queryset(self):
        return self.queryset.filter(organization=self.kwargs.get('organization'))


class SaleOrderCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer.SaleOrderCSerializer


class SaleOrderRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    lookup_field = 'id'
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer


class SaleOrderUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer.SaleOrderUSerializer


class WorkDoneListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = WorkDone.objects.all()
    serializer_class = WorkDoneSerializer

    def get_queryset(self):
        return self.queryset.filter(organization=self.kwargs.get('organization'))


class WorkDoneCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    queryset = WorkDone.objects.all()
    serializer_class = WorkDoneSerializer.WorkDoneCSerializer


class WorkDoneRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    lookup_field = 'id'
    queryset = WorkDone.objects.all()
    serializer_class = WorkDoneSerializer


class WorkDoneUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = WorkDone.objects.all()
    serializer_class = WorkDoneSerializer.WorkDoneUSerializer

    @transaction.atomic
    def delete(self, requests, **kwargs):
        instance = self.get_object()
        create_orderHistory(order=instance.order, model='1', organization=instance.order.organization, method='delete',
                            body={"id": instance.id, "name": instance.name})
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductOrderListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer

    def get_queryset(self):
        return self.queryset.filter(organization=self.kwargs.get('organization'))


class ProductOrderCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer.ProductOrderCSerializer


class ProductOrderRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    lookup_field = 'id'
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer


class ProductOrderUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer.ProductOrderUSerializer

    @transaction.atomic
    def delete(self, requests, **kwargs):
        instance = self.get_object()
        create_orderHistory(order=instance.order, model='0',
                            organization=instance.order.organization, method='delete')
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
