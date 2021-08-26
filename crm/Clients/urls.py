from django.urls import path

from . import views



urlpatterns = [
    path('client/', views.ClientViewSet.as_view({
        'get': 'list_orders_as_client',
        'patch':'update_client'
        }), name = 'client')
]