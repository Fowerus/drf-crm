from django.contrib.auth import get_user_model
from django.core import validators

from rest_framework.test import APITestCase

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

from Users.models import User
from Sessions.models import Session
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
			'number':'+79513450183',
		}
		self.user = User(**self.user_data)
		self.user.set_password('1995landa')
		self.user.save()

		self.session = Session.objects.create(id = 1000, user = self.user, device = 'test device')


	def testSessionModel(self):
		#user
		self.assertEquals(self.session._meta.get_field('user').verbose_name, 'User')
		self.assertEquals(self.session.user.__class__, get_user_model())
		self.assertEquals(self.user.user_sessions.first(), self.session)

		#device
		self.assertEquals(self.session._meta.get_field('device').verbose_name, 'Device')
		self.assertEquals(self.session._meta.get_field('device').max_length, 150)

		#created_at
		self.assertEquals(self.session._meta.get_field('created_at').verbose_name, 'Created_at')
		self.assertTrue(self.session._meta.get_field('created_at').auto_now_add)

		#updated_at
		self.assertEquals(self.session._meta.get_field('updated_at').verbose_name, 'Updated_at')
		self.assertTrue(self.session._meta.get_field('updated_at').auto_now)

		#Meta-class
		self.assertEquals(self.session._meta.unique_together, (("user","device"),))
		self.assertEquals(self.session._meta.db_table, 'Session')
		self.assertEquals(self.session._meta.verbose_name_plural, 'Sessions')
		self.assertEquals(self.session._meta.verbose_name, 'Session')
		self.assertEquals(self.session._meta.ordering, ['-updated_at'])


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