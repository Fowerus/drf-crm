from django.urls import path

from . import views


urlpatterns = [
	path('mcourier-l/<int:organization>/', views.MCourierListAPIView.as_view(), name = 'mcourier_l'),
	path('mcourier-c/', views.MCourierCreateAPIView.as_view(), name = 'mcourier_c'),
	path('mcourier-d/<str:_id>/', views.MCourierDestroyAPIView.as_view(), name = 'mcourier_d'),
]