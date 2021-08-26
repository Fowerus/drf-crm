from django.urls import path

from rest_framework_simplejwt import views as jwt_view

from . import views

urlpatterns = [
    path('client/', views.ClientViewSet.as_view({
        'get': 'list_orders_as_client',
        'patch':'update_client'
        }), name = 'client')
]