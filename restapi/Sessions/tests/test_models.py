from django.core import validators

from rest_framework.test import APITestCase

from Users.models import User
from Sessions.models import Session_user, Session_client
from Organizations.models import *
from Clients.models import *
from Sessions.models import *



class TestSessionsModels(APITestCase):

	def setUp(self):
		self.user_data = {
			'id':1000,
			'surname':'Landa',
			'name':'Hans',
			'patronymic':'maybe_not',
			'address':'Austria',
			'email':'tarantino_the_best@gmail.com',
			'phone':'+79513450183',
		}
		self.user = User(**self.user_data)
		self.user.set_password('1995landa')
		self.user.save()

		self.session_user = Session_user.objects.create(id = 1000, user = self.user, device = 'test device')
		self.organization = Organization.objects.create(id = 1000, name = 'test', description = 'descr', creator = self.user, address = 'gdeto zdes')
		self.client_data = {
			'id':1000,
			'surname':'Client',
			'name':'Client',
			'patronymic':'Client',
			'address':'Client',
			'phone':'+79517386274'
		}
		self.client = Client(**self.client_data)
		self.client.set_password('client1client1')
		self.client.organization.add(self.organization.id)
		self.client.save()

		self.session_client = Session_client.objects.create(id = 1000, client = self.client, device = 'test device')


	def testSession_userModel(self):
		#user
		self.assertEquals(self.session_user._meta.get_field('user').verbose_name, 'User')
		self.assertEquals(self.session_user.user.__class__, get_user_model())
		self.assertEquals(self.user.user_sessions.first(), self.session_user)

		#device
		self.assertEquals(self.session_user._meta.get_field('device').verbose_name, 'Device')
		self.assertEquals(self.session_user._meta.get_field('device').max_length, 150)

		#created_at
		self.assertEquals(self.session_user._meta.get_field('created_at').verbose_name, 'Created_at')
		self.assertTrue(self.session_user._meta.get_field('created_at').auto_now_add)

		#updated_at
		self.assertEquals(self.session_user._meta.get_field('updated_at').verbose_name, 'Updated_at')
		self.assertTrue(self.session_user._meta.get_field('updated_at').auto_now)

		#Meta-class
		self.assertEquals(self.session_user._meta.unique_together, (("user","device"),))
		self.assertEquals(self.session_user._meta.db_table, 'Session_user')
		self.assertEquals(self.session_user._meta.verbose_name_plural, 'Sessions users')
		self.assertEquals(self.session_user._meta.verbose_name, 'Session user')
		self.assertEquals(self.session_user._meta.ordering, ['-updated_at'])



	def testSession_clientModel(self):
		#client
		self.assertEquals(self.session_client._meta.get_field('client').verbose_name, 'Client')
		self.assertEquals(self.session_client.client.__class__, Client)
		self.assertEquals(self.client.client_sessions.first(), self.session_client)

		#device
		self.assertEquals(self.session_client._meta.get_field('device').verbose_name, 'Device')
		self.assertEquals(self.session_client._meta.get_field('device').max_length, 150)

		#created_at
		self.assertEquals(self.session_client._meta.get_field('created_at').verbose_name, 'Created_at')
		self.assertTrue(self.session_client._meta.get_field('created_at').auto_now_add)

		#updated_at
		self.assertEquals(self.session_client._meta.get_field('updated_at').verbose_name, 'Updated_at')
		self.assertTrue(self.session_client._meta.get_field('updated_at').auto_now)

		#Meta-class
		self.assertEquals(self.session_client._meta.unique_together, (("client","device"),))
		self.assertEquals(self.session_client._meta.db_table, 'Session_client')
		self.assertEquals(self.session_client._meta.verbose_name_plural, 'Sessions clients')
		self.assertEquals(self.session_client._meta.verbose_name, 'Session client')
		self.assertEquals(self.session_client._meta.ordering, ['-updated_at'])



	def tearDown(self):
		Client.objects.all().delete()
		Service.objects.all().delete()
		Organization.objects.all().delete()
		Session_user.objects.all().delete()
		Session_client.objects.all().delete()
		User.objects.all().delete()
		