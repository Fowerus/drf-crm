from rest_framework.permissions import BasePermission
from rest_framework import status
from rest_framework.response import Response
from .views import *
from Sessions.models import Session_user



class CustomPermissionVerificationOrganization(BasePermission):

	def has_permission(self, requests, view):

		try:

			if requests.method == 'GET':
				user_data = get_userData(requests)
				return True

			id_obj = requests._request.resolver_match.kwargs.get('id')


			if requests.method == 'POST':
				if check_confirmed(user_data['user_id']):
					return True
				return False

			perms_map = {
				'patch':'organization_change',
				'put':'organization_change',
				'delete':'organization_delete'
			}

			permissions = ['organization_creator', perms_map[str(requests.method).lower()]]
			return is_valid_member(user_data['user_id'], id_obj, permissions)
		except:
			return False



class CustomPermissionVerificationRole(BasePermission):

	def has_permission(self, requests, view):

		try:
			view_name = get_viewName(view)
			organization = get_orgId(requests)
			user_data = get_userData(requests)

			perms_map = {
				'creator':'organization_creator',
				'guru':f'{view_name}_guru',
				'get':f'{view_name}_view',
				'post':f'{view_name}_create',
				'patch':f'{view_name}_change',
				'put':f'{view_name}_change',
				'delete':f'{view_name}_delete'
			}

			permissions = [perms_map[str(requests.method).lower()], perms_map['guru'], perms_map['creator']]

			return is_valid_member(user_data['user_id'], organization,  permissions)
		except:
			return False



class CustomPermissionVerificationAffiliation(BasePermission):

	def has_permission(self, requests, view):

		try:
			organization = get_orgId(requests)
			id_obj = requests._request.resolver_match.kwargs.get('id')
			view_name = get_viewName(view)
			user_data = get_userData(requests)

			return validate_func_map[view_name](id_obj, organization)

		except:
			return False



class CustomPermissionCheckRelated(BasePermission):

	def has_permission(self, requests, view):
		if requests.method != "DELETE":
			global validate_func_map

			organization = get_orgId(requests)
			view_name = get_viewName(view)
			result = set()

			if 'user' in requests.data:
				result.add(check_confirmed(requests.data['user']))

			elif view_name == 'order':
				validate_func_map = validate_func_map[:len(validate_func_map)-6]
				
			for valid_key in requests.data.keys():
				if valid_key in validate_func_map:
					result.add(validate_func_map[valid_key](requests.data[valid_key], organization))
			return not (False in result)



		return True




class CustomPermissionGetUser(BasePermission):

	def has_permission(self, requests, view):

		try:
			view_name = get_viewName(view)
			
			id_obj = requests._request.resolver_match.kwargs.get('id')
			if view_name != 'client':
				user_data = get_userData(requests)

				if id_obj:
					return id_obj == user_data['user_id']

				view.kwargs['id'] = user_data['user_id']
						
				return True
			else:
				client_data = get_clientData(requests)
				if id_obj:
					return id_obj == client_data['client_id']

				view.kwargs['id'] = client_data['client_id']
				return True

			return False
		except:
			return False



class CustomPermissionSession(BasePermission):

	def has_permission(self, requests, view):
		try:
			view_name = get_viewName(view)

			sessions_map = {
				'session_user':get_userData,
				'session_client':get_clientData
			} 
			data = sessions_map[view_name](requests)

			id_obj = requests._request.resolver_match.kwargs.get('id')

			try:
				return id_obj == data['user_id']
			except:
				return id_obj == data['client_id'] 

		except:
			return False
			

class CustomPermissionCheckSession(BasePermission):

	def has_permission(self, requests, view):
		try:
			try:
				data = get_userData(requests)
			except:
				data = get_clientData(requests) 

			return True

		except:
			return False
			