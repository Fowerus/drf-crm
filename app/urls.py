"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path as url
from django.views.static import serve
from core.views import post_generator, post_test
from core.views import post_generator
from . import settings
from core.views import index_home

urlpatterns = [
    path('', index_home),
    path('test-generate-posts/', post_generator),

    path('admin/', admin.site.urls),
    path('users/', include('Users.urls')),
    path('organizations/', include('Organizations.urls')),
    path('sessions/', include('Sessions.urls')),
    path('clients/', include('Clients.urls')),
    path('orders/', include('Orders.urls')),
    path('verify-info/', include('VerifyInfo.urls')),
    path('market/', include('Market.urls')),
    path('marketplace/', include('Marketplace.urls')),
    path('handbook/', include('Handbook.urls')),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]
