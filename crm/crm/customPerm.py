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
				return bool(check_confirmed(requests.data['user']) and validate_func_map['role'](requests.data['role']), organization)

			return validate_func_map[str(view_name)](id_obj, organization)

		except:
			return False



class CustomPermissionGetUser(BasePermission):

	def has_permission(self, requests, view):

		try:
			user_data = get_userData(requests)
			view_name = get_viewName(view)
			id_obj = requests._request.resolver_match.kwargs.get('id')

			if id_obj:
				return id_obj == user_data['user_id']

			view.kwargs['id'] = user_data['user_id']
					
			return True
		except:
			return False
			