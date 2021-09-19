from django.urls import path
from . import views



urlpatterns = [
    # path('verify-client-number/', views.ClientVerifyInfoSendNumberAPIView.as_view(), name = 'verify_client_number'),
    path('accept-client-info/', views.ClientVerifyInfoAcceptAPIView.as_view(), name = 'accept_client_info'),

    path('verify-user-email/', views.UserVerifyInfoSendEmailAPIView.as_view(), name = 'verify_user_email'),
    # path('verify-user-number/', views.UserVerifyInfoSendNumberAPIView.as_view(), name = 'verify_user_number'),
    path('accept-user-info/', views.UserVerifyInfoAcceptAPIView.as_view(), name = 'accept_user_info'),
]
