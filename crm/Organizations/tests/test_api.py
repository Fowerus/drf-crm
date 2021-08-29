from django.contrib.auth import get_user_model
from django.core import validators
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

from Organizations.models import *
from Users.models import User
from Sessions.models import Session
from Clients.models import Client



class TestOrganizationsAPI(APITestCase):

	def setUp(self):
		self.user_data = {
			'surname':'Landa',
			'name':'Hans',
			'patronymic':'maybe_not',
			'address':'Austria',
			'number':'+79968148328',
			'email':'tarantino_tthe_best22222@gmail.com',
		}

		self.user = User(id = 1000, **self.user_data)
		self.user.set_password('1995landa')
		self.user.confirmed_email = True
		self.user.confirmed_number = True
		self.user.save()

		self.user2 = User(id = 1001, **self.user_data)
		self.user2.email = 'tarantino_tthe_best3@gmail.com'
		self.user2.number = '+79996248729'
		self.user2.set_password('1995landa')
		self.user2.confirmed_email = True
		self.user2.confirmed_number = True
		self.user2.save()

		self.user3 = User(id = 1002, **self.user_data)
		self.user3.email = 'tarantino_tthe_best4@gmail.com'
		self.user3.number = '+79996248720'
		self.user3.set_password('1995landa')
		self.user3.confirmed_email = True
		self.user3.confirmed_number = True
		self.user3.save()

		self.user4 = User(id = 1003, **self.user_data)
		self.user4.email = 'tarantino3_tthe_best@gmail.com'
		self.user4.number = '+79996142720'
		self.user4.set_password('1995landa')
		self.user4.confirmed_email = True
		self.user4.confirmed_number = True
		self.user4.save()


		self.response = self.client.post(
			reverse('token_obtain_pair'), 
			data = {'number':'+79968148328', 'password':'1995landa'},
			HTTP_USER_AGENT = 'Firefox/47.3 Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4')

		self.access = self.response.data['access']

		self.organization_data = {
			'name':'Test', 
			'description':'Test',
			'address':'Test_address',
			'creator': self.user
		}
		self.organization = Organization.objects.create(id = 1000, **self.organization_data)

		self.organization_number_data = {
			'number':'+79995392710',
			'organization':self.organization
		}
		self.organization_number = Organization_number.objects.create(id = 1000, **self.organization_number_data)

		self.organization_link_data = {
			'name':'vk',
			'link':'https://vk.com',
			'organization':self.organization
		}
		self.organization_link = Organization_link.objects.create(id = 1000, **self.organization_link_data)

		self.custom_permission = CustomPermission.objects.create(id = 1000, name = 'Can add role', codename = 'role_create')
		self.custom_permission2 = CustomPermission.objects.create(id = 1001, name = 'Can view perm', codename = 'role_guru')

		self.role_data = {
			'name':'Main role',
			'organization': self.organization
		}
		self.role = Role(id = 1000, **self.role_data)
		self.role.name = 'Main role 2'
		self.role.permissions.set({self.custom_permission})
		self.role.save()

		self.role2 = Role(id = 1001, **self.role_data)
		self.role2.permissions.set({self.custom_permission})
		self.role2.save()

		self.organization_member_data = {
			'user':self.user2,
			'role':self.role,
			'organization':self.organization
		}
		self.organization_member = Organization_member.objects.create(id = 1000, **self.organization_member_data)

		self.service_data = {
			'name':'TestService',
			'number':'+79518373619',
			'address':'test_address',
			'organization':self.organization
		}
		self.service = Service.objects.create(id = 1000, **self.service_data)
		self.service2 = Service(id = 1001, **self.service_data)
		self.service2.name = 'TestService2'
		self.service2.number = '+79518373610'
		self.service2.save()

		self.my_client = Client.objects.create(id = 1000, user = self.user3, organization = self.organization)



	def testOrganization(self):
		url = reverse('organization')
		access = f'Bearer {self.access}'

		#GET
		#Within token
		response_get = self.client.get(url)
		self.assertEquals(response_get.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_get = self.client.get(url, HTTP_AUTHORIZATION = access)

		self.assertEquals(response_get.status_code, status.HTTP_200_OK)
		self.assertTrue(set(self.organization_data.keys()) <= set(response_get.data[0].keys()))

		#POST
		data_post = self.organization_data
		data_post['name'] = 'Test 2 organization'
		data_check = data_post
		data_check['creator'] = data_post['creator'].id

		#Within token
		response_post = self.client.post(url, data = data_post)
		self.assertEquals(response_post.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_post = self.client.post(url, data = data_post, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_post.status_code, status.HTTP_201_CREATED)
		self.assertEquals(response_post.data, data_check)

		#PATCH
		data_patch = {
			'name':'TestChanged', 
			'description':'TestChanged',
			'address':'TestChanged',
			'organization':self.organization.id
		}
		data_check = dict(data_patch)
		data_check.pop('organization')

		#Within token
		response_patch = self.client.patch(url, data = data_patch)
		self.assertEquals(response_patch.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_patch = self.client.patch(url, data = data_patch, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_patch.status_code, status.HTTP_200_OK)
		self.assertEquals(len(response_patch.data['success'].keys()), len(data_check.keys()))

		#DELETE
		#Within token
		data_delete = {
			'organization':self.organization.id
		}
		response_delete = self.client.delete(url, data = data_delete)
		self.assertEquals(response_delete.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_delete = self.client.delete(url, data = data_delete, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_delete.status_code, status.HTTP_200_OK)


	def testNumber(self):
		url = reverse('organization_number')
		access = f'Bearer {self.access}'

		#GET
		#WIthin token
		response_get = self.client.get(url)
		self.assertEquals(response_get.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_get = self.client.get(url, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_get.status_code, status.HTTP_200_OK)
		self.assertEquals(response_get.data[0]['organization']['id'], self.organization_number_data['organization'].id)
		self.assertEquals(response_get.data[0]['number'], self.organization_number_data['number'])

		#POST
		data_post = {
			'number':'+79968472184',
			'organization':self.organization.id
		}
		#Within token
		response_post = self.client.post(url, data = data_post)
		self.assertEquals(response_post.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_post = self.client.post(url, data = data_post, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_post.status_code, status.HTTP_201_CREATED)
		self.assertEquals(response_post.data, data_post)

		#PATCH
		data_patch = {
			'number':self.organization_number.id,
			'new_number':'+79969473184',
			'organization':self.organization.id
		}
		#Within token
		response_patch = self.client.patch(url, data = data_patch)
		self.assertEquals(response_patch.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_patch = self.client.patch(url, data = data_patch, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_patch.status_code, status.HTTP_200_OK)
		self.assertTrue('success' in response_patch.data)

		#DELETE
		data_delete = {
			'number':self.organization_number.id,
			'organization':self.organization.id
		}
		#Within token
		response_delete = self.client.delete(url, data = data_delete)
		self.assertEquals(response_delete.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_delete = self.client.delete(url, data = data_delete, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_delete.status_code, status.HTTP_200_OK)


	def testLink(self):
		url = reverse('organization_link')
		access = f'Bearer {self.access}'

		#GET
		#WIthin token
		response_get = self.client.get(url)
		self.assertEquals(response_get.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_get = self.client.get(url, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_get.status_code, status.HTTP_200_OK)
		self.assertEquals(response_get.data[0]['organization']['id'], self.organization_link_data['organization'].id)
		self.assertEquals(response_get.data[0]['link'], self.organization_link_data['link'])
		self.assertEquals(response_get.data[0]['name'], self.organization_link_data['name'])

		#POST
		data_post = {
			'name':'hmhm',
			'link':'http://instagram.com',
			'organization':self.organization.id
		}
		#Within token
		response_post = self.client.post(url, data = data_post)
		self.assertEquals(response_post.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_post = self.client.post(url, data = data_post, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_post.status_code, status.HTTP_201_CREATED)
		self.assertEquals(response_post.data, data_post)

		#PATCH
		data_patch = {
			'link':self.organization_link.id,
			'new_link':'http://facebook.com',
			'organization':self.organization.id
		}
		#Within token
		response_patch = self.client.patch(url, data = data_patch)
		self.assertEquals(response_patch.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_patch = self.client.patch(url, data = data_patch, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_patch.status_code, status.HTTP_200_OK)
		self.assertTrue('success' in response_patch.data)

		#DELETE
		data_delete = {
			'link':self.organization_link.id,
			'organization':self.organization.id
		}
		#Within token
		response_delete = self.client.delete(url, data = data_delete)
		self.assertEquals(response_delete.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_delete = self.client.delete(url, data = data_delete, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_delete.status_code, status.HTTP_200_OK)


	def testMember(self):
		url = reverse('organization_member')
		access = f'Bearer {self.access}'

		#GET
		#Within token
		response_get = self.client.get(url)
		self.assertEquals(response_get.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_get = self.client.get(url, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_get.status_code, status.HTTP_200_OK)
		self.assertEquals(response_get.data[0]['user']['id'], self.user2.id)
		self.assertEquals(response_get.data[0]['role']['id'], self.role.id)
		self.assertEquals(response_get.data[0]['organization']['id'], self.organization.id)

		#POST
		data_post = {
			'user':self.user4.id,
			'role': self.role.id,
			'organization':self.organization.id
		}
		#Within token
		response_post = self.client.post(url, data = data_post)
		self.assertEquals(response_post.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_post = self.client.post(url, data = data_post, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_post.status_code, status.HTTP_201_CREATED)
		self.assertEquals(response_post.data, data_post)

		#PATCH
		data_patch = {
			'member':1,
			'role': self.role2.id,
			'organization':self.organization.id
		}
		#Within token
		response_patch = self.client.patch(url, data = data_patch)
		self.assertEquals(response_patch.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_patch = self.client.patch(url, data = data_patch, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_patch.status_code, status.HTTP_200_OK)
		self.assertTrue('success' in response_patch.data)

		#DELETE
		data_delete = {
			'member':1,
			'organization':self.organization.id
		}
		#Within token
		response_delete = self.client.delete(url, data = data_delete)
		self.assertEquals(response_delete.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_delete = self.client.delete(url, data = data_delete, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_delete.status_code, status.HTTP_200_OK)


	def testRole(self):
		url = reverse('organization_role')
		access = f'Bearer {self.access}'

		#POST
		data_post = {
			'name':'Test role',
			'permissions': [self.custom_permission.id],
			'organization':self.organization.id
		}
		#Within token
		response_post = self.client.post(url, data = data_post)
		self.assertEquals(response_post.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_post = self.client.post(url, data = data_post, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_post.status_code, status.HTTP_201_CREATED)
		self.assertEquals(response_post.data, data_post)

		#PATCH
		data_patch = {
			'role':self.role.id,
			'name':'Test roleChanged',
			'new_permissions': [self.custom_permission2.id],
			'organization':self.organization.id
		}
		#Within token
		response_patch = self.client.patch(url, data = data_patch)
		self.assertEquals(response_patch.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_patch = self.client.patch(url, data = data_patch, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_patch.status_code, status.HTTP_200_OK)
		self.assertEquals(len(response_patch.data['success'].keys()), 2)

		#DELETE
		data_delete = {
			'role':self.role.id,
			'organization':self.organization.id
		}
		#Within token
		response_delete = self.client.delete(url, data = data_delete)
		self.assertEquals(response_delete.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_delete = self.client.delete(url, data = data_delete, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_delete.status_code, status.HTTP_200_OK)


	def testService(self):
		url = reverse('organization_service')
		access = f'Bearer {self.access}'

		#GET
		#Within token
		response_get = self.client.get(url)
		self.assertEquals(response_get.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_get = self.client.get(url, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_get.status_code, status.HTTP_200_OK)
		self.assertEquals(response_get.data[0]['id'], self.service2.id)
		self.assertEquals(response_get.data[0]['organization']['id'], self.organization.id)

		#POST
		data_post = {
			'name':'Test_service_3',
			'number': '+79137593710',
			'address':'Test_address_2',
			'organization':self.organization.id
		}
		#Within token
		response_post = self.client.post(url, data = data_post)
		self.assertEquals(response_post.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_post = self.client.post(url, data = data_post, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_post.status_code, status.HTTP_201_CREATED)
		self.assertEquals(response_post.data, data_post)

		#PATCH
		data_patch = {
			'service':1,
			'name':'Test_serviceChanged',
			'number':'+79134725591',
			'address':'Test_address_Changed',
			'organization':self.organization.id
		}
		#Within token
		response_patch = self.client.patch(url, data = data_patch)
		self.assertEquals(response_patch.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_patch = self.client.patch(url, data = data_patch, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_patch.status_code, status.HTTP_200_OK)
		self.assertEquals(len(response_patch.data['success'].keys()), 3)

		#DELETE
		data_delete = {
			'service':self.service.id,
			'organization':self.organization.id
		}
		#Within token
		response_delete = self.client.delete(url, data = data_delete)
		self.assertEquals(response_delete.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_delete = self.client.delete(url, data = data_delete, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_delete.status_code, status.HTTP_200_OK)


	def testClient(self):
		url = reverse('organization_client')
		access = f'Bearer {self.access}'

		#POST
		data_post = {
			'surname':'Landa2',
			'name':'Hans2',
			'patronymic':'maybe_not2',
			'address':'Austria2',
			'number':'+79996248722',
			'email':'tarantino_tthe_best22@gmail.com',
			'password':'isclient1995',
			'organization':self.organization.id
		}
		#Within token
		response_post = self.client.post(url, data = data_post)
		self.assertEquals(response_post.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_post = self.client.post(url, data = data_post, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_post.status_code, status.HTTP_201_CREATED)
		self.assertEquals(response_post.data['organization'], data_post['organization'])

		#PATCH
		data_patch = {
			'surname':'Landa2Changed',
			'name':'Hans2Changed',
			'patronymic':'maybe_not2Changed',
			'address':'Austria2Changed',
			'number':'+7951643712',
			'email':'tarantino_tthe_best22Changed@gmail.com',
			'password':'isclient1995Changed',
			'image':'/to/here/',
			'organization':self.organization.id,
			'client':1
		}
		#Within token
		response_patch = self.client.patch(url, data = data_patch)
		self.assertEquals(response_patch.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_patch = self.client.patch(url, data = data_patch, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_patch.status_code, status.HTTP_200_OK)
		self.assertEquals(len(response_patch.data['success'].keys()), 8)

		#DELETE
		data_delete = {
			'client': 1,
			'organization':self.organization.id
		}
		#Within token
		response_delete = self.client.delete(url, data = data_delete)
		self.assertEquals(response_delete.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_delete = self.client.delete(url, data = data_delete, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_delete.status_code, status.HTTP_200_OK)


	def testOrder(self):
		url = reverse('organization_order')
		access = f'Bearer {self.access}'

		#POST
		data_post = {
			'description':'just do it sdfdsfdsf',
			'client':self.my_client.id,
			'executor':self.user3.id,
			'creator':self.user.id,
			'service':self.service.id,
			'organization':self.organization.id
		}
		#Within token
		response_post = self.client.post(url, data = data_post)
		self.assertEquals(response_post.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_post = self.client.post(url, data = data_post, HTTP_AUTHORIZATION = access)
		data_post.pop('organization')
		self.assertEquals(response_post.status_code, status.HTTP_201_CREATED)
		self.assertEquals(response_post.data, data_post)
		#PATCH
		data_patch = {
			'organization':self.organization.id,
			'description':'Changed kdsjfdsfds',
			'executor':self.user4.id,
			'service':self.service2.id
		}
		#Within token
		response_patch = self.client.patch(url, data = data_patch)
		self.assertEquals(response_patch.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_patch = self.client.patch(url, data = data_patch, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_patch.status_code, status.HTTP_200_OK)
		self.assertEquals(len(response_patch.data['success'].keys()), 3)

		#POST-blocked_order
		url_blocked = reverse('block_order')
		data_blocked = {
			'order_code':132343,
			'organization':self.organization.id
		}
		#Within tokne
		response_blocked = self.client.post(url_blocked, data = data_blocked)
		self.assertEquals(response_blocked.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_blocked = self.client.post(url_blocked, data = data_blocked, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_blocked.status_code, status.HTTP_200_OK)
		
		#DELETE
		data_delete = {
			'order_code': 132343,
			'organization':self.organization.id
		}
		#Within token
		response_delete = self.client.delete(url, data = data_delete)
		self.assertEquals(response_delete.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_delete = self.client.delete(url, data = data_delete, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_delete.status_code, status.HTTP_200_OK)


	def tearDown(self):
		Order.objects.all().delete()
		Client.objects.all().delete()
		Service.objects.all().delete()
		Organization_member.objects.all().delete()
		Role.objects.all().delete()
		CustomPermission.objects.all().delete()
		Organization_link.objects.all().delete()
		Organization_number.objects.all().delete()
		Organization.objects.all().delete()
		Session.objects.all().delete()
		get_user_model().objects.all().delete()