from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

from .serializers import *

from Handbook.models import *
from core.utils.customPerm import *
from core.utils.customViewMethods import *



class DeviceTypeListAPIView(CustomFilterQueryset, generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceType.objects.all()
	serializer_class = DeviceTypeSerializer
	filterset_fields = ['service__id']


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




class DeviceMakerListAPIView(CustomFilterQueryset, generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceMaker.objects.all()
	serializer_class = DeviceMakerSerializer
	filterset_fields = ['service__id']


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




class DeviceModelListAPIView(CustomFilterQueryset, generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceModel.objects.all()
	serializer_class = DeviceModelSerializer
	filterset_fields = ['service__id']


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




class DeviceKitListAPIView(CustomFilterQueryset, generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceKit.objects.all()
	serializer_class = DeviceKitSerializer
	filterset_fields = ['service__id']


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




class DeviceAppearanceListAPIView(CustomFilterQueryset, generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceAppearance.objects.all()
	serializer_class = DeviceAppearanceSerializer
	filterset_fields = ['service__id']


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




class DeviceDefectListAPIView(CustomFilterQueryset, generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = DeviceDefect.objects.all()
	serializer_class = DeviceDefectSerializer
	filterset_fields = ['service__id']


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




class ServicePriceListAPIView(CustomFilterQueryset, generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = ServicePrice.objects.all()
	serializer_class = ServicePriceSerializer
	filterset_fields = ['service__id']


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