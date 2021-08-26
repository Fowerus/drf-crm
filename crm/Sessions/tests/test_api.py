from django.contrib.auth import get_user_model
from django.core import validators
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

from Users.models import User
from Sessions.models import Session



class TestSessionsAPI(APITestCase):

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
		self.user.save()

		self.user_agent = [
			'Mozilla: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101',
			'Firefox/47.3 Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/43.4',
		] 

		self.response1 = self.client.post(
			reverse('token_obtain_pair'), 
			data = {'number':'+79996248728', 'password':'1995landa'},
			HTTP_USER_AGENT = self.user_agent[0])

		self.response2 = self.client.post(
			reverse('token_obtain_pair'),
			data = {'number':'+79996248728', 'password':'1995landa'},
			HTTP_USER_AGENT = self.user_agent[1])

		self.access = self.response2.data['access']


	def testSession(self):
		url = reverse('session')
		access = f'Bearer {self.access}'

		#GET
		#Within token
		response_get = self.client.get(url)
		self.assertEquals(response_get.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_get = self.client.get(url, HTTP_AUTHORIZATION = access)

		self.assertEquals(response_get.status_code, status.HTTP_200_OK)
		self.assertEquals(len(response_get.data), 2)

		#DELETE
		#Within token
		response_delete = self.client.delete(url)
		self.assertEquals(response_delete.status_code, status.HTTP_401_UNAUTHORIZED)

		#With token
		response_delete = self.client.delete(url, data = {'session':1}, HTTP_AUTHORIZATION = access)
		self.assertEquals(response_delete.status_code, status.HTTP_200_OK)