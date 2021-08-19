from django.urls import path

from . import views


urlpatterns = [
    path('organizations/', views.OrganizationAPIView.as_view(), name = 'organization'),
]