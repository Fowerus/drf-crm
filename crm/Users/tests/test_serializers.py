from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

from Users.models import User
from Users.serializers import *
from Organizations.models import *
from Clients.models import *
from Sessions.models import *



class TestUsersSerializers(APITestCase):

	def testUserRegistrationSerializer(self):
		user_data = {
			'surname':'Landa',
			'name':'Hans',
			'patronymic':'maybe_not',
			'address':'Austria',
			'email':'tarantino_the_best@gmail.com',
			'number':'+79513450183',
			'password':'1995landa'
		}
		user_registration_serializer = UserRegistrationSerializer(data = user_data)

		self.assertEquals(user_registration_serializer.fields['password'].max_length, 128)
		self.assertEquals(user_registration_serializer.fields['password'].min_length, 8)
		self.assertEquals(user_registration_serializer.fields['password'].write_only, True)

		self.assertEquals(set(user_registration_serializer.Meta.fields), set(['email','surname','name','patronymic', 'address', 'number', 'password']))
		self.assertEquals(user_registration_serializer.Meta.model, get_user_model())

		self.assertTrue(user_registration_serializer.is_valid())
		self.assertEquals(user_registration_serializer.errors, {})


	def testUserSerializer(self):
		user_serializer = UserSerializer()

		self.assertEquals(user_serializer.Meta.fields, ['id', 'surname', 'name', 'patronymic', 'address', 'email', 'image','confirmed_email', 'confirmed_number', 'created_at', 'updated_at'])
		self.assertEquals(user_serializer.Meta.model, get_user_model())


	def testMyTokenRefreshSerializer(self):
		token_refresh_serializer = MyTokenRefreshSerializer()
		token_refresh_serializer_fields = token_refresh_serializer.fields

		self.assertTrue(token_refresh_serializer_fields['refresh'].write_only) 
		self.assertTrue(token_refresh_serializer_fields['device'].write_only) 
		self.assertTrue(token_refresh_serializer_fields['detail'].read_only) 
		self.assertTrue(token_refresh_serializer_fields['access'].read_only)


	def testMyTokenObtainPairEmailSerializer(self):
		token_obtain_pair_email_serializer = MyTokenObtainPairEmailSerializer()
		token_obtain_pair_email_serializer_fields = token_obtain_pair_email_serializer.fields

		self.assertTrue(token_obtain_pair_email_serializer_fields['device'].write_only, True)
		self.assertTrue(token_obtain_pair_email_serializer_fields['detail'].read_only, True)
		self.assertTrue(token_obtain_pair_email_serializer_fields['refresh'].read_only, True)
		self.assertTrue(token_obtain_pair_email_serializer_fields['access'].read_only, True)


	def testMyTokenObtainPairNumberSerializer(self):
		token_obtain_pair_number_serializer = MyTokenObtainPairNumberSerializer()
		token_obtain_pair_number_serializer_fields = token_obtain_pair_number_serializer.fields

		self.assertTrue(token_obtain_pair_number_serializer_fields['device'].write_only, True)
		self.assertTrue(token_obtain_pair_number_serializer_fields['detail'].read_only, True)
		self.assertTrue(token_obtain_pair_number_serializer_fields['refresh'].read_only, True)
		self.assertTrue(token_obtain_pair_number_serializer_fields['access'].read_only, True)


	def testMyTokenObtainForNumberSerializer(self):
		token_obtain_for_number_serializer = MyTokenObtainForNumberSerializer()
		token_obtain_for_number_serializer_fields = token_obtain_for_number_serializer.fields
		
		self.assertTrue('number' in token_obtain_for_number_serializer_fields)


	def testMyTokenObtainForEmailSerializer(self):
		token_obtain_for_email_serializer = MyTokenObtainForEmailSerializer()
		token_obtain_for_email_serializer_fields = token_obtain_for_email_serializer.fields
		username_field = get_user_model().USERNAME_FIELD

		self.assertTrue(token_obtain_for_email_serializer_fields[username_field].write_only)


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