from django.urls import path

from . import views


urlpatterns = [
	path('mproduct-l/<int:organization>/', views.MProductListAPIView.as_view(), name = 'mproduct_l'),
	path('mproduct-r/<str:_id>/<int:organization>/', views.MProductRetrieveAPIView.as_view(), name = 'mproduct_r'),
	path('mproduct-c/', views.MProductCreateAPIView.as_view(), name = 'mproduct_c'),
	path('mproduct-ud/<str:_id>/', views.MProductUpdateDestroyAPIView.as_view(), name = 'mproduct_ud'),


	path('mbusket-l/<int:organization>/', views.MBusketListAPIView.as_view(), name = 'mbusket_l'),
	path('mbusket-r/<str:_id>/<int:organization>/', views.MBusketRetrieveAPIView.as_view(), name = 'mbusket_r'),
	path('mbusket-c/', views.MBusketCreateAPIView.as_view(), name = 'mbusket_c'),
	path('mbusket-ud/<str:_id>/', views.MBusketUpdateDestroyAPIView.as_view(), name = 'mbusket_ud'),


	path('mcourier-l/<int:organization>/', views.MCourierListAPIView.as_view(), name = 'mcourier_l'),
	path('mcourier-c/', views.MCourierCreateAPIView.as_view(), name = 'mcourier_c'),
	path('mcourier-ud/<str:_id>/', views.MCourierUpdateDestroyAPIView.as_view(), name = 'mcourier_d'),


	path('morder-l/<int:organization>/', views.MOrderListAPIView.as_view(), name = 'morder_l'),
	path('morder-provider-l/<int:organization>/', views.MOrderListAPIView.as_view(), name = 'morder_provider_l'),
	path('morder-r/<str:_id>/<int:organization>/', views.MOrderRetrieveAPIView.as_view(), name = 'morder_r'),
	path('morder-c/', views.MOrderCreateAPIView.as_view(), name = 'morder_c'),
	path('morder-ud/<str:_id>/', views.MOrderUpdateDestroyAPIView.as_view(), name = 'morder_ud'),
	path('morder-courier-u/<str:_id>/', views.MOrderForCourierUpdateAPIView.as_view(), name = 'morder_courier_ud'),
]