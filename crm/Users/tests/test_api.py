from django.contrib.auth import get_user_model
from django.core import validators
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

from Users.models import User
from Organizations.models import *
from Clients.models import *
from Sessions.models import *



class TestUsersAPI(APITestCase):

	def testAuthRegistration(self):

		url = reverse('registration')

		#by email
		data_by_email = {
			'surname':'Landa',
			'name':'Hans',
			'patronymic':'maybe_not',
			'address':'Austria',
			'email':'tarantino_the_best@gmail.com',
			'password':'1995landa'
		}
		response_email = self.client.post(url, data = data_by_email)
		data_by_email.pop('password')

		self.assertEquals(response_email.status_code, status.HTTP_201_CREATED)
		self.assertEquals(response_email.data, data_by_email)

		#by number
		data_by_number = {
			'surname':'Landa',
			'name':'Hans',
			'patronymic':'maybe_not',
			'address':'Austria',
			'number':'+79996348628',
			'password':'1995landa'
		}
		response_number = self.client.post(url, data = data_by_number)
		data_by_number.pop('password')

		self.assertEquals(response_number.status_code, status.HTTP_201_CREATED)
		self.assertEquals(response_number.data, data_by_number)

		#by all
		data_by_all = {
			'surname':'Landa',
			'name':'Hans',
			'patronymic':'maybe_not',
			'address':'Austria',
			'number':'+79966148628',
			'email':'tarantino_uhe_best@gmail.com',
			'password':'1995landa'
		}
		response_all = self.client.post(url, data = data_by_all)
		data_by_all.pop('password')

		self.assertEquals(response_all.status_code, status.HTTP_201_CREATED)
		self.assertEquals(response_all.data, data_by_all)


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

		self.user_data2 = {
			'surname':'Landa',
			'name':'Hans',
			'patronymic':'maybe_not',
			'address':'Austria',
			'number':'+79132488720',
			'email':'tarantino_tthe_best9809801@gmail.com',
		}

		self.user2 = User(id = 1001, **self.user_data2)
		self.user2.set_password('1995landa')
		self.user2.save()

		self.response = self.client.post(
			reverse('token_obtain_pair'), 
			data = {'number':'+79132488720', 'password':'1995landa'},
			HTTP_USER_AGENT = 'Firefox/47.3 Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4')

		self.access = self.response.data['access']


	def testAuthToken_AuthTokenRefresh(self):

		url_obtain = reverse('token_obtain_pair')
		user_agent = [
			'Mozilla: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101',
			'Firefox/47.3 Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4',
		]

		#by number
		data_number = {
			'number':self.user_data['number'],
			'password':'1995landa'
		}
		response_number = self.client.post(url_obtain, data = data_number, HTTP_USER_AGENT = user_agent[0])

		self.assertEquals(response_number.status_code, status.HTTP_200_OK)
		self.assertTrue('access' in response_number.data)
		self.assertTrue('refresh' in response_number.data)
		self.assertTrue('expired_at' in response_number.data)

		#by email
		data_email = {
			'email':self.user_data['email'],
			'password':'1995landa'
		}
		response_email = self.client.post(url_obtain, data = data_email, HTTP_USER_AGENT = user_agent[1])

		self.assertEquals(response_email.status_code, status.HTTP_200_OK)
		self.assertTrue('access' in response_email.data)
		self.assertTrue('refresh' in response_email.data)
		self.assertTrue('expired_at' in response_email.data)

		#check refresh
		url_refresh = reverse('token_refresh')
		refresh = response_email.data['refresh']

		data_refresh = {
			'refresh': refresh
		}
		response_refresh = self.client.post(url_refresh, data = data_refresh, HTTP_USER_AGENT = user_agent[1])

		self.assertEquals(response_refresh.status_code, status.HTTP_200_OK)
		self.assertTrue('access' in response_refresh.data)
		self.assertTrue('refresh' in response_refresh.data)
		self.assertTrue('expired_at' in response_refresh.data)


	def testUser(self):
		url = reverse('user')
		access = f'Bearer {self.access}'

		#GET
		#Within token
		response_get = self.client.get(url)
		self.assertEquals(response_get.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_get = self.client.get(url, HTTP_AUTHORIZATION = access)
		fields = ['id', 'surname', 'name', 'patronymic', 'address', 'email', 'image','confirmed_email', 'confirmed_number', 'created_at', 'updated_at']

		self.assertEquals(response_get.status_code, status.HTTP_200_OK)
		self.assertEquals(set(response_get.data.keys()), set(fields))

		#PATCH
		data_patch = {
			'surname':'LandaChange',
			'name':'HansChange',
			'patronymic':'maybe_notChange',
			'address':'AustriaChange',
			'number':'+79133248721',
			'email':'tarantino_tthe_bestChange@gmail.com',
			'password':'199landaChange',
			'image':'/user/photo/check/' 
		}

		#Within token
		response_patch = self.client.patch(url, data = data_patch)
		self.assertEquals(response_patch.status_code, status.HTTP_401_UNAUTHORIZED)

		#With tokne
		response_patch = self.client.patch(url, data = data_patch, HTTP_AUTHORIZATION = access)

		self.assertEquals(response_patch.status_code, status.HTTP_200_OK)
		self.assertEquals(len(response_patch.data['success'].keys()), len(data_patch.keys()))

		#DELETE
		#Within token
		response_delete = self.client.delete(url)
		self.assertEquals(response_delete.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_delete = self.client.delete(url, HTTP_AUTHORIZATION = access)
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