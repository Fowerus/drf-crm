from django.contrib.auth import get_user_model

from rest_framework import status, permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import *

from Handbook.models import *
from crm.customPerm import *



class DeviceTypeListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceType.objects.all()
	serializer_class = DeviceTypeSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class DeviceTypeCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = DeviceTypeSerializer.DeviceTypeCSerializer


class DeviceTypeRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = DeviceType.objects.all()
	serializer_class = DeviceTypeSerializer


class DeviceTypeUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = DeviceType.objects.all()
	serializer_class = DeviceTypeSerializer.DeviceTypeUSerializer




class DeviceMakerListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceMaker.objects.all()
	serializer_class = DeviceMakerSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class DeviceMakerCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = DeviceMakerSerializer.DeviceMakerCSerializer


class DeviceMakerRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = DeviceMaker.objects.all()
	serializer_class = DeviceMakerSerializer


class DeviceMakerUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = DeviceMaker.objects.all()
	serializer_class = DeviceMakerSerializer.DeviceMakerUSerializer




class DeviceModelListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceModel.objects.all()
	serializer_class = DeviceModelSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class DeviceModelCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = DeviceModelSerializer.DeviceModelCSerializer


class DeviceModelRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = DeviceModel.objects.all()
	serializer_class = DeviceModelSerializer


class DeviceModelUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = DeviceModel.objects.all()
	serializer_class = DeviceModelSerializer.DeviceModelUSerializer




class DeviceKitListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceKit.objects.all()
	serializer_class = DeviceKitSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class DeviceKitCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = DeviceKitSerializer.DeviceKitCSerializer


class DeviceKitRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = DeviceKit.objects.all()
	serializer_class = DeviceKitSerializer


class DeviceKitUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = DeviceKit.objects.all()
	serializer_class = DeviceKitSerializer.DeviceKitUSerializer




class DeviceAppearanceListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceAppearance.objects.all()
	serializer_class = DeviceAppearanceSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class DeviceAppearanceCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = DeviceAppearanceSerializer.DeviceAppearanceCSerializer


class DeviceAppearanceRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = DeviceAppearance.objects.all()
	serializer_class = DeviceAppearanceSerializer


class DeviceAppearanceUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = DeviceAppearance.objects.all()
	serializer_class = DeviceAppearanceSerializer.DeviceAppearanceUSerializer




class DeviceDefectListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceDefect.objects.all()
	serializer_class = DeviceDefectSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class DeviceDefectCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = DeviceDefectSerializer.DeviceDefectCSerializer


class DeviceDefectRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = DeviceDefect.objects.all()
	serializer_class = DeviceDefectSerializer


class DeviceDefectUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = DeviceDefect.objects.all()
	serializer_class = DeviceDefectSerializer.DeviceDefectUSerializer




class ServicePriceListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = ServicePrice.objects.all()
	serializer_class = ServicePriceSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = self.kwargs.get('organization'))


class ServicePriceCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = ServicePriceSerializer.ServicePriceCSerializer


class ServicePriceRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = ServicePrice.objects.all()
	serializer_class = ServicePriceSerializer


class ServicePriceUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = 'id'
	queryset = ServicePrice.objects.all()
	serializer_class = ServicePriceSerializer.ServicePriceUSerializer