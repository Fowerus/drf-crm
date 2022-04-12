from django.db import transaction
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from .serializers import *

from Handbook.models import *
from core.utils.customPerm import *
from core.utils.customViewMethods import *


class ProductCategoryListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    perm_view_name = 'product'


class TransactionListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    filterset_fields = ['service__id']


class ProductListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['service__id']


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


class ProductUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer.ProductUSerializer


class CashboxListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = Cashbox.objects.all()
    serializer_class = CashboxSerializer
    filterset_fields = ['service__id']


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


class PurchaseRequestListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = PurchaseRequest.objects.all()
    serializer_class = PurchaseRequestSerializer
    filterset_fields = ['service__id']


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


class PurchaseAcceptListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = PurchaseAccept.objects.all()
    serializer_class = PurchaseAcceptSerializer
    filterset_fields = ['service__id']


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


class SaleProductListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = SaleProduct.objects.all()
    serializer_class = SaleProductSerializer
    filterset_fields = ['service__id']


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


class SaleOrderListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer
    filterset_fields = ['service__id']


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


class WorkDoneListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = WorkDone.objects.all()
    serializer_class = WorkDoneSerializer
    filterset_fields = ['service__id']


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
    def delete(self, request, **kwargs):
        instance = self.get_object()
        create_orderHistory(order=instance.order, model='1', organization=instance.order.organization, method='delete',
                            body={"id": instance.id, "name": instance.name})
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductOrderListAPIView(CustomFilterQueryset,generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
    filterset_fields = ['service__id']


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
    def delete(self, request, **kwargs):
        instance = self.get_object()
        create_orderHistory(order=instance.order, model='0',
                            organization=instance.order.organization, method='delete')
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
