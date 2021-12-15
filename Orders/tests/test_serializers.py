from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

from Organizations.models import *
from Organizations.serializers import *
from Users.serializers import UserSerializer
from Orders.serializers import OrderSerializer
from Orders.models import Order
from Clients.models import Client



class TestOrderSerialiser(APITestCase):

	@classmethod
	def setUpTestData(cls):
		user_data = {
			'id':1,
			'surname':'Landa',
			'name':'Hans',
			'patronymic':'-',
			'address':'Austria',
			'email':'tarantino_the_best@gmail.com',
			'phone':'+79513450183'
		}
		user = get_user_model()(**user_data)
		user.set_password('1995')
		user.save()

		organization = Organization.objects.create(id = 1, name = 'Test', description = 'description', address = 'address', creator = user)
		service = Service.objects.create(id = 1, name = 'Test', address = 'phone', phone = '+79967364916', organization = organization)
		client_data = {
			'id':1,
			'surname':'client1',
			'name':'client1',
			'patronymic':'client1',
			'address':'client1',
			'phone':'+79968376291'
		}
		client = Client(**client_data)
		client.set_password('client1client1')
		client.organization.add(organization.id)



	def testOrderSerializer(self):
		#OrderSerializer for list
		order_serializer = OrderSerializer()

		self.assertEquals(order_serializer.fields['creator'].__class__, UserSerializer)
		self.assertEquals(order_serializer.fields['executor'].__class__, UserSerializer)
		self.assertEquals(order_serializer.fields['service'].__class__, ServiceSerializer)

		self.assertEquals(order_serializer.Meta.fields, ['id', 'order_code', 'description', 'creator', 'executor', 'client', 'done', 'service', 'created_at', 'updated_at'])
		self.assertEquals(order_serializer.Meta.model, Order)

		#OrderSerializer for create
		org_order_data = {
			'description':'test',
			'client':1,
			'creator':1,
			'executor':1,
			'service':1
		}
		order_serializer_create = order_serializer.OrderCSerializer(data = org_order_data)

		self.assertEquals(order_serializer_create.Meta.fields, ['description', 'creator', 'executor', 'client', 'service'])
		self.assertEquals(order_serializer_create.Meta.model, Order)


	def tearDown(self):
		Client.objects.all().delete()
		Service.objects.all().delete()

		Organization.objects.all().delete()
		get_user_model().objects.all().delete()
		