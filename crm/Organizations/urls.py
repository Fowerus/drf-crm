from django.urls import path

from . import views


urlpatterns = [
    path('organizations/', views.OrganizationAPIView.as_view(), name = 'organization'),

    path('number/', views.Organization_numberViewSet.as_view({
        'get':'list_organizations_numbers',
        'post':'create_organization_number',
        'patch':'update_organization_number',
        'delete':'delete_organization_number'
        }), name = 'organization_number'),
    path('number-all/<int:org_id>', views.Organization_numberViewSet.as_view({'get':'list_organization_numbers'}), name = 'list_organization_numbers'),


    path('link/', views.Organization_linkViewSet.as_view({
        'get':'list_organizations_links',
        'post':'create_organization_link',
        'patch':'update_organization_link',
        'delete':'delete_organization_link'
        }), name = 'organization_link'),
    path('link-all/<int:org_id>', views.Organization_numberViewSet.as_view({'get':'list_organization_links'}), name = 'list_organization_links'),


    path('member/', views.Organization_linkViewSet.as_view({
        'get':'list_all_organizations_members',
        'post':'create_organization_member',
        'patch':'update_organization_member',
        'delete':'delete_organization_member'
        }), name = 'organization_member'),
    path('member-all/<int:org_id>', views.Organization_memberViewSet.as_view({'get':'list_organization_members'}), name = 'list_organization_members'),


    path('role/', views.RolePermViewSet.as_view({
        'post':'create_role',
        'patch':'updata_role',
        'delete':'delete_role'
        }), name = 'organization_role'),
    path('role-all/<int:org_id>', views.RolePermViewSet.as_view({'get':'list_roles'}), name = 'list_roles'),
    path('perms-all/<int:org_id>', views.RolePermViewSet.as_view({'get':'list_permissions'}), name = 'list_permissions'),


    path('service/', views.ServiceViewSet.as_view({
        'get':'list_all_service',
        'post':'create_service',
        'patch':'update_service',
        'delete':'delete_service'
        }), name = 'organization_service'),
    path('service-all/<int:org_id>', views.ServiceViewSet.as_view({'get':'list_organization_services'}), name = 'list_organization_services'),


    path('client/', views.ClientViewSet.as_view({
        'post':'create_client',
        'patch':'update_client',
        'delete':'delete_client'
        }), name = 'organization_client'),
    path('client-all/<int:org_id>', views.ClientViewSet.as_view({'get':'list_clients'}), name = 'list_clients'),


    path('order/', views.OrderViewSet.as_view({
        'post':'create_order',
        'patch':'update_order',
        'delete':'delete_order'
        }), name = 'organization_order'),
    path('order-all/<int:org_id>', views.OrderViewSet.as_view({'get':'list_orders'}), name = 'list_orders'),
    path('order-block/', views.OrderViewSet.as_view({'post':'block_order'}), name = 'block_order'),
]