from django.urls import path

from . import views


urlpatterns = [
    path('mproduct-l/', views.MProductListAPIView.as_view(), name='mproduct_l'),
    path('mproduct-r/<str:_id>/',
         views.MProductRetrieveAPIView.as_view(), name='mproduct_r'),
    path('mproduct-c/', views.MProductCreateAPIView.as_view(), name='mproduct_c'),
    path('mproduct-file-c/', views.MProductFileCreateAPIView.as_view(),
         name='mproduct_file_c'),
    path('mproduct-ud/<str:_id>/',
         views.MProductUpdateDestroyAPIView.as_view(), name='mproduct_ud'),


    path('mbusket-l/',
         views.MBusketListAPIView.as_view(), name='mbusket_l'),
    path('mbusket-mcourier-l/<str:_id>/',
         views.MBusketMCourierListAPIView.as_view(), name='mbusket_courier_l'),
    path('mbusket-r/<str:_id>/',
         views.MBusketRetrieveAPIView.as_view(), name='mbusket_r'),
    path('mbusket-c/', views.MBusketCreateAPIView.as_view(), name='mbusket_c'),
    path('mbusket-ud/<str:_id>/',
         views.MBusketUpdateDestroyAPIView.as_view(), name='mbusket_ud'),


    path('mcourier-l/',
         views.MCourierListAPIView.as_view(), name='mcourier_l'),
    path('mcourier-morder-l/',
         views.MCourierMOrderListAPIView.as_view(), name='mcourier_morder_l'),
    path('mcourier-c/', views.MCourierCreateAPIView.as_view(), name='mcourier_c'),
    path('mcourier-ud/<str:_id>/',
         views.MCourierUpdateDestroyAPIView.as_view(), name='mcourier_d'),


    path('morder-l/',
         views.MOrderListAPIView.as_view(), name='morder_l'),
    path('morder-mcourier-l/<str:_id>/',
         views.MOrderMCourierListAPIView.as_view(), name='morder_courier_l'),
    path('morder-for-provider-l/',
         views.MOrderForProviderListAPIView.as_view(), name='morder_provider_l'),
    path('morder-r/<str:_id>/',
         views.MOrderRetrieveAPIView.as_view(), name='morder_r'),
    path('morder-c/', views.MOrderCreateAPIView.as_view(), name='morder_c'),
    path('morder-ud/<str:_id>/',
         views.MOrderUpdateDestroyAPIView.as_view(), name='morder_ud'),
    path('morder-mcourier-u/<str:_id>/',
         views.MOrderForCourierUpdateAPIView.as_view(), name='morder_courier_u'),
]
