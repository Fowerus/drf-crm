from django.urls import path

from . import views


urlpatterns = [
    # path('auth/token/', views.ClientLoginAPIView.as_view(), name='client_login'),
    # path('client-u/<int:id>/', views.ClientUpdateAPIView.as_view(), name='client_u'),

    path('client-card-l/<int:organization>/',
         views.ClientCardListAPIView.as_view(), name='client_card_l'),
    path('client-card-l/<int:organization>/p=<str:phone>/',
         views.ClientCardListAPIView.as_view(), name='client_card_phone'),
    path('client-card-l/<int:organization>/f=<str:fio>/',
         views.ClientCardListAPIView.as_view(), name='client_card_fio'),
    path('client-card-r/<int:id>/',
         views.ClientCardRetrieveAPIView.as_view(), name='client_card_r'),
    path('client-card-c/', views.ClientCardCreateAPIView.as_view(),
         name='client_card_c'),
    path('client-card-ud/<int:id>/',
         views.ClientCardUpdateAPIView.as_view(), name='client_card_u'),
]
