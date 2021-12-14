from django.core import validators

from rest_framework.test import APITestCase

from Users.models import User
from Sessions.models import Session_user, Session_client
from Organizations.models import *
from Clients.models import *
from Sessions.models import *
from Orders.models import Order



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

		self.organization = Organization.objects.create(id = 1000, name = 'test', description = 'descr', creator = self.user, address = 'gdeto zdes')
		self.service = Service.objects.create(id = 1000, name = 'Test', address = 'phone', phone = '+79967364916', organization = self.organization)
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

		self.order_data = {
			"id":1000,
			"order_code":2323,
			"description":"fdsf",
			'service':self.service,
			"executor":self.user,
			"creator":self.user,
			"client":self.client
		}
		self.order = Order.objects.create(**self.order_data)



	def testOrderModel(self):
		#order_code
		self.assertEquals(self.order._meta.get_field('order_code').verbose_name, 'Order_code')
		self.assertTrue(self.order._meta.get_field('order_code').unique)

		#description
		self.assertEquals(self.order._meta.get_field('description').verbose_name, 'Description')
		self.assertEquals(self.order._meta.get_field('description').max_length, 500)

		#client
		self.assertEquals(self.order._meta.get_field('client').verbose_name, 'Client')
		self.assertEquals(self.order.client.__class__, self.client.__class__)
		self.assertEquals(self.client.client_orders.first(), self.order)

		#executor
		self.assertEquals(self.order._meta.get_field('executor').verbose_name, 'Executor')
		self.assertEquals(self.order.executor.__class__, self.user.__class__)
		self.assertEquals(self.user.user_executor.first(), self.order)

		#creator
		self.assertEquals(self.order._meta.get_field('creator').verbose_name, 'Creator')
		self.assertEquals(self.order.creator.__class__, self.user.__class__)
		self.assertEquals(self.user.user_creator.first(), self.order)

		#service
		self.assertEquals(self.order._meta.get_field('service').verbose_name, 'Service')
		self.assertEquals(self.order.service.__class__, self.service.__class__)
		self.assertEquals(self.service.service_orders.first(), self.order)

		#done
		self.assertFalse(self.order._meta.get_field('done').default)

		#Meta-class
		self.assertEquals(self.order._meta.db_table, 'Order')
		self.assertEquals(self.order._meta.verbose_name_plural, 'Orders')
		self.assertEquals(self.order._meta.verbose_name, 'Order')
		self.assertEquals(self.order._meta.ordering, ['-updated_at'])


	def tearDown(self):
		Order.objects.all().delete()
		Client.objects.all().delete()
		Service.objects.all().delete()
		Organization.objects.all().delete()
		User.objects.all().delete()
		