from bson.objectid import ObjectId
from rest_framework.permissions import BasePermission
from rest_framework import status
from rest_framework.response import Response
from core.views import get_userData, get_viewName, get_orgId, get_clientData, get_mproviderData, validate_func_map, check_confirmed
from Sessions.models import Session_user, Session_client


class CustomPermissionVerificationOrganization(BasePermission):

    def has_permission(self, requests, view):

        try:
            user_data = get_userData(requests)

            if requests.method == 'GET':
                return True

            id_obj = view.kwargs.get('id')

            if requests.method == 'POST':
                return requests.user.confirmed

            perms_map = {
                'patch': 'change_organization',
                'put': 'change_organization',
                'delete': 'delete_organization'
            }
            requests.POST._mutable = True
            requests.data.update({'organization':requests.user.current_org})

            return bool(requests.user.confirmed and len(requests.user.api_has_perm(perms_map[requests.method])) > 0)

        except Exception as e:
            return False


class CustomPermissionForList(BasePermission):
    def has_permission(self, requests, view):
        pass
        

class CustomPermissionVerificationRole(BasePermission):

    def has_permission(self, requests, view):

        view_name = get_viewName(view)

        perms_map = {
            'get': f'view_{view_name}',
            'post': f'add_{view_name}',
            'patch': f'change_{view_name}',
            'put': f'change_{view_name}',
            'delete': f'delete_{view_name}'
        }
        requests.POST._mutable = True
        requests.data.update({'organization': requests.user.current_org})

        view.service_id_list = requests.user.api_has_perm(perms_map[requests.method.lower()])

        view.view_name = view_name
        
        return bool(requests.user.confirmed and len(view.service_id_list) > 0)


class CustomPermissionCheckRelated(BasePermission):

    def has_permission(self, requests, view):
        if requests.method != "DELETE":
            global validate_func_map

            view_name = get_viewName(view)
            result = set()

            if 'user' in requests.data:
                result.add(requests.user.confirmed)

            elif view_name == 'order':
                validate_func_map.pop('devicedefect', 'devicetype')
                validate_func_map.pop('devicemaker', 'devicemodel')
                validate_func_map.pop('devicekit', 'deviceappearance')

            elif view_name == 'purchaserequest':
                validate_func_map.pop('product')

            for valid_key in requests.data.keys():
                if valid_key in validate_func_map:
                    result.add(validate_func_map[valid_key](
                        requests.data[valid_key], requests.user.current_org))

            return not (False in result)

        return True


class CustomPermissionGetUser(BasePermission):

    def has_permission(self, requests, view):

        try:
            view_name = get_viewName(view)

            if view_name != 'client':
                user_data = get_userData(requests)

                view.kwargs['id'] = user_data['user_id']

                return True
            else:
                client_data = get_clientData(requests)

                view.kwargs['id'] = client_data['client_id']
                return True

            return False
        except Exception as e:
            return False


class CustomPermissionSession(BasePermission):

    def has_permission(self, requests, view):
        try:
            view_name = get_viewName(view)

            sessions_validate_map = {
                'session_user': get_userData,
                'session_client': get_clientData
            }

            sessions_map = {
                'session_user': Session_user,
                'session_client': Session_client
            }

            data = sessions_validate_map[view_name](requests)
            key = view_name.split('_')[1]+'_id'
            if 'id' in view.kwargs:
                sessions_map[view_name](
                    session_map[view_name], data['session'], data[key], is_client='client' in view_name)
                return True

            view.kwargs['id'] = data[key]

            return True

        except Exception as e:
            return False


class CustomPermissionCheckSession(BasePermission):

    def has_permission(self, requests, view):
        try:
            try:
                data = get_userData(requests)
            except Exception as e:
                data = get_clientData(requests)

            return True

        except Exception as e:
            return False


class CustomPermissionMarketplaceHelper(BasePermission):

    def has_permission(self, requests, view):
        try:
            view.kwargs['_id'] = ObjectId(view.kwargs.get('_id'))
            return True
        except Exception as e:
            return False


class CustomPermissionMProviderAccess(BasePermission):

    def has_permission(self, requests, view):
        try:
            mprovider = get_mproviderData(requests)
            view.kwargs['organization'] = mprovider['organization']

            return True

        except Exception as e:
            return False
