from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('device-type-l/<int:organization>/', views.DeviceTypeListAPIView.as_view(), name = 'devicetype_l'),
    path('device-type-r/<int:id>/<int:organization>/', views.DeviceTypeRetrieveAPIView.as_view(), name = 'devicetype_r'),
    path('device-type-c/', views.DeviceTypeCreateAPIView.as_view(), name = 'devicetype_c'),
    path('device-type-ud/<int:id>/', views.DeviceTypeUpdateDestroyAPIView.as_view(), name = 'devicetype_ud'),

    path('device-maker-l/<int:organization>/', views.DeviceMakerListAPIView.as_view(), name = 'devicemaker_l'),
    path('device-maker-r/<int:id>/<int:organization>/', views.DeviceMakerRetrieveAPIView.as_view(), name = 'devicemaker_r'),
    path('device-maker-c/', views.DeviceMakerCreateAPIView.as_view(), name = 'devicemaker_c'),
    path('device-maker-ud/<int:id>/', views.DeviceMakerUpdateDestroyAPIView.as_view(), name = 'devicemaker_ud'),

    path('device-model-l/<int:organization>/', views.DeviceModelListAPIView.as_view(), name = 'device_model_l'),
    path('device-model-r/<int:id>/<int:organization>/', views.DeviceModelRetrieveAPIView.as_view(), name = 'device_model_r'),
    path('device-model-c/', views.DeviceModelCreateAPIView.as_view(), name = 'device_model_c'),
    path('device-model-ud/<int:id>/', views.DeviceModelUpdateDestroyAPIView.as_view(), name = 'device_model_ud'),

    path('device-kit-l/<int:organization>/', views.DeviceKitListAPIView.as_view(), name = 'device_kit_l'),
    path('device-kit-r/<int:id>/<int:organization>/', views.DeviceKitRetrieveAPIView.as_view(), name = 'device_kit_r'),
    path('device-kit-c/', views.DeviceKitCreateAPIView.as_view(), name = 'device_kit_c'),
    path('device-kit-ud/<int:id>/', views.DeviceKitUpdateDestroyAPIView.as_view(), name = 'device_kit_ud'),

    path('device-appearance-l/<int:organization>/', views.DeviceAppearanceListAPIView.as_view(), name = 'device_appearance_l'),
    path('device-appearance-r/<int:id>/<int:organization>/', views.DeviceAppearanceRetrieveAPIView.as_view(), name = 'device_appearance_r'),
    path('device-appearance-c/', views.DeviceAppearanceCreateAPIView.as_view(), name = 'device_appearance_c'),
    path('device-appearance-ud/<int:id>/', views.DeviceAppearanceUpdateDestroyAPIView.as_view(), name = 'device_appearance_ud'),

    path('device-defect-l/<int:organization>/', views.DeviceDefectListAPIView.as_view(), name = 'device_defect_l'),
    path('device-defect-r/<int:id>/<int:organization>/', views.DeviceDefectRetrieveAPIView.as_view(), name = 'device_defect_r'),
    path('device-defect-c/', views.DeviceDefectCreateAPIView.as_view(), name = 'device_defect_c'),
    path('device-defect-ud/<int:id>/', views.DeviceDefectUpdateDestroyAPIView.as_view(), name = 'device_defect_ud'),

    path('service-price-l/<int:organization>/', views.ServicePriceListAPIView.as_view(), name = 'service_price_l'),
    path('service-price-r/<int:id>/<int:organization>/', views.ServicePriceRetrieveAPIView.as_view(), name = 'service_price_r'),
    path('service-price-c/', views.ServicePriceCreateAPIView.as_view(), name = 'service_price_c'),
    path('service-price-ud/<int:id>/', views.ServicePriceUpdateDestroyAPIView.as_view(), name = 'service_price_ud'),

    path('order-history-c/', views.OrderHistoryCreateAPIView.as_view(), name = 'order_history_c')
]