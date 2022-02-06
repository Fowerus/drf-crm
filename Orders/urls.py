from django.urls import path
from . import views



urlpatterns = [
	path('order-l/', views.OrderListAPIView.as_view(), name = 'organization_order_l'),
    path('order-creator-l/', views.OrderCreatorListAPIView.as_view(), name = 'organization_order_creator_l'),
    path('order-executor-l/', views.OrderExecutorListAPIView.as_view(), name='organization_order_executor_l'),
    path('order-r/<int:id>/', views.OrderRetrieveAPIView.as_view(), name = 'organization_order_r'),
    path('order-c/', views.OrderCreateAPIView.as_view(), name = 'organization_order_c'),
    path('order-ud/<int:id>/', views.OrderUpdateDestroyAPIView.as_view(), name = 'organization_order_ud'),
]