import jwt
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response

from .serializers import *
from crm.views import *
# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyOTUxNTczMSwianRpIjoiZmIxMWEzZTNjZGI2NDI0MTk2YWI0OGQ5MmFmMWQxYjkiLCJ1c2VyX2lkIjoyfQ.NpqsAxf2vhMS57xMOBV3g1GN4Xm2oWH-dGl0Clo3uBg",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwNTUyNTMxLCJqdGkiOiI1NThmNDE0MjgxMGE0MDBiODI2OGIxNTE0Yzc2ODQyYSIsInVzZXJfaWQiOjJ9.ZGG4NtbrpH-Srz7oEapSoWIQ8z_c_BiOYra5ed2cKhw",
#     "expire_at": 0
# }


class OrganizationAPIView(APIView):
	serializer_class = OrganizationSerializer

	def get(self, requests):
		if check_authHeader(requests):
			try:
				all_organizations = Organization.objects.all()
				serializer = self.serializer_class(all_organizations, many = True)	

				return Response(serializer.data, status = status.HTTP_200_OK)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def post(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)
			if not check_memberships(user_data['user_id']):
				serializer = self.serializer_class.OrganizationCSerializer(data = requests.data)
				if serializer.is_valid():
					serializer.save()

					return Response(serialzier.data, status = status.HTTP_201_CREATE)

				else:
					return Response(status = status.HTTP_400_BAD_REQUEST)
			else:
				return Response(status = status.HTTP_403_FORBIDDEN)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def patch(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Organization-PATCH']):
	
					current_org = Organization.objects.get(id = 1)

					output = {
						'success':{},
						'error':{}
					}

					if 'name' in requests.data:
						if 10 <= len(requests.data['name']) <= 150:
							current_org.name = requests.data['name']
							output['success']['name'] = 'Name changed successfully'
						else:
							output['error']['name'] = 'Name is too long or too short'

					if 'description' in requests.data:
						if 10 <= len(requests.data['description']) <= 500:
							current_org.description = requests.data['description']
							output['success']['description'] = 'Description changed successfully'
						else:
							output['error']['description'] = 'Description is too long or too short'

					if 'address' in requests.data:
						if 10 <= len(requests.data['description']) <= 500:
							current_org.description = requests.data['description']
							output['success']['address'] = 'Address changed successfully'
						else:
							output['error']['address'] = 'Address is too long or too short'

					if len(output['success']) > 0:
						current_org.save()

					return Response(output, status = status.HTTP_200_OK)

				else:
					return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def delete(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)
			if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Organization-DELETE']):
				try:
					Organization.objects.get(id = requests.data['organization']).delete()

					return Response(status = status.HTTP_200_OK)

				except:
					return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			else:
				return Response(status = status.HTTP_403_FORBIDDEN)

		return Response(status = status.HTTP_401_UNAUTHORIZED)



class Organization_numberAPIView(ViewSet):
	serializer_class = Organization_numberSerializer

	def list_organizations_numbers(self, requests):
		if check_authHeader(requests):
			try:
				all_organization_number = Organization_number.objects.all()
				serializer = self.serializer_class(all_organization_number, many = True)

				return Response(serializer.data, status = status.HTTP_200_OK)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def list_organization_numbers(self, requests, org_id):
		if check_authHeader(requests):
			try:
				all_organization_number = Organization_number.objects.filter(id = org_id)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			serializer = self.serializer_class(all_organization_number, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def create_organization_number(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Organization_number-POST', 'Organization_number-GURU']):
					serializer = self.serializer_class.Organization_numberCSerializer(data = requests.data)
					if serializer.is_valid():
						serializer.save()

						return Response(status = status.HTTP_200_OK)

					else:
						return Response(status = status.HTTP_400_BAD_REQUEST)
				else:
					return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def update_organization_number(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Organization_number-PATCH', 'Organization_number-GURU']):
					if check_orgNumber(requests.data['number_id'], requests.data['organization']):
						current_number = Organization_number.objects.get(id = requests.data['number_id'])
						if 'new_number' in requests.data:

							try:
								current_number.number = requests.data['new_number']
								current_number.save()

								return Response(status = status.HTTP_200_OK)

							except:
								return Response({'error':'Bad new number'}, status = status.HTTP_400_BAD_REQUEST)

				return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def delete_organization_number(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Organization_number-DELETE', 'Organization_number-GURU']):
					if check_orgNumber(requests.data['number_id'], requests.data['organization']):

						try:
							Organization_number.objects.get(id = requests.data['number_id']).delete()

							return Response(status = status.HTTP_200_OK)

						except:
							return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

				return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)



class Organization_linkAPIView(ViewSet):
	serializer_class = Organization_linkSerializer

	def list_organizations_links(self, requests):
		if check_authHeader(requests):
			try:
				all_organization_link = Organization_link.objects.all()
				serializer = self.serializer_class(all_organization_link, many = True)

				return Response(serializer.data, status = status.HTTP_200_OK)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def list_organization_links(self, requests, org_id):
		if check_authHeader(requests):
			try:
				all_organization_link = Organization_link.objects.filter(id = org_id)
				serializer = self.serializer_class(all_organization_link, many = True)

				return Response(serializer.data, status = status.HTTP_200_OK)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def create_organization_link(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Organization_link-POST', 'Organization_link-GURU']):
					serializer = self.serializer_class.Organization_linkCSerializer(data = requests.data)
					if serializer.is_valid():
						serializer.save()

						return Response(status = status.HTTP_200_OK)

					else:
						return Response(status = status.HTTP_400_BAD_REQUEST)
				else:
					return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def update_organization_link(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Organization_link-PATCH', 'Organization_link-GURU']):
					if check_orgLink(requests.data['link_id'], requests.data['organization']):
						current_number = Organization_number.objects.get(id = requests.data['link_id'])
						if 'new_link' in requests.data:

							try:
								current_number.number = requests.data['new_link']
								current_number.save()

								return Response(status = status.HTTP_200_OK)

							except:
								return Response({'error':'Bad new link'}, status = status.HTTP_400_BAD_REQUEST)

				return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def delete_organization_link(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Organization_number-DELETE', 'Organization_number-GURU']):
					if check_orgLink(requests.data['number_id'], requests.data['organization']):

						try:
							Organization_link.objects.get(id = requests.data['number_id']).delete()

							return Response(status = status.HTTP_200_OK)

						except:
							return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

				return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)



class Organization_memberAPIView(ViewSet):
	serializer_class = Organization_memberSerializer

	def list_all_organizations_member(self, requests):
		if check_authHeader(requests):
			try:
				all_organization_members = Organization_member.objects.all()
				serializer = self.serializer_class(all_organization_members, many = True)

				return Response(serializer.data, status = status.HTTP_200_OK)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def list_organization_members(self, requests, org_id):
		if check_authHeader(requests):
			try:
				all_organization_members = Organization_member.objects.filter(organization = org_id)
				serializer = self.serializer_class(all_organization_members, many = True)

				return Response(serializer.data, status = status.HTTP_200_OK)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def create_organization_member(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Organization_member-POST', 'Organization_member-GURU']):
					serializer = self.serializer_class.Organization_memberCSerializer(data = requests.data)
					if serializer.is_valid():
						serializer.save()

						return Response(status = status.HTTP_200_OK)

					else:
						return Response(status = status.HTTP_400_BAD_REQUEST)
				else:
					return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def update_organization_member(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Organization_member-PATCH', 'Organization_member-GURU']):
					if check_orgMember(requests.data['member_id'], requests.data['organization']):

						try:
							current_member = Organization_member.objects.get(id = requests.data['member_id'])
							current_member.role = requests.data['new_role']
							current_member.save()

							return Response(status = status.HTTP_200_OK)

						except:
							return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

				return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def delete_organization_member(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Organization_member-DELETE', 'Organization_member-GURU']):
					if check_orgMember(requests.data['member_id'], requests.data['organization']):

						try:
							Organization_member.objects.get(id = requests.data['member_id']).delete()

							return Response(status = status.HTTP_200_OK)

						except:
							return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

				return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)



class RolePermAPIView(ViewSet):
	serializer_class = RoleSerializer

	def list_permissions(self, requests, org_id):
		if check_authHeader(requests):
			user_data = get_userData(requests)
			if is_valid_member(user_data['user_id'], org_id, ['Organization-CREATOR', 'Role-POST', 'Role-GURU']):
				try:
					all_permissions = Permission.objects.all()
					serializer = PermissionSerializer(all_permissions, many = True)

					return Response(serializer.data, status = status.HTTP_200_OK)
				except:
					return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			return Response(status = status.HTTP_403_FORBIDDEN)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def list_roles(self, requests, org_id):
		if check_authHeader(requests):
			user_data = get_userData(requests)
			if is_valid_member(user_data['user_id'], org_id, ['Organization-CREATOR', 'Role-GET', 'Role-GURU']):
				try:
					all_role = Role.objects.filter(organization = org_id)
					serializer = self.serializer_class(all_role, many = True)

					return Response(serializer.data, status = status.HTTP_200_OK)
				except:
					return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			return Response(status = status.HTTP_403_FORBIDDEN)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def create_role(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Role-POST', 'Role-GURU']):
					serializer = self.serializer_class.RoleCSerializer(data = requests.data)
					if serializer.is_valid():
						serializer.save()

						return Response(status = status.HTTP_200_OK)

					else:
						return Response(status = status.HTTP_400_BAD_REQUEST)
				else:
					return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def update_role(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:

				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Role-PATCH', 'Role-GURU']):
					if check_orgRole(requests.data['role_id'], requests.data['organization']):
						current_role = Role.objects.get(id = requests.data['role_id'])

						output = {
							'success':{},
							'error':{}
						}

						if 'new_permissions' in requests.data:
							try:
								old_perms = set(current_role.permissions.all())
								current_role.permissions.set(requests.data['new_permissions'])
								add_remove_perms = set(current_role.permissions.all())
								new_perms = old_perms ^ add_remove_perms
								current_role.permissions.set(new_perms)
								output['success']['permissions'] = "Permissions successfully changed"

							except:
								output['error']['permissions'] = 'Some error on the server'

						if 'name' in requests.data:
							if 10 <= requests.data['name'] <= 100:
								current_role.name = requests.data['name']
								output['success']['name'] = 'Name changed successfully'
							else:
								output['error']['name'] = 'Name is too short or too long'


						if len(output['success']) > 0:
							current_role.save()

						return Response(output, status = status.HTTP_200_OK)


				return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def delete(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Role-DELETE', 'Role-GURU']):
					if check_orgRole(requests.data['role_id'], requests.data['organization']):

						try:
							Role.objects.get(id = requests.data['role_id']).delete()

							return Response(status = status.HTTP_200_OK)

						except:
							return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

				return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)



class ServiceAPIView(ViewSet):
	serializer_class = ServiceSerializer

	def list_all_service(self, requests):
		if check_authHeader(requests):
			try:
				all_service = Service.objects.all()
				serializer = self.serializer_class(all_service, many = True)

				return Response(serializer.data, status = status.HTTP_200_OK)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def list_organization_services(self, requests, org_id):
		if check_authHeader(requests):
			try:
				all_service = Service.objects.filter(organization = org_id)
				serializer = self.serializer_class(all_service, many = True)

				return Response(serializer.data, status = status.HTTP_200_OK)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def create_service(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Service-POST', 'Service-GURU']):
					serializer = self.serializer_class.ServiceCSerializer(data = requests.data)
					if serializer.is_valid():
						serializer.save()

						return Response(status = status.HTTP_200_OK)

					else:
						return Response(status = status.HTTP_400_BAD_REQUEST)
				else:
					return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def update_service(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Service-PATCH', 'Service-GURU']):
					if check_orgService(requests.data['service_id'], requests.data['organization']):

						current_service = Service.objects.get(id = requests.data['service_id'])

						output = {
							'success':{},
							'error':{}
						}

						if 'new_name' in requests.data:
							if 10 <= len(requests.data['new_name']) <= 150:
								current_service.name = requests.data['new_name']
								output['success']['Name'] = 'Name successfully changed'

							else:
								output['error']['Name'] = 'Name is too short or too long'

						if 'number' in requests.data:
							try:
								current_service.number = requests.data['number']
								output['success']['Number'] = 'Number successfully changed'
							except:
								output['error']['Number'] = 'Wrong format of number'

						if 'address' in requests.data:
							if 10 <= requests.data['address'] <= 200:
								current_service.address = requests.data['address']
								output['success']['Address'] = 'Address successfully changed'

							else:
								output['error']['Address'] = 'Address too long or too short'

						if len(output['success']) > 0:
							current_service.save()

						return Response(output, status = status.HTTP_200_OK)

						return Response(status = status.HTTP_200_OK)

				return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def delete_organization_member(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-CREATOR', 'Service-DELETE', 'Service-GURU']):
					if check_orgMember(requests.data['service_id'], requests.data['organization']):

						try:
							Service.objects.get(id = requests.data['service_id']).delete()

							return Response(status = status.HTTP_200_OK)

						except:
							return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

				return Response(status = status.HTTP_403_FORBIDDEN)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)