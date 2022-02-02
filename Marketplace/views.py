import jwt
from bson.objectid import ObjectId

from django.contrib.auth import get_user_model

from rest_framework import status, permissions,  filters
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from core.utils.customPerm import *


class MProductListAPIView(generics.ListAPIView):
    queryset = MProduct.objects.all()
    serializer_class = MProductSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    # def get_queryset(self):
    #     return self.queryset.filter(organization={'id': self.kwargs.get('organization')})


class MProductCreateAPIView(generics.CreateAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    serializer_class = MProductSerializer.MProductCSerializer


class MProductFileCreateAPIView(generics.CreateAPIView):
    permission_classes = [CustomPermissionMProviderAccess]
    serializer_class = MProductSerializer.MProductCFileSerializer
    perm_view_name = 'MProduct'


class MProductRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [CustomPermissionMarketplaceHelper]
    lookup_field = '_id'
    queryset = MProduct.objects.all()
    serializer_class = MProductSerializer


class MProductUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionVerificationAffiliation, CustomPermissionMarketplaceHelper]
    lookup_field = '_id'
    queryset = MProduct.objects.all()
    serializer_class = MProductSerializer.MProductUSerializer


class MBusketListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = MBusket.objects.all()
    serializer_class = MBusketSerializer

    def get_queryset(self):
        return self.queryset.filter(organization={'id': self.kwargs.get('organization')})


class MBusketMCourierListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionVerificationAffiliation, CustomPermissionMarketplaceHelper]
    queryset = MBusket.objects.all()
    serializer_class = MCourierSerializer

    def get(self, requests, *args, **kwargs):
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
    permission_classes = [CustomPermissionVerificationRole]
    serializer_class = MBusketSerializer.MBusketCSerializer


class MBusketRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionMarketplaceHelper]
    lookup_field = '_id'
    queryset = MBusket.objects.all()
    serializer_class = MBusketSerializer


class MBusketUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionVerificationAffiliation, CustomPermissionMarketplaceHelper]
    lookup_field = '_id'
    queryset = MBusket.objects.all()
    serializer_class = MBusketSerializer.MBusketUSerializer


class MCourierListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = MCourier.objects.all()
    serializer_class = MCourierSerializer

    def get_queryset(self):
        return self.queryset.filter(organization={'id': self.kwargs.get('organization')})


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
    permission_classes = [CustomPermissionVerificationRole]
    serializer_class = MCourierSerializer.MCourierCSerializer


class MCourierUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionVerificationAffiliation, CustomPermissionMarketplaceHelper]
    lookup_field = '_id'
    queryset = MCourier.objects.all()
    serializer_class = MCourierSerializer.MCourierUSerializer


class MOrderListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = MOrder.objects.all()
    serializer_class = MOrderSerializer

    def get_queryset(self):
        return self.queryset.filter(organization={'id': self.kwargs.get('organization')})


class MOrderForProviderListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionMarketplaceHelper]
    queryset = MOrder.objects.all()
    serializer_class = MOrderSerializer.MOrderForProviderSerializer
    perm_view_name = 'MOrder'

    def get_queryset(self):

        return MOrder.objects.mongo_aggregate([{"$set": {"price": "$$REMOVE", "products": {"$filter": {"input": "$products", "cond": {"$eq": ["$$this.organization.id", self.kwargs.get('organization')]
                                                                                                                                      }}}}}])


class MOrderMCourierListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionVerificationAffiliation, CustomPermissionMarketplaceHelper]
    queryset = MOrder.objects.all()
    serializer_class = MCourierSerializer

    def get(self, requests, *args, **kwargs):
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
    permission_classes = [
        CustomPermissionVerificationAffiliation, CustomPermissionMarketplaceHelper]
    lookup_field = '_id'
    queryset = MOrder.objects.all()
    serializer_class = MOrderSerializer.MOrderUForCourierSerializer


class MOrderUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionVerificationAffiliation, CustomPermissionMarketplaceHelper]
    lookup_field = '_id'
    queryset = MOrder.objects.all()
    serializer_class = MOrderSerializer.MOrderUSerializer
