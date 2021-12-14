from django.core import validators

from rest_framework.test import APITestCase

from Users.models import User



class TestUsersModels(APITestCase):

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

		#phone
		self.assertTrue(self.user._meta.get_field('phone').unique)
		self.assertTrue(self.user._meta.get_field('phone').blank)
		self.assertTrue(self.user._meta.get_field('phone').null)

		#address
		self.assertEquals(self.user._meta.get_field('address').max_length, 200)
		self.assertFalse(self.user._meta.get_field('address').blank)
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
		self.assertFalse(self.user._meta.get_field('confirmed_phone').default)
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



	def tearDown(self):
		User.objects.all().delete()
		