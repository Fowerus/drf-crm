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
		data_by_email['number'] = None

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

		print(response_number.errors)
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
		data = {
			'surname':'Landa',
			'name':'Hans',
			'patronymic':'maybe_not',
			'address':'Austria',
			'number':'+79996248728',
			'email':'tarantino_tthe_best@gmail.com',
		}

		self.user = User(id = 1000, **data)
		self.user.set_password('1995landa')
		self.user.save()


	def testAuthToken(self):

		url_obtain = reverse('token_obtain_pair')
		user_agent = [
			'Mozilla: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101',
			'Firefox/47.3 Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4',
		]

		#by email
		data_email = {
			'email':'tarantino_tthe_best@gmail.com',
			'password':'1995landa'
		}
		response_email = self.client.post(url_obtain, data = data_email, HTTP_USER_AGENT = user_agent[0])

		self.assertEquals(response_email.status_code, status.HTTP_200_OK)
		self.assertTrue('access' in response_email.data)
		self.assertTrue('refresh' in response_email.data)
		self.assertTrue('expired_at' in response_email.data)

		#by number
		data_number = {
			'number':'+79996248728',
			'password':'1995landa'
		}
		response_number = self.client.post(url_obtain, data = data_number, HTTP_USER_AGENT = user_agent[1])

		self.assertEquals(response_number.status_code, status.HTTP_200_OK)
		self.assertTrue('access' in response_number.data)
		self.assertTrue('refresh' in response_number.data)
		self.assertTrue('expired_at' in response_number.data)

		#check refresh
		url_refresh = reverse('token_refresh')
		refresh = response_number.data['refresh']

		data_refresh = {
			'refresh': refresh
		}
		response_refresh = self.client.post(url_refresh, data = data_refresh, HTTP_USER_AGENT = user_agent[1])

		self.assertEquals(response_refresh.status_code, status.HTTP_200_OK)
		self.assertTrue('access' in response_refresh.data)
		self.assertTrue('refresh' in response_refresh.data)
		self.assertTrue('expired_at' in response_refresh.data)