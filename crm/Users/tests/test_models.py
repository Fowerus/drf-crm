from django.contrib.auth import get_user_model
from django.core import validators

from rest_framework.test import APITestCase

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

from Users.models import User, VerifyInfo
from Organizations.models import *
from Clients.models import *
from Sessions.models import *



class TestUsersModels(APITestCase):

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

		self.verify_info = VerifyInfo.objects.create(id = 1000, user = self.user, code = 123432124, type_code = 'email')


	def testUserModel(self):
		#surname
		self.assertEquals(self.user._meta.get_field('surname').verbose_name, 'Surname')
		self.assertEquals(self.user._meta.get_field('surname').max_length, 150)
		
		#name
		self.assertEquals(self.user._meta.get_field('name').verbose_name, 'Name')
		self.assertEquals(self.user._meta.get_field('name').max_length, 150)

		#patronymic
		self.assertEquals(self.user._meta.get_field('patronymic').verbose_name, 'Patronymic')
		self.assertEquals(self.user._meta.get_field('patronymic').max_length, 150)

		#email
		self.assertEquals(self.user._meta.get_field('email').verbose_name, 'Email')
		self.assertEquals(self.user._meta.get_field('email').max_length, 100)
		self.assertTrue(self.user._meta.get_field('email').unique)
		self.assertTrue(validators.EmailValidator in self.user._meta.get_field('email').validators)

		#number
		self.assertTrue(self.user._meta.get_field('number').unique)
		self.assertTrue(self.user._meta.get_field('number').blank)
		self.assertTrue(self.user._meta.get_field('number').null)

		#address
		self.assertEquals(self.user._meta.get_field('address').max_length, 200)
		self.assertTrue(self.user._meta.get_field('address').blank)
		self.assertEquals(self.user._meta.get_field('address').verbose_name, 'Address')

		#image
		self.assertEquals(self.user._meta.get_field('image').crop, ['middle', 'center'])
		self.assertEquals(self.user._meta.get_field('image').verbose_name, 'Image')
		self.assertTrue(self.user._meta.get_field('image').blank)

		#created_at
		self.assertEquals(self.user._meta.get_field('created_at').verbose_name, 'Created_at')
		self.assertTrue(self.user._meta.get_field('created_at').auto_now_add)

		#updated_at
		self.assertEquals(self.user._meta.get_field('updated_at').verbose_name, 'Updated_at')
		self.assertTrue(self.user._meta.get_field('updated_at').auto_now)

		#other
		self.assertFalse(self.user._meta.get_field('confirmed_email').default)
		self.assertFalse(self.user._meta.get_field('confirmed_number').default)
		self.assertFalse(self.user._meta.get_field('is_staff').default)
		self.assertFalse(self.user._meta.get_field('is_superuser').default)
		self.assertTrue(self.user._meta.get_field('is_active').default)

		#self.USERNAME_FIELD
		self.assertEquals(self.user.USERNAME_FIELD, 'email')
		#REQUIRED_FIELDS
		self.assertEquals(self.user.REQUIRED_FIELDS, ('surname','name', 'patronymic', 'address'))

		#Meta-class
		self.assertEquals(self.user._meta.db_table, 'User')
		self.assertEquals(self.user._meta.verbose_name_plural, 'Users')
		self.assertEquals(self.user._meta.verbose_name, 'User')
		self.assertEquals(self.user._meta.ordering, ['-created_at'])


	def testVerifyInfoModel(self):
		#user
		self.assertEquals(self.verify_info._meta.get_field('user').verbose_name, 'User')
		self.assertEquals(self.verify_info.user.__class__, get_user_model())

		#code
		self.assertTrue(self.verify_info._meta.get_field('code').unique)

		#type_code
		self.assertEquals(self.verify_info._meta.get_field('type_code').max_length, 10)
		self.assertEquals(self.verify_info._meta.get_field('type_code').verbose_name, 'Type_code')

		#created_at
		self.assertEquals(self.verify_info._meta.get_field('created_at').verbose_name, 'Created_at')
		self.assertTrue(self.verify_info._meta.get_field('created_at').auto_now_add)

		#Meta-class
		self.assertEquals(self.verify_info._meta.unique_together, (('user', 'type_code'),))
		self.assertEquals(self.verify_info._meta.db_table, 'VerifyInfo')
		self.assertEquals(self.verify_info._meta.verbose_name_plural, 'VerifyInfoes')
		self.assertEquals(self.verify_info._meta.verbose_name, 'VerifyInfo')
		self.assertEquals(self.verify_info._meta.ordering, ['-created_at'])


	def tearDown(self):
		VerifyInfo.objects.all().delete()
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