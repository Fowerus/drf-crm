from django.urls import path

from rest_framework_simplejwt import views as jwt_view

from . import views


urlpatterns = [
    path('signup/',
         views.UserRegistrationAPIView.as_view(), name='registration'),

    path('singin/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('refresh/',
         views.MyTokenRefreshView.as_view(), name='token_refresh'),


    path('user/', views.UserRetrieveUpdateDestroyAPIView.as_view(), name='user'),
    path('test_send_post/', views.TestSendEmail.as_view(), name='test')
]
