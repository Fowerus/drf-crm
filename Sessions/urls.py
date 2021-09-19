from django.urls import path

from . import views



urlpatterns = [
	path('session-user-l/<int:id>/', views.Session_userListAPIView.as_view(), name = 'session_user_l'),
	path('session-user-d/<int:id>/', views.Session_userDestroyAPIView.as_view(), name = 'session_user_d'),

	path('session-client-l/<int:id>/', views.Session_clientListAPIView.as_view(), name = 'session_user_l'),
	path('session-client-d/<int:id>/', views.Session_clientDestroyAPIView.as_view(), name = 'session_user_d')
]
