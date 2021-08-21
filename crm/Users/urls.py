from django.urls import path
from rest_framework.response import Response
from rest_framework_simplejwt import views as jwt_view

from . import views

urlpatterns = [
    path('auth/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', views.MyTokenRefreshView.as_view(), name='token_refresh'),

    path('auth/registration/', views.UserViewSet.as_view({
        'get': 'information_about_user',
        'patch':'update_user',
        'delete':'delete_user'
        }), name='registration'),
]