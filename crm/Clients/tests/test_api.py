from django.contrib.auth import get_user_model
from django.core import validators
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

from Users.models import User
from Sessions.models import Session
from Organizations.models import *
from Clients.models import Client



class TestClientsAPI(APITestCase):

	def setUp(self):
		self.user_data = {
			'surname':'Landa',
			'name':'Hans',
			'patronymic':'maybe_not',
			'address':'Austria',
			'number':'+79996248728',
			'email':'tarantino_tthe_best@gmail.com',
		}

		self.user = User(id = 1000, **self.user_data)
		self.user.set_password('1995landa')
		self.user.confirmed_email = True
		self.user.confirmed_number = True
		self.user.save()

		self.user2 = User(id = 1001, **self.user_data)
		self.user2.email = 'tarantino_tthe_best2@gmail.com'
		self.user2.number = '+79996248729'
		self.user2.set_password('1995landa')
		self.user2.confirmed_email = True
		self.user2.confirmed_number = True
		self.user2.save()

		self.user3 = User(id = 1002, **self.user_data)
		self.user3.email = 'tarantino_tthe_best3@gmail.com'
		self.user3.number = '+79996248720'
		self.user3.set_password('1995landa')
		self.user3.confirmed_email = True
		self.user3.confirmed_number = True
		self.user3.save()

		self.response = self.client.post(
			reverse('token_obtain_pair'),
			data = {'number':self.user3.number.raw_input, 'password':'1995landa'},
			HTTP_USER_AGENT = 'Firefox/47.3 Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4')

		self.access = self.response.data['access']

		self.organization_data = {
			'name':'Test', 
			'description':'Test',
			'address':'Test_address',
			'creator': self.user
		}
		self.organization = Organization.objects.create(id = 1000, **self.organization_data)

		self.service_data = {
			'name':'TestService',
			'number':'+79518373619',
			'address':'test_address',
			'organization':self.organization
		}
		self.service = Service.objects.create(id = 1000, **self.service_data)

		self.my_client = Client.objects.create(id = 1000, user = self.user3, organization = self.organization)

		self.order_data = {
			'order_code':12343,
			'description':'wefredef',
			'client':self.user3,
			'executor':self.user2,
			'creator':self.user,
			'service':self.service
		}
		self.order = Order.objects.create(id = 1000, **self.order_data)



	def testClient(self):
		url = reverse('client')
		access = f'Bearer {self.access}'

		#GET
		#Within token
		response_get = self.client.get(url)
		self.assertEquals(response_get.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_get = self.client.get(url, HTTP_AUTHORIZATION = access)

		self.assertEquals(response_get.status_code, status.HTTP_200_OK)
		self.assertEquals(response_get.data[0]['client'], self.user3.id)
		self.assertEquals(response_get.data[0]['executor']['id'], self.user2.id)
		self.assertEquals(response_get.data[0]['creator']['id'], self.user.id)
		self.assertEquals(response_get.data[0]['service']['id'], self.service.id)

		#PATCH
		data_patch = {
			'surname':'LandaChange',
			'name':'HansChange',
			'patronymic':'maybe_notChange',
			'address':'AustriaChange',
			'number':'+79996248720',
			'email':'tarantino_tthe_bestChange@gmail.com',
			'password':'199landaChange',
			'image':'/user/photo/check/' 
		}
		#Within token
		response_patch = self.client.patch(url, data = data_patch)
		self.assertEquals(response_patch.status_code, status.HTTP_401_UNAUTHORIZED)

		response_patch = self.client.patch(url, data = data_patch, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_patch.status_code, status.HTTP_200_OK)
		self.assertEquals(len(response_patch.data['success'].keys()), len(data_patch.keys()))


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