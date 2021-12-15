from django.core import validators

from rest_framework.test import APITestCase

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

from Users.models import User
from VerifyInfo.models import VerifyInfoUser, VerifyInfoClient



class TestVerifyInfoModels(APITestCase):

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

		self.verify_info = VerifyInfoUser.objects.create(id = 1000, user = self.user, code = 123432124, type_code = 'email')



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
		self.assertEquals(self.verify_info._meta.db_table, 'VerifyInfoUser')
		self.assertEquals(self.verify_info._meta.verbose_name_plural, 'VerifyInfoUsers')
		self.assertEquals(self.verify_info._meta.verbose_name, 'VerifyInfoUser')
		self.assertEquals(self.verify_info._meta.ordering, ['-created_at'])



	def tearDown(self):
		VerifyInfoUser.objects.all().delete()
		User.objects.all().delete()
		