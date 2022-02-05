from django.urls import path

from . import views


urlpatterns = [
    path('organization-lc/', views.OrganizationListCreateAPIView.as_view(),
         name='organization_lc'),
    path('organization-creator-l/', views.OrganizationCreatorListAPIView.as_view(),
         name='organization_creator_l'),
    path('organization-rud/<int:id>/',
         views.OrganizationRetrieveUpdateDestroyAPIView.as_view(), name='organization_rud'),


    path('member-l/<int:organization>/',
         views.Organization_memberListAPIView.as_view(), name='organization_member_l'),
    path('member-r/<int:id>/',
         views.Organization_memberRetrieveAPIView.as_view(), name='organization_member_r'),
    path('member-c/', views.Organization_memberCreateAPIView.as_view(),
         name='organization_member_c'),
    path('member-ud/<int:id>/', views.Organization_memberUpdateDestroyAPIView.as_view(),
         name='organization_member_ud'),


    path('service-l/<int:organization>/',
         views.ServiceListAPIView.as_view(), name='organization_service_l'),
    path('service-r/<int:id>/<int:organization>/',
         views.ServiceRetrieveAPIView.as_view(), name='organization_service_r'),
    path('service-c/', views.ServiceCreateAPIView.as_view(),
         name='organization_service_c'),
    path('service-ud/<int:id>/', views.ServiceUpdateDestroyAPIView.as_view(),
         name='organization_service_ud'),


    path('mprovider-l/int:organization/',
         views.MProviderListAPIView.as_view(), name='mprovider_l'),
    path('mprovider-r/<int:id>/int:organization/',
         views.MProviderRetrieveAPIView.as_view(), name='mprovider_r'),
    path('mprovider-c/', views.MProviderCreateAPIView.as_view(), name='mprovider_c'),
    path('mprovider-d/int:id/',
         views.MProviderDestroyAPIView.as_view(), name='mprovider_d'),
]
