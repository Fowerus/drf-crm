import jwt
from bson.objectid import ObjectId

from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, permissions,  filters
from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializers import *
from core.utils.customPerm import *
from core.utils.customViewMethods import *


class MProductListAPIView(generics.ListAPIView):
    queryset = MProduct.objects.all()
    serializer_class = MProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']


class MProductCreateAPIView(generics.CreateAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    serializer_class = MProductSerializer.MProductCSerializer


class MProductFileCreateAPIView(generics.CreateAPIView):
    permission_classes = [CustomPermissionMProviderAccess]
    serializer_class = MProductSerializer.MProductCFileSerializer
    perm_view_name = 'MProduct'


class MProductRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = '_id'
    queryset = MProduct.objects.all()
    serializer_class = MProductSerializer


class MProductUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionMarketplaceHelper, 
        CustomPermissionCheckRelated]
    lookup_field = '_id'
    queryset = MProduct.objects.all()
    serializer_class = MProductSerializer.MProductUSerializer


class MBusketListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = MBusket.objects.all()
    serializer_class = MBusketSerializer


class MBusketMCourierListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole,CustomPermissionMarketplaceHelper]
    queryset = MBusket.objects.all()
    serializer_class = MCourierSerializer
    perm_view_name = 'mbusket'

    def get(self, request, *args, **kwargs):
        try:
            instance = self.queryset.get(_id=self.kwargs.get('_id'))
            self.queryset = MCourier.objects.all()
            data = list()
            for item in list(set(instance.providers + [self.kwargs.get('organization')])):
                data += self.serializer_class(self.queryset.filter(
                    organization={"id": item}), many=True).data

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': "Serializer data error or does not exist"}, status=status.HTTP_400_BAD_REQUEST)


class MBusketCreateAPIView(generics.CreateAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelatedMarketplace]
    serializer_class = MBusketSerializer.MBusketCSerializer


class MBusketRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionMarketplaceHelper]
    lookup_field = '_id'
    queryset = MBusket.objects.all()
    serializer_class = MBusketSerializer


class MBusketUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole,CustomPermissionMarketplaceHelper,
        CustomPermissionCheckRelatedMarketplace]
    lookup_field = '_id'
    queryset = MBusket.objects.all()
    serializer_class = MBusketSerializer.MBusketUSerializer


class MCourierListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = MCourier.objects.all()
    serializer_class = MCourierSerializer


class MCourierMOrderListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionGetUser]
    queryset = MOrder.objects.all()
    serializer_class = MOrderSerializer

    def get_queryset(self):
        try:
            member = Organization.objects.get(id=self.kwargs.get(
                'organization')).organization_members.all().get(user__id=self.kwargs.get('id'))
            mcourier = MCourier.objects.filter(courier={"id": member.id}).get(
                organization={'id': self.kwargs.get('organization')})

            return self.queryset.filter(courier={'_id': str(mcourier._id)})

        except Exception as e:
            pass

        return {}


class MCourierCreateAPIView(generics.CreateAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelatedMarketplace]
    serializer_class = MCourierSerializer.MCourierCSerializer


class MCourierUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole,CustomPermissionCheckRelatedMarketplace, 
        CustomPermissionMarketplaceHelper]
    lookup_field = '_id'
    queryset = MCourier.objects.all()
    serializer_class = MCourierSerializer.MCourierUSerializer


class MOrderListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = MOrder.objects.all()
    serializer_class = MOrderSerializer


class MOrderForProviderListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionMarketplaceHelper]
    queryset = MOrder.objects.all()
    serializer_class = MOrderSerializer.MOrderForProviderSerializer
    perm_view_name = 'MOrder'

    def get_queryset(self):

        return MOrder.objects.mongo_aggregate([{"$set": {"price": "$$REMOVE", 
            "products": {"$filter": {"input": "$products", 
            "cond": {"$eq": ["$$this.organization.id", self.user.current_org]}}}}}])


class MOrderMCourierListAPIView(CustomGetObject, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionMarketplaceHelper]
    queryset = MOrder.objects.all()
    serializer_class = MCourierSerializer
    perm_view_name = 'morder'

    def get(self, request, *args, **kwargs):
        try:
            instance = self.queryset.get(_id=self.kwargs.get('_id'))
            self.queryset = MCourier.objects.all()
            data = list()
            for item in list(set(instance.providers + [self.kwargs.get('organization')])):
                data += self.serializer_class(self.queryset.filter(
                    organization={"id": item}), many=True).data

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': "Serializer data error or does not exist"}, status=status.HTTP_400_BAD_REQUEST)


class MOrderCreateAPIView(generics.CreateAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    serializer_class = MOrderSerializer.MOrderCSerializer


class MOrderRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionMarketplaceHelper]
    lookup_field = '_id'
    queryset = MOrder.objects.all()
    serializer_class = MOrderSerializer


class MOrderForCourierUpdateAPIView(generics.UpdateAPIView):
    permissions = [CustomPermissionMarketplaceHelper]
    lookup_field = '_id'
    queryset = MOrder.objects.all()
    serializer_class = MOrderSerializer.MOrderUForCourierSerializer


class MOrderUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole,CustomPermissionMarketplaceHelper]
    lookup_field = '_id'
    queryset = MOrder.objects.all()
    serializer_class = MOrderSerializer.MOrderUSerializer