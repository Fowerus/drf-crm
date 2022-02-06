from django.contrib.auth import get_user_model

from rest_framework import status, permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import *

from Handbook.models import *
from core.utils.customPerm import *
from core.utils.customGet_object import *



class DeviceTypeListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceType.objects.all()
	serializer_class = DeviceTypeSerializer

	def get_queryset(self):
		return self.queryset.select_related('organization').filter(organization = self.kwargs.get('organization'))


class DeviceTypeCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	serializer_class = DeviceTypeSerializer.DeviceTypeCSerializer


class DeviceTypeRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = DeviceType.objects.all()
	serializer_class = DeviceTypeSerializer


class DeviceTypeUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	lookup_field = 'id'
	queryset = DeviceType.objects.all()
	serializer_class = DeviceTypeSerializer.DeviceTypeUSerializer




class DeviceMakerListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceMaker.objects.all()
	serializer_class = DeviceMakerSerializer

	def get_queryset(self):
		return self.queryset.select_related('organization').filter(organization = self.kwargs.get('organization'))


class DeviceMakerCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	serializer_class = DeviceMakerSerializer.DeviceMakerCSerializer


class DeviceMakerRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = DeviceMaker.objects.all()
	serializer_class = DeviceMakerSerializer


class DeviceMakerUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	lookup_field = 'id'
	queryset = DeviceMaker.objects.all()
	serializer_class = DeviceMakerSerializer.DeviceMakerUSerializer




class DeviceModelListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceModel.objects.all()
	serializer_class = DeviceModelSerializer

	def get_queryset(self):
		return self.queryset.select_related('organization').filter(organization = self.kwargs.get('organization'))


class DeviceModelCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	serializer_class = DeviceModelSerializer.DeviceModelCSerializer


class DeviceModelRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = DeviceModel.objects.all()
	serializer_class = DeviceModelSerializer


class DeviceModelUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	lookup_field = 'id'
	queryset = DeviceModel.objects.all()
	serializer_class = DeviceModelSerializer.DeviceModelUSerializer




class DeviceKitListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceKit.objects.all()
	serializer_class = DeviceKitSerializer

	def get_queryset(self):
		return self.queryset.select_related('organization').filter(organization = self.kwargs.get('organization'))


class DeviceKitCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	serializer_class = DeviceKitSerializer.DeviceKitCSerializer


class DeviceKitRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = DeviceKit.objects.all()
	serializer_class = DeviceKitSerializer


class DeviceKitUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	lookup_field = 'id'
	queryset = DeviceKit.objects.all()
	serializer_class = DeviceKitSerializer.DeviceKitUSerializer




class DeviceAppearanceListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceAppearance.objects.all()
	serializer_class = DeviceAppearanceSerializer

	def get_queryset(self):
		return self.queryset.select_related('organization').filter(organization = self.kwargs.get('organization'))


class DeviceAppearanceCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	serializer_class = DeviceAppearanceSerializer.DeviceAppearanceCSerializer


class DeviceAppearanceRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = DeviceAppearance.objects.all()
	serializer_class = DeviceAppearanceSerializer


class DeviceAppearanceUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	lookup_field = 'id'
	queryset = DeviceAppearance.objects.all()
	serializer_class = DeviceAppearanceSerializer.DeviceAppearanceUSerializer




class DeviceDefectListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceDefect.objects.all()
	serializer_class = DeviceDefectSerializer

	def get_queryset(self):
		return self.queryset.select_related('organization').filter(organization = self.kwargs.get('organization'))


class DeviceDefectCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	serializer_class = DeviceDefectSerializer.DeviceDefectCSerializer


class DeviceDefectRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = DeviceDefect.objects.all()
	serializer_class = DeviceDefectSerializer


class DeviceDefectUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	lookup_field = 'id'
	queryset = DeviceDefect.objects.all()
	serializer_class = DeviceDefectSerializer.DeviceDefectUSerializer




class ServicePriceListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = ServicePrice.objects.all()
	serializer_class = ServicePriceSerializer

	def get_queryset(self):
		return self.queryset.select_related('organization').filter(organization = self.kwargs.get('organization'))


class ServicePriceCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	serializer_class = ServicePriceSerializer.ServicePriceCSerializer


class ServicePriceRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = 'id'
	queryset = ServicePrice.objects.all()
	serializer_class = ServicePriceSerializer


class ServicePriceUpdateDestroyAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	lookup_field = 'id'
	queryset = ServicePrice.objects.all()
	serializer_class = ServicePriceSerializer.ServicePriceUSerializer



class OrderHistoryCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
	queryset = OrderHistory.objects.all()
	serializer_class = OrderHistorySerializer.OrderHistoryCSerializer