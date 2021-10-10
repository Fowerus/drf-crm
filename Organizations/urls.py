from django.urls import path

from . import views


urlpatterns = [
    path('organization-lc/', views.OrganizationListCreateAPIView.as_view(), name = 'organization_lc'),
    path('organization-rud/<int:id>/', views.OrganizationRetrieveUpdateDestroyAPIView.as_view(), name = 'organization_rud'),


    path('member-l/<int:organization>/', views.Organization_memberListAPIView.as_view(), name = 'organization_member_l'),
    path('member-r/<int:id>/', views.Organization_memberRetrieveAPIView.as_view(), name = 'organization_member_r'),
    path('member-c/', views.Organization_memberCreateAPIView.as_view(), name = 'organization_member_c'),
    path('member-ud/<int:id>/', views.Organization_memberUpdateDestroyAPIView.as_view(), name = 'organization_member_ud'),


    path('role-l/<int:organization>/', views.RoleListAPIView.as_view(), name = 'organization_role_l'),
    path('role-r/<int:id>/<int:organization>/', views.RoleRetrieveAPIView.as_view(), name = 'organization_role_r'),
    path('role-c/', views.RoleCreateAPIView.as_view(), name = 'organization_role_c'),
    path('role-ud/<int:id>/', views.RoleUpdateDestroyAPIView.as_view(), name = 'organization_role_ud'),

    path('perm-l/<int:organization>/', views.PermListAPIView.as_view(), name = 'organization_perm_l'),


    path('service-l/<int:organization>/', views.ServiceListAPIView.as_view(), name = 'organization_service_l'),
    path('service-r/<int:id>/<int:organization>/', views.ServiceRetrieveAPIView.as_view(), name = 'organization_service_r'),
    path('service-c/', views.ServiceCreateAPIView.as_view(), name = 'organization_service_c'),
    path('service-ud/<int:id>/', views.ServiceUpdateDestroyAPIView.as_view(), name = 'organization_service_ud'),
]
