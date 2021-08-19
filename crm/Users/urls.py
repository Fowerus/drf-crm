from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework.response import Response

from . import views

urlpatterns = [
    path('auth/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('auth/registration/', views.Registration.as_view(), name='registration'),
    path('auth/login/', views.Login.as_view(), name='login'),
]