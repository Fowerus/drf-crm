import jwt
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response

from .serializers import *
from crm.views import *
# {
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwNDE1OTI0LCJqdGkiOiJmYWRlOTkxZjNjYmU0ZWVkOWFkM2E0NzdmNzljOTAxNCIsInVzZXJfaWQiOjJ9.0ZQGq57AOHoy6CocQ4nxQ7pU7mvvvnZ25tyMlQeNgE4",
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyOTM3OTEyNCwianRpIjoiMjM0N2ZlZjE5YjIwNGRiNDk3ZmM4Y2NhNGY4YWQwNzYiLCJ1c2VyX2lkIjoyfQ.1WY1IZ0aZyFqm7NF51KmreU0htLpNI_IJa72wxENfMo",
#     "expire": 0
# }


class OrganizationAPIView(APIView):
	serializer_class = OrganizationSerializer

	def get(self, requests):
		if check_authHeader(requests):
			try:
				all_organizations = Organization.objects.all()
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			serializer = self.serializer_class(all_organizations, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

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
			if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-PATCH', 'Organization-CREATOR']):
				try:
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
				except:
					return Response(status = status.HTTP_400_BAD_REQUEST)
				
			else:
				return Response(status = status.HTTP_403_FORBIDDEN)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def delete(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)
			if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization-DELETE', 'Organization-CREATOR']):
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
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			serializer = self.serializer_class(all_organization_number, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

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
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization_number-POST', 'Organization-CREATOR', 'Organization_number-GURU']):
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
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization_number-PATCH', 'Organization-CREATOR', 'Organization_number-GURU']):
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
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization_number-DELETE', 'Organization-CREATOR', 'Organization_number-GURU']):
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
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			serializer = self.serializer_class(all_organization_link, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def list_organization_links(self, requests, org_id):
		if check_authHeader(requests):
			try:
				all_organization_link = Organization_link.objects.filter(id = org_id)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			serializer = self.serializer_class(all_organization_link, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def create_organization_link(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization_link-POST', 'Organization-CREATOR', 'Organization_link-GURU']):
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
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization_link-PATCH', 'Organization-CREATOR', 'Organization_link-GURU']):
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
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization_number-DELETE', 'Organization-CREATOR', 'Organization_number-GURU']):
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
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			serializer = self.serializer_class(all_organization_members, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def list_organization_members(self, requests, org_id):
		if check_authHeader(requests):
			try:
				all_organization_members = Organization_member.objects.filter(organization = org_id)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			serializer = self.serializer_class(all_organization_members, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def create_organization_member(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization_member-POST', 'Organization-CREATOR', 'Organization_member-GURU']):
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
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization_member-PATCH', 'Organization-CREATOR', 'Organization_member-GURU']):
					if check_memOrg(requests.data['member_id'], requests.data['organization']):

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
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Organization_member-DELETE', 'Organization-CREATOR', 'Organization_member-GURU']):
					if check_memOrg(requests.data['member_id'], requests.data['organization']):

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
			if is_valid_member(user_data['user_id'], org_id, ['Organization-CREATOR', 'Role-GURU', 'Role-POST']):
				try:
					all_permissions = Permission.objects.all()
				except:
					return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

				serializer = PermissionSerializer(all_permissions, many = True)

				return Response(serializer.data, status = status.HTTP_200_OK)

			return Response(status = status.HTTP_403_FORBIDDEN)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def list_roles(self, requests, org_id):
		if check_authHeader(requests):
			user_data = get_userData(requests)
			if is_valid_member(user_data['user_id'], org_id, ['Organization-CREATOR', 'Role-GURU', 'Role-GET']):
				try:
					all_role = Role.objects.filter(organization = org_id)
				except:
					return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

				serializer = self.serializer_class(all_role, many = True)

				return Response(serializer.data, status = status.HTTP_200_OK)

			return Response(status = status.HTTP_403_FORBIDDEN)

		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def create_role(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)

			try:
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Role-POST', 'Organization-CREATOR', 'Role-GURU']):
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

				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Role-PATCH', 'Organization-CREATOR', 'Role-GURU']):
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
				if is_valid_member(user_data['user_id'], requests.data['organization'], ['Role-DELETE', 'Organization-CREATOR', 'Role-GURU']):
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