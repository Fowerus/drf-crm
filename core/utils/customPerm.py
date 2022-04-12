from bson.objectid import ObjectId

from rest_framework.permissions import BasePermission
from rest_framework import status
from rest_framework.response import Response

from core.views import get_userData, get_viewName, get_orgId, get_mproviderData, validate_func_map, check_confirmed


class CustomPermissionVerificationOrganization(BasePermission):

    def has_permission(self, request, view):

        try:
            user_data = get_userData(request)

            if request.method == 'GET':
                return True

            id_obj = view.kwargs.get('id')

            if request.method == 'POST':
                return request.user.confirmed

            perms_map = {
                'patch': 'change_organization',
                'put': 'change_organization',
                'delete': 'delete_organization'
            }
            request.POST._mutable = True
            request.data.update({'organization':request.user.current_org})

            return bool(request.user.confirmed and len(request.user.api_has_perm(perms_map[request.method])) > 0)

        except Exception as e:
            return False


class CustomPermissionVerificationRole(BasePermission):

    def has_permission(self, request, view):

        view.view_name = get_viewName(view)
        view.user = request.user

        perms_map = {
            'get': f'view_{view.view_name}',
            'post': f'add_{view.view_name}',
            'patch': f'change_{view.view_name}',
            'put': f'change_{view.view_name}',
            'delete': f'delete_{view.view_name}'
        }
        request.POST._mutable = True

        if view.view_name in ['morder', 'mproduct', 'mbusket', 'mcourier']:
            request.data.update({'organization': {"id":request.user.current_org}})
        else:
            request.data.update({'organization': request.user.current_org})

        view.service_id_list = request.user.api_has_perm(perms_map[request.method.lower()])

        return bool(request.user.confirmed and len(view.service_id_list) > 0)


class CustomPermissionCheckRelated(BasePermission):

    def has_permission(self, request, view):
        if request.method != "DELETE":
            global validate_func_map

            view_name = get_viewName(view)
            result = set()
            blocklist = list()

            if 'user' in request.data:
                result.add(request.user.confirmed)

            elif view_name == 'order':
                blocklist.append('devicedefect')
                blocklist.append('devicetype')
                blocklist.append('devicemaker')
                blocklist.append('devicemodel')
                blocklist.append('devicekit')
                blocklist.append('deviceappearance')

            elif view_name == 'purchaserequest':
                validate_func_map.pop('product')

            for valid_key, value in request.data.items():
                if valid_key in validate_func_map and valid_key not in blocklist:
                    result.add(validate_func_map[valid_key](
                        value, request.user.current_org, request = request))

            return not (False in result)

        return True


class CustomPermissionCheckRelatedMarketplace(BasePermission):

    def has_permission(self, request, view):
        if request.method != "DELETE":
            try:
                global validate_func_map

                result = set()
                blocklist = list()

                for i in ['member', 'author']:
                    if i in request.data:
                        result.add(validate_func_map['member'](
                            request.data[i].get('id', None), request.user.current_org, request = request))

                blocklist.append('member')

                for valid_key, value in request.data.items():
                    if valid_key in validate_func_map and valid_key not in blocklist:
                        result.add(validate_func_map[valid_key](
                            value.get('id'), request.user.current_org, request = request))

                return not (False in result)

            except:
                return False
        return True



class CustomPermissionGetUser(BasePermission):

    def has_permission(self, request, view):

        try:
            view_name = get_viewName(view)

            if view_name != 'client':
                user_data = get_userData(request)

                view.kwargs['id'] = user_data['user_id']

                return True
            else:

                return True

            return False
        except Exception as e:
            return False



class CustomPermissionCheckSession(BasePermission):

    def has_permission(self, request, view):
        try:
            data = get_userData(request)

            return True

        except Exception as e:
            return False


class CustomPermissionMarketplaceHelper(BasePermission):

    def has_permission(self, request, view):
        try:
            view.kwargs['_id'] = ObjectId(view.kwargs.get('_id'))
            return True
        except Exception as e:
            return False


class CustomPermissionMProviderAccess(BasePermission):

    def has_permission(self, request, view):
        try:
            mprovider = get_mproviderData(request)
            view.kwargs['organization'] = mprovider['organization']

            return True

        except Exception as e:
            return False