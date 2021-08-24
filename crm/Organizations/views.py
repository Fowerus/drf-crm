import jwt

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework import status, permissions
from rest_framework.response import Response

from .serializers import *
from crm.views import *
from Clients.serializers import ClientSerializer



class OrganizationAPIView(APIView):
	serializer_class = OrganizationSerializer

	def get(self, requests):
		try:
			all_organizations = Organization.objects.all()
			serializer = self.serializer_class(all_organizations, many = True)	

			return Response(serializer.data, status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)



	def post(self, requests):
		user_data = get_userData(requests)
		if not check_UsrClient(user_data['user_id']) and not check_confirmed(user_data['user_id']):
			serializer = self.serializer_class.OrganizationCSerializer(data = requests.data)
			if serializer.is_valid():
				serializer.save()

				return Response(serialzier.data, status = status.HTTP_201_CREATE)

			else:
				return Response(status = status.HTTP_400_BAD_REQUEST)
		else:
			return Response(status = status.HTTP_403_FORBIDDEN)



	def patch(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'organization_change']):

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



	def delete(self, requests):
		user_data = get_userData(requests)
		if is_valid_member(user_data['user_id'], requests.data['organization'],
			['organization_creator', 'organization_delete']):
			try:
				Organization.objects.get(id = requests.data['organization']).delete()

				return Response(status = status.HTTP_200_OK)

			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		else:
			return Response(status = status.HTTP_403_FORBIDDEN)




class Organization_numberViewSet(ViewSet):
	serializer_class = Organization_numberSerializer

	def list_organizations_numbers(self, requests):
		try:
			all_organization_number = Organization_number.objects.all()
			serializer = self.serializer_class(all_organization_number, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)



	def list_organization_numbers(self, requests, org_id):
		try:
			all_organization_number = Organization_number.objects.filter(id = org_id)
		except:
			return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		serializer = self.serializer_class(all_organization_number, many = True)

		return Response(serializer.data, status = status.HTTP_200_OK)



	def create_organization_number(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'organization_number_create', 'organization_number_guru']):
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



	def update_organization_number(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'organization_number_change', 'organization_number_guru']):
				if check_orgNumber(requests.data['number'], requests.data['organization']):
					current_number = Organization_number.objects.get(id = requests.data['number'])

					try:
						current_number.number = requests.data['new_number']
						current_number.save()
						return Response(status = status.HTTP_200_OK)

					except:
						return Response({'error':'Bad new number'}, status = status.HTTP_400_BAD_REQUEST)

			return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



	def delete_organization_number(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'organization_number_delete', 'organization_number_guru']):
				if check_orgNumber(requests.data['number'], requests.data['organization']):

					try:
						Organization_number.objects.get(id = requests.data['number']).delete()

						return Response(status = status.HTTP_200_OK)

					except:
						return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



class Organization_linkViewSet(ViewSet):
	serializer_class = Organization_linkSerializer

	def list_organizations_links(self, requests):
		try:
			all_organization_link = Organization_link.objects.all()
			serializer = self.serializer_class(all_organization_link, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)



	def list_organization_links(self, requests, org_id):
		try:
			all_organization_link = Organization_link.objects.filter(id = org_id)
			serializer = self.serializer_class(all_organization_link, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)



	def create_organization_link(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'organization_link_create', 'organization_link_guru']):
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



	def update_organization_link(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'organization_link_change', 'organization_link_guru']):
				if check_orgLink(requests.data['link'], requests.data['organization']):
					current_number = Organization_number.objects.get(id = requests.data['link'])

					try:
						current_number.number = requests.data['new_link']
						current_number.save()

						return Response(status = status.HTTP_200_OK)

					except:
						return Response({'error':'Bad new link'}, status = status.HTTP_400_BAD_REQUEST)

			return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



	def delete_organization_link(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'organization_number_delete', 'organization_number_guru']):
				if check_orgLink(requests.data['link'], requests.data['organization']):

					try:
						Organization_link.objects.get(id = requests.data['link']).delete()

						return Response(status = status.HTTP_200_OK)

					except:
						return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



class Organization_memberViewSet(ViewSet):
	serializer_class = Organization_memberSerializer

	def list_all_organizations_members(self, requests):
		try:
			all_organization_members = Organization_member.objects.all()
			serializer = self.serializer_class(all_organization_members, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)



	def list_organization_members(self, requests, org_id):
		try:
			all_organization_members = Organization_member.objects.filter(organization = org_id)
			serializer = self.serializer_class(all_organization_members, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)



	def create_organization_member(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'], 
				['organization_creator', 'organization_member_create', 'organization_member_guru']):
				if Organization.objects.get(id = requests.data['organization']).creator.id == requests.data['user'] and not check_UsrClient(requests.data['user']) and check_confirmed(requests.data['client']):
					serializer = self.serializer_class.Organization_memberCSerializer(data = requests.data)
					if serializer.is_valid():
						serializer.save()

						return Response(status = status.HTTP_200_OK)

				return Response(status = status.HTTP_400_BAD_REQUEST)
			else:
				return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



	def update_organization_member(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'organization_member_change', 'organization_member_guru']):
				if check_orgMember(requests.data['user'], requests.data['organization']):

					try:
						current_member = Organization_member.objects.get(id = requests.data['user'])
						current_member.role = requests.data['new_role']
						current_member.save()

						return Response(status = status.HTTP_200_OK)

					except:
						return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



	def delete_organization_member(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'organization_member_delete', 'organization_member_guru']):
				if check_orgMember(requests.data['member'], requests.data['organization']):

					try:
						Organization_member.objects.get(id = requests.data['member']).delete()

						return Response(status = status.HTTP_200_OK)

					except:
						return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



class RolePermViewSet(ViewSet):
	serializer_class = RoleSerializer

	def list_permissions(self, requests, org_id):
		user_data = get_userData(requests)
		if is_valid_member(user_data['user_id'], org_id, ['organization_creator', 'role_create', 'role_guru']):
			try:
				all_permissions = CustomPermission.objects.all()
				serializer = PermissionSerializer(all_permissions, many = True)

				return Response(serializer.data, status = status.HTTP_200_OK)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status = status.HTTP_403_FORBIDDEN)



	def list_roles(self, requests, org_id):
		user_data = get_userData(requests)
		if is_valid_member(user_data['user_id'], org_id, ['organization_creator', 'role_view', 'role_guru']):
			try:
				all_role = Role.objects.filter(organization = org_id)
				serializer = self.serializer_class(all_role, many = True)

				return Response(serializer.data, status = status.HTTP_200_OK)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status = status.HTTP_403_FORBIDDEN)



	def create_role(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'role_create', 'role-_guru']):
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



	def update_role(self, requests):
		user_data = get_userData(requests)

		try:

			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'role_change', 'role_guru']):
				if check_orgRole(requests.data['role'], requests.data['organization']):
					current_role = Role.objects.get(id = requests.data['role'])

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



	def delete_role(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'role_delete', 'role_guru']):
				if check_orgRole(requests.data['role'], requests.data['organization']):

					try:
						Role.objects.get(id = requests.data['role']).delete()

						return Response(status = status.HTTP_200_OK)

					except:
						return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)




class ServiceViewSet(ViewSet):
	serializer_class = ServiceSerializer

	def list_all_service(self, requests):
		try:
			all_service = Service.objects.all()
			serializer = self.serializer_class(all_service, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)



	def list_organization_services(self, requests, org_id):
		try:
			all_service = Service.objects.filter(organization = org_id)
			serializer = self.serializer_class(all_service, many = True)

			return Response(serializer.data, status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)



	def create_service(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'service_create', 'service_guru']):
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



	def update_service(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'service_change', 'service_guru']):
				if check_orgService(requests.data['service'], requests.data['organization']):

					current_service = Service.objects.get(id = requests.data['service'])

					output = {
						'success':{},
						'error':{}
					}

					if 'new_name' in requests.data:
						if 10 <= len(requests.data['name']) <= 150:
							current_service.name = requests.data['name']
							output['success']['Name'] = 'Name successfully changed'

						else:
							output['error']['Name'] = 'Name is too short or too long'

					if 'number' in requests.data:
						try:
							current_service.number = requests.data['number']
							output['success']['Number'] = 'Number successfully changed'
						except:
							output['error']['Number'] = "Wrong number's format"

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



	def delete_service(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'service_delete', 'service_guru']):
				if check_orgMember(requests.data['service'], requests.data['organization']):

					try:
						Service.objects.get(id = requests.data['service']).delete()

						return Response(status = status.HTTP_200_OK)

					except:
						return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



class ClientViewSet(ViewSet):
	serializer_class = ClientSerializer

	def list_clients(self, requests, org_id):
		user_data = get_userData(requests)

		if is_valid_member(user_data['user_id'], org_id,
			['organization_creator', 'client_view', 'client_guru']):
			try:
				all_clients = Organization.objects.get(id = org_id)
				serializer = self.serializer_class(all_clients, many = True)

				return Response(serializer.data, status = HTTP_200_OK)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_403_FORBIDDEN)



	def create_client(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'], 
				['organization_creator', 'client_create', 'client_guru']):
				serializer = self.serializer_class.ClientCSerializer(data = requests.data)
				if serializer.is_valid():
					serializer.save()

					return Response(status = status.HTTP_200_OK)

				return Response(status = status.HTTP_400_BAD_REQUEST)
			else:
				return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



	def update_client(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'], 
				['organization_creator', 'client_change', 'client_guru']):
				if check_orgClient(requests.data['client'], requests.data['organization']):

					current_client = Client.objects.get(id = requests.data['client'])

					output = {
						"success":{},
						"error":{}
					}

					if 'surname' in requests.data:
						if 10 <= len(requests.data['surname']) <= 150:
							current_client.user.surname = requests.data['surname']
							output['success']['Surname'] = 'Surname successfully changed'
						else:
							output['error']['Surname'] = 'Surname is too short or too long'

					if 'name' in requests.data:
						if 10 <= len(requests.data['name']) <= 150:
							current_client.user.name = requests.data['name']
							output['success']['Name'] = 'Name successfully changed'
						else:
							output['error']['Name'] = 'Name is too short or too long'

					if 'patronymic' in requests.data:
						if 10 <= len(requests.data['patronymic']) <= 150:
							current_client.user.patronymic = requests.data['patronymic']
							output['success']['Patronymic'] = 'Patronymic successfully changed'
						else:
							output['error']['Patronymic'] = 'Patronymic is too short or too long'

					if 'address' in requests.data:
						if 10 <= len(requests.data['address']) <= 150:
							current_client.user.address = requests.data['address']
							output['success']['Address'] = 'Address successfully changed'
						else:
							output['error']['Address'] = 'Address is too short or too long'

					if 'email' in requests.data:
						try:
							current_client.user.email = requests.data['email']
							output['success']['Email'] = 'Email successfully changed'
							current_client.user.confirmed_email = False
						except:
							output['error']['Email'] = 'Wrong email format'


					if 'number' in requests.data:
						try:
							current_client.user.email = requests.data['number']
							output['success']['Number'] = 'Number successfully changed'
							current_client.user.confirmed_number = False
						except:
							output['error']['Number'] = 'Wrong number format'


					if len(output['success'] > 0):
						current_client.save()

					return Response(output, status = status.HTTP_200_OK)

				return Response(status = status.HTTP_400_BAD_REQUEST)
			else:
				return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



	def delete_client(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'client_delete', 'client_guru']):
				if check_orgClient(requests.data['client'], requests.data['organization']):

					try:
						Client.objects.get(id = requests.data['client']).delete()

						return Response(status = status.HTTP_200_OK)

					except:
						return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



class OrderViewSet(ViewSet):
	serializer_class = OrderSerializer

	def list_orders(self, requests, org_id):
		user_data = get_userData(requests)

		if is_valid_member(user_data['user_id'], org_id,
			['organization_creator', 'order_view', 'order_guru']):
			try:
				all_orders = Orders.objects.get(id = org_id)
				serializer = self.serializer_class(all_orders, many = True)

				return Response(serializer.data, status = HTTP_200_OK)

			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_403_FORBIDDEN)



	def create_order(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'], 
				['organization_creator', 'order_create', 'order_guru']) and check_confirmed(requests.data['executor']):
				serializer = self.serializer_class.OrderCSerializer(data = requests.data)
				if serializer.is_valid():
					serializer.save()

					return Response(status = status.HTTP_200_OK)

				return Response(status = status.HTTP_400_BAD_REQUEST)
			else:
				return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



	def update_order(self, requests):
		user_data = get_userData(requests)

		try:

			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'order_change', 'order_guru']):
				if check_orgOrder(requests.data['order_code'], requests.data['organization']):
					current_order = Order.objects.get(order_code = requests.data['order_code'])

					output = {
						'success':{},
						'error':{}
					}

					if 'description' in requests.data:
						if 10 <= len(requests.data['description']) <= 500:
							current_order.description = requests.data['description']
							output['success']['Description'] = 'Description successfully changed'
						else:
							output['error']['Description'] = 'Description is too short or too long'

					if 'executor' in requests.data:
						try:
							if not check_UsrClient(requests.data['executor']):
								current_order.executor = requests.data['executor']
								output['success']['Executor'] = 'Executor successfully changed'
							else:
								output['error']['Executor'] = 'Wrong executor'
						except:
							output['error']['Executor'] = 'Wrong executor'

					if 'service' in requests.data:
						try:
							if check_orgService(requests.data['service'], requests.data['organization']):
								current_order.executor = requests.data['service']
								output['success']['Service'] = 'Service successfully changed'
							else:
								output['error']['Service'] = 'Wrong service'
						except:
							output['error']['Service'] = 'Wrong service'


					if len(output['success']) > 0:
						current_order.save()

					return Response(output, status = status.HTTP_200_OK)


			return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



	def delete_order(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'order_delete', 'order_guru']):
				if check_orgOrder(requests.data['order_code'], requests.data['organization']):

					try:
						Order.objects.get(order_code = requests.data['order_code']).delete()

						return Response(status = status.HTTP_200_OK)

					except:
						return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)



	def block_order(self, requests):
		user_data = get_userData(requests)

		try:
			if is_valid_member(user_data['user_id'], requests.data['organization'],
				['organization_creator', 'order_delete', 'order_guru']):
				if check_orgOrder(requests.data['order_code'], requests.data['organization']):

					try:
						current_order = Order.objects.get(order_code = requests.data['order_code'])
						current_order.blocked = True
						current_order.save()

						return Response(status = status.HTTP_200_OK)

					except:
						return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

			return Response(status = status.HTTP_403_FORBIDDEN)

		except:
			return Response(status = status.HTTP_400_BAD_REQUEST)