from django.urls import path

from rest_framework_simplejwt import views as jwt_view

from . import views


urlpatterns = [
    path('auth/registration/', views.UserRegistrationViewSet.as_view({'post':'registration_user'}), name = 'registration'),

    path('auth/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', views.MyTokenRefreshView.as_view(), name='token_refresh'),


    path('user/', views.UserViewSet.as_view({
        'get': 'information_about_user',
        'patch':'update_user',
        'delete':'delete_user'
        }), name='user'),
    path('user/executor', views.UserViewSet.as_view({'get':'list_user_executorOrders'}), name = 'user_executor'),

    path('verify-email/', views.VerifyNumberEmailViewSet.as_view({'post':'verify_email_send'}), name = 'verify_email'),
    path('accept-email/<int:code>/', views.VerifyNumberEmailViewSet.as_view({'post':'accept_email'}), name = 'accept_email'),
]