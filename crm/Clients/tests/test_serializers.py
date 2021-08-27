from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

from Users.serializers import *
from Organizations.serializers import OrganizationSerializer

from Users.models import User
from Organizations.models import *
from Clients.models import Client
from Sessions.models import Session

from Clients.serializers import ClientSerializer



class TestClientsSerializers(APITestCase):

	@classmethod
	def setUpTestData(cls):
		user = User(id = 1000, surname = 'users', name = 'usern', patronymic = 'userp', address = 'usera', email = 'usere@gmail.com')
		user.set_password('user17893')
		user.save()

		organization = Organization(id = 1000, name = 'organization', description = 'description', address = 'Moscow', creator = user)
		organization.save()

 
	def testClientSerializer(self):
		#ClientSerializer for list
		client_serializer = ClientSerializer()

		self.assertEquals(client_serializer.fields['user'].__class__, UserSerializer)
		self.assertEquals(client_serializer.fields['organization'].__class__, OrganizationSerializer)

		self.assertEquals(client_serializer.Meta.fields, ['id','organization', 'user'])
		self.assertEquals(client_serializer.Meta.model, Client)

		#ClientSerializer for create
		client_data = {
			'surname':'client_surn',
			'name':'client_name',
			'patronymic':'client_patr',
			'password':'client23344',
			'address':'ssdfsf',
			'email':'cliente@gmail.com',
			'organization':1000
		}
		client_serializer_create = client_serializer.ClientCSerializer(data = client_data)

		self.assertTrue(client_serializer_create.fields['password'].write_only)
		self.assertTrue(client_serializer_create.fields['address'].write_only)
		self.assertTrue(client_serializer_create.fields['email'].write_only)
		self.assertTrue(client_serializer_create.fields['surname'].write_only)
		self.assertTrue(client_serializer_create.fields['name'].write_only)
		self.assertTrue(client_serializer_create.fields['patronymic'].write_only)

		self.assertEquals(client_serializer_create.Meta.fields, ['organization', 'password', 'email', 'surname', 'name', 'patronymic', 'address'])
		self.assertEquals(client_serializer_create.Meta.model, Client)

		self.assertTrue(client_serializer_create.is_valid())
		self.assertEquals(client_serializer_create.errors, {})


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