from django.contrib.auth import get_user_model
from django.core import validators

from rest_framework.test import APITestCase

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

from Users.models import User
from Organizations.models import *
from Clients.models import Client
from Sessions.models import Session



class TestClientsModels(APITestCase):

	def setUp(self):
		self.user_data = {
			'id':1000,
			'surname':'Landa',
			'name':'Hans',
			'patronymic':'maybe_not',
			'address':'Austria',
			'email':'tarantino_the_best@gmail.com',
			'number':'+79513450183',
		}
		self.user = User(**self.user_data)
		self.user.set_password('1995landa')
		self.user.save()

		self.organization = Organization.objects.create(id = 1000, name = 'Test', description = 'Test', address = 'Test', creator = self.user)
		self.client = Client.objects.create(id = 1000, user = self.user, organization = self.organization)


	def testClientModel(self):
		#user
		self.assertEquals(self.client._meta.get_field('user').verbose_name, 'Client')
		self.assertEquals(self.client.user.__class__, get_user_model())
		self.assertEquals(self.user.user_client, self.client)

		#organization
		self.assertEquals(self.client._meta.get_field('organization').verbose_name, 'Organization')
		self.assertEquals(self.client.organization.__class__, self.organization.__class__)
		self.assertEquals(self.organization.organization_clients.first(), self.client)

		#created_at
		self.assertEquals(self.client._meta.get_field('created_at').verbose_name, 'Created_at')
		self.assertTrue(self.client._meta.get_field('created_at').auto_now_add)

		#updated_at
		self.assertEquals(self.client._meta.get_field('updated_at').verbose_name, 'Updated_at')
		self.assertTrue(self.client._meta.get_field('updated_at').auto_now)

		#Meta-class
		self.assertEquals(self.client._meta.db_table, 'Client')
		self.assertEquals(self.client._meta.verbose_name_plural, 'Clients')
		self.assertEquals(self.client._meta.verbose_name, 'Client')
		self.assertEquals(self.client._meta.ordering, ['-updated_at'])


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