from django.urls import path

from . import views



urlpatterns = [
	path('session', views.SessionAPIView.as_view(), name = 'session')
]