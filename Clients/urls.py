from django.urls import path

from . import views



urlpatterns = [
    path('auth/token/', views.ClientLoginAPIView.as_view(), name = 'client_login'),

    path('client-c/', views.ClientCreateAPIView.as_view(), name = 'organization_client_c'),
    path('client-l/<int:organization>/', views.ClientListAPIView.as_view(), name = 'organization_client_l'),
    path('client-u/<int:id>/', views.ClientUpdateAPIView.as_view(), name = 'organization_client_u'),
    path('client-r/<int:id>/<int:organization>/', views.ClientRetrieveAPIView.as_view(), name = 'organization_client_r'),
]
