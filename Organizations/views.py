import jwt

from django.contrib.auth import get_user_model

from rest_framework import status, permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import *

from Users.serializers import UserSerializer

from Organizations.models import *
from core.utils.customPerm import *
from core.utils.customGet_object import *


class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [CustomPermissionVerificationOrganization]
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def post(self, requests):
        self.serializer_class = OrganizationSerializer.OrganizationCSerializer
        return super().post(requests)


class OrganizationCreatorListAPIView(generics.ListAPIView):
    permission_classes = [
        CustomPermissionVerificationOrganization, CustomPermissionGetUser]
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get_queryset(self):
        return self.queryset.select_related('creator').filter(creator__id=self.kwargs.get('id'))


class OrganizationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermissionVerificationOrganization]
    lookup_field = 'id'
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def patch(self, requests, **kwargs):
        self.serializer_class = OrganizationSerializer.OrganizationUSerializer
        return super().patch(requests, kwargs)

    def put(self, requests, **kwargs):
        self.serializer_class = OrganizationSerializer.OrganizationUSerializer
        return super().put(requests, kwargs)


class Organization_memberListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionCheckSession]
    queryset = Organization_member.objects.all()
    serializer_class = Organization_memberSerializer

    def get_queryset(self):
        return self.queryset.select_related('organization').filter(organization=self.kwargs.get('organization'))


class Organization_memberCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    serializer_class = Organization_memberSerializer.Organization_memberCSerializer


class Organization_memberRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [CustomPermissionCheckSession]
    queryset = Organization_member.objects.all()
    lookup_field = 'id'
    serializer_class = Organization_memberSerializer


class Organization_memberUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = Organization_member.objects.all()
    serializer_class = Organization_memberSerializer.Organization_memberUSerializer


class ServiceListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionCheckSession]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_queryset(self):
        return self.queryset.select_related('organization').filter(organization=self.kwargs.get('organization'))


class ServiceCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    serializer_class = ServiceSerializer.ServiceCSerializer


class ServiceRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [CustomPermissionCheckSession]
    lookup_field = 'id'
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionVerificationAffiliation, CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer.ServiceUSerializer


class MProviderListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionVerificationAffiliation]
    queryset = MProvider.objects.all()
    serializer_class = MProviderSerializer

    def get_queryset(self):
        return self.queryset.select_related('organization').filter(organization=self.kwargs.get('organization'))


class MProviderCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    serializer_class = MProviderSerializer.MProviderCSerializer


class MProviderRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole,
                          CustomPermissionVerificationAffiliation]
    queryset = MProvider.objects.all()
    lookup_field = 'id'
    serializer_class = MProviderSerializer


class MProviderDestroyAPIView(CustomGetObject, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = MProvider.objects.all()
    lookup_field = 'id'
