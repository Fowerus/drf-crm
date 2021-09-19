from django.urls import path

from rest_framework_simplejwt import views as jwt_view

from . import views



urlpatterns = [
    path('auth/registration/', views.UserRegistrationAPIView.as_view(), name = 'registration'),

    path('auth/token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', views.MyTokenRefreshView.as_view(), name='token_refresh'),


    path('user/<int:id>/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),
    path('user/executor/', views.UserExecutorListAPIView.as_view(), name='user_executor'),
]
