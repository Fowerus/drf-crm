from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from Users.models import User
from Users.serializers import *



class TestUsersSerializers(APITestCase):

	def setUp(self):
		pass


	def testUserRegistrationSerializer(self):
		pass