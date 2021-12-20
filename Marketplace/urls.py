from django.urls import path

from . import views


urlpatterns = [
	path('morder-c/', views.MOrderCreateAPIView.as_view(), name = 'morder_c'),


	path('mproduct-l/<int:organization>/', views.MProductListAPIView.as_view(), name = 'mproduct_l'),
	path('mproduct-r/<str:_id>/<int:organization>/', views.MProductRetrieveAPIView.as_view(), name = 'mproduct_r'),
	path('mproduct-c/', views.MProductCreateAPIView.as_view(), name = 'mproduct_c'),
	path('mproduct-ud/<str:_id>/', views.MProductUpdateDestroyAPIView.as_view(), name = 'mproduct_ud'),


	path('mcourier-l/<int:organization>/', views.MCourierListAPIView.as_view(), name = 'mcourier_l'),
	path('mcourier-c/', views.MCourierCreateAPIView.as_view(), name = 'mcourier_c'),
	path('mcourier-d/<str:_id>/', views.MCourierDestroyAPIView.as_view(), name = 'mcourier_d'),
]