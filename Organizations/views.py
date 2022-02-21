import jwt

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.db import transaction

from rest_framework import status, permissions, filters
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

import django_filters

from .serializers import *

from Users.serializers import UserSerializer

from Organizations.models import *
from core.utils.customPerm import *
from core.utils.customViewMethods import *


class OrganizationListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [CustomPermissionVerificationOrganization]
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    filterset_fields = ['id', 'name']


    def post(self, request):
        self.serializer_class = OrganizationSerializer.OrganizationCSerializer
        return super().post(request)


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

    def patch(self, request, **kwargs):
        self.serializer_class = OrganizationSerializer.OrganizationUSerializer
        return super().patch(request, kwargs)

    def put(self, request, **kwargs):
        self.serializer_class = OrganizationSerializer.OrganizationUSerializer
        return super().put(request, kwargs)


class Organization_memberListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionCheckSession]
    queryset = Organization_member.objects.all()
    serializer_class = Organization_memberSerializer


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


class ServiceListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['organization__id']


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
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer.ServiceUSerializer

    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        members = Organization.objects.get(id = instance.organization.id).organization_members.all()

        for m in members:
            m.user.services.pop(m.user.services.index(instance.id))
            m.user.save()

        return super().destroy(request, *args, **kwargs)


class MProviderListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = MProvider.objects.all()
    serializer_class = MProviderSerializer
    filterset_fields = ['service__id']


class MProviderCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    serializer_class = MProviderSerializer.MProviderCSerializer


class MProviderRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = MProvider.objects.all()
    lookup_field = 'id'
    serializer_class = MProviderSerializer


class MProviderDestroyAPIView(CustomGetObject, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = MProvider.objects.all()
    lookup_field = 'id'


class PermissionListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = Permission.objects.filter(id__gt=24)
    filter_backends = [filters.SearchFilter]
    serializer_class = PermissionSerializer
    search_fields = ['name']
    perm_view_name = 'mygroup'


class MyGroupListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = MyGroup.objects.all()
    serializer_class = MyGroupSerializer
    filterset_fields = ['service__id']


class MyGroupCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    serializer_class = MyGroupSerializer.MyGroupCSerializer


class MyGroupRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [CustomPermissionCheckSession]
    queryset = MyGroup.objects.all()
    lookup_field = 'id'
    serializer_class = MyGroupSerializer


class MyGroupUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = MyGroup.objects.all()
    serializer_class = MyGroupSerializer.MyGroupUSerializer
