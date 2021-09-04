import uuid
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
from crm.customPerm import *



class OrganizationListCreateAPIView(generics.ListCreateAPIView):
	permission_classes = [CustomPermissionVerificationOrganization]
	queryset = Organization.objects.all()
	serializer_class = OrganizationSerializer

	def post(self, requests):
		self.serializer_class = OrganizationSerializer.OrganizationCUSerializer 
		return super().post(requests)


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



class PermListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = CustomPermission.objects.all()
	serializer_class = PermissionSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class RoleListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = RoleSerializer
	queryset = Role.objects.all()

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class RoleCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = RoleSerializer.RoleCSerializer


class RoleRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = Role.objects.all()
	serializer_class = RoleSerializer


class RoleUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = Role.objects.all()
	serializer_class = RoleSerializer.RoleUSerializer




class Organization_memberListAPIView(generics.ListAPIView):
	queryset = Organization_member.objects.all()
	serializer_class = Organization_memberSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class Organization_memberCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	serializer_class = Organization_memberSerializer.Organization_memberCSerializer


class Organization_memberRetrieveAPIView(generics.RetrieveAPIView):
	queryset = Organization_member.objects.all()
	lookup_field = 'id'
	serializer_class = Organization_memberSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class Organization_memberUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = Organization_member.objects.all()
	serializer_class = Organization_memberSerializer.Organization_memberUSerializer




class ServiceListAPIView(generics.ListAPIView):
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class ServiceCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = ServiceSerializer.ServiceCSerializer


class ServiceRetrieveAPIView(generics.RetrieveAPIView):
	lookup_field = 'id'
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer


class ServiceUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = Service.objects.all()
	serializer_class = ServiceSerializer.ServiceUSerializer