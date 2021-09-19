from rest_framework.permissions import BasePermission
from rest_framework import status
from rest_framework.response import Response
from .views import *
from Sessions.models import Session_user



class CustomPermissionVerificationOrganization(BasePermission):

	def has_permission(self, requests, view):

		try:
			user_data = get_userData(requests)

			if requests.method == 'GET':
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

			perms_map = {
				'creator':'organization_creator',
				'guru':f'{view_name}_guru',
				'get':f'{view_name}_view',
				'post':f'{view_name}_create',
				'patch':f'{view_name}_change',
				'put':f'{view_name}_change',
				'delete':f'{view_name}_delete'
			}

			if requests.method == 'GET':
				organization = requests._request.resolver_match.kwargs.get('organization')
			else:
				if type(requests.data['organization']) == list:
					organization = requests.data['organization'][0]
				else:
					organization = requests.data['organization']

			user_data = get_userData(requests)
			permissions = [perms_map[str(requests.method).lower()], perms_map['guru'], perms_map['creator']]

			return is_valid_member(user_data['user_id'], organization,  permissions)
		except:
			return False



class CustomPermissionVerificationAffiliation(BasePermission):

	def has_permission(self, requests, view):

		try:
			if requests.method == 'GET':
				organization = requests._request.resolver_match.kwargs.get('organization')
			else:
				if type(requests.data['organization']) == list:
					organization = requests.data['organization'][0]
				else:
					organization = requests.data['organization']


			id_obj = requests._request.resolver_match.kwargs.get('id')
			view_name = get_viewName(view)

			validate_func_map = {
				'client': check_orgClient,
				'order': check_orgOrder,
				'role':check_orgRole,
				'service':check_orgService,
				'organization_member':check_orgMember,
			}

			user_data = get_userData(requests)

			if view_name == 'organization_member' and requests.method == 'POST':
				return bool(check_confirmed(requests.data['user']) and validate_func_map['role'](requests.data['role'], organization))
			if view_name == 'order' and requests.method == 'POST':
				return bool(validate_func_map[str(view_name)](id_obj, organization)
						and validate_func_map['service'](requests.data['service'], organization)
						and validate_func_map['client'](requests.data['client'], organization))

			return validate_func_map[str(view_name)](id_obj, organization)

		except:
			return False



class CustomPermissionGetUser(BasePermission):

	def has_permission(self, requests, view):

		try:
			view_name = get_viewName(view)
			if view_name != 'client':
				user_data = get_userData(requests)
				id_obj = requests._request.resolver_match.kwargs.get('id')

				if id_obj:
					return id_obj == user_data['user_id']

				view.kwargs['id'] = user_data['user_id']
						
				return True

			client_data = get_clientData(requests)
			view.kwargs['id'] = client_data['client_id']

			return True
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
			