from django.urls import path
from . import views


urlpatterns = [
	path('order-l/<int:organization>/', views.OrderListAPIView.as_view(), name = 'organization_order_l'),
    path('order-c/', views.OrderCreateAPIView.as_view(), name = 'organization_order_c'),
    path('order-ud/<int:id>/', views.OrderUpdateDestroyAPIView.as_view(), name = 'organization_order_ud'),
    path('order-r/<int:organization>/', views.OrderRetrieveAPIView.as_view(), name = 'organization_order_r'),
]