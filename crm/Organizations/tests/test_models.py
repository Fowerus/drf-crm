from django.contrib.auth import get_user_model
from django.core import validators

from rest_framework.test import APITestCase

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

from Organizations.models import *
from Users.models import User
from Clients.models import Client
from Sessions.models import Session



class TestOrganizationsModels(APITestCase):

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

		self.organization_number = Organization_number.objects.create(id = 1000, number = '+79516285284', organization = self.organization)

		self.organization_link = Organization_link.objects.create(id = 1000, name = 'Link to vk', link = 'https://vk.com', organization = self.organization)

		self.service = Service.objects.create(name = 'Test service', number = '+79994763851', address = 'Test address', organization = self.organization)

		self.perm = CustomPermission.objects.create(id = 1000, name = 'Can and client', codename = 'client_create')

		self.role = Role(id = 1000, name = 'Test role', organization = self.organization)
		self.role.permissions.set({self.perm.id})
		self.role.save()

		self.organization_member = Organization_member.objects.create(id = 1000, user = self.user, role = self.role, organization = self.organization)

		self.order = Order.objects.create(order_code = 12321, description = 'test', client = self.user, executor = self.user, creator = self.user, service = self.service)


	def testOrganizationModel(self):
		#name
		self.assertEquals(self.organization._meta.get_field('name').verbose_name, 'Name')
		self.assertEquals(self.organization._meta.get_field('name').max_length, 150)
		self.assertTrue(self.organization._meta.get_field('name').unique)

		#description
		self.assertEquals(self.organization._meta.get_field('description').verbose_name, 'Description')
		self.assertEquals(self.organization._meta.get_field('description').max_length, 500)
		self.assertTrue(self.organization._meta.get_field('description').blank)

		#address
		self.assertEquals(self.organization._meta.get_field('address').max_length, 200)
		self.assertEquals(self.organization._meta.get_field('address').verbose_name, 'Address')

		#creator
		self.assertTrue(self.organization.creator.__class__, get_user_model())
		self.assertEquals(self.organization._meta.get_field('creator').verbose_name, 'Creator')
		self.assertEquals(self.user.my_organizations.first(), self.organization)

		#created_at
		self.assertEquals(self.organization._meta.get_field('created_at').verbose_name, 'Created_at')
		self.assertTrue(self.organization._meta.get_field('created_at').auto_now_add)

		#updated_at
		self.assertEquals(self.organization._meta.get_field('updated_at').verbose_name, 'Updated_at')
		self.assertTrue(self.organization._meta.get_field('updated_at').auto_now)

		#Meta-class
		self.assertEquals(self.organization._meta.unique_together, (("name","address"),))
		self.assertEquals(self.organization._meta.db_table, 'Organization')
		self.assertEquals(self.organization._meta.verbose_name_plural, 'Organizations')
		self.assertEquals(self.organization._meta.verbose_name, 'Organization')
		self.assertEquals(self.organization._meta.ordering, ['-updated_at'])


	def testOrganization_numberModel(self):
		#number
		self.assertTrue(self.organization_number._meta.get_field('number').unique)

		#organization
		self.assertEquals(self.organization_number._meta.get_field('organization').verbose_name, 'Organization')
		self.assertEquals(self.organization_number.organization.__class__, self.organization.__class__)
		self.assertEquals(self.organization.organization_numbers.first(), self.organization_number)

		#Meta-class
		self.assertEquals(self.organization_number._meta.unique_together, (("number","organization"),))
		self.assertEquals(self.organization_number._meta.db_table, 'Organization_number')
		self.assertEquals(self.organization_number._meta.verbose_name_plural, 'Organizations numbers')
		self.assertEquals(self.organization_number._meta.verbose_name, 'Organization number')
		self.assertEquals(self.organization_number._meta.ordering, ['-updated_at'])


	def testOrganization_linkModel(self):
		#name
		self.assertEquals(self.organization_link._meta.get_field('name').verbose_name, 'Name')
		self.assertEquals(self.organization_link._meta.get_field('name').max_length, 50)

		#link
		self.assertEquals(self.organization_link._meta.get_field('link').verbose_name, 'Link')
		self.assertEquals(self.organization_link._meta.get_field('link').max_length, 200)
		self.assertTrue(self.organization_link._meta.get_field('link').unique)

		#organization
		self.assertEquals(self.organization_link._meta.get_field('organization').verbose_name, 'Organization')
		self.assertEquals(self.organization_link.organization.__class__, self.organization.__class__)
		self.assertEquals(self.organization.organization_links.first(), self.organization_link)

		#Meta-class
		self.assertEquals(self.organization_link._meta.unique_together, (("link","organization"),))
		self.assertEquals(self.organization_link._meta.db_table, 'Organization_link')
		self.assertEquals(self.organization_link._meta.verbose_name_plural, 'Organizations links')
		self.assertEquals(self.organization_link._meta.verbose_name, 'Organization link')
		self.assertEquals(self.organization_link._meta.ordering, ['-updated_at'])


	def tearDown(self):
		self.organization_link.delete()
		self.organization_number.delete()


	def testServiceModel(self):
		#name
		self.assertEquals(self.service._meta.get_field('name').verbose_name, 'Name')
		self.assertEquals(self.service._meta.get_field('name').max_length, 150)
		self.assertTrue(self.service._meta.get_field('name').unique)

		#number
		self.assertEquals(self.service._meta.get_field('number').verbose_name, 'Number')
		self.assertTrue(self.service._meta.get_field('number').unique)

		#address
		self.assertEquals(self.service._meta.get_field('address').verbose_name, 'Address')
		self.assertEquals(self.service._meta.get_field('address').max_length, 200)

		#organization
		self.assertEquals(self.service._meta.get_field('organization').verbose_name, 'Organization')
		self.assertEquals(self.service.organization.__class__, self.organization.__class__)
		self.assertEquals(self.organization.organization_services.first(), self.service)

		#Meta-class
		self.assertEquals(self.service._meta.unique_together, (("name","organization"),))
		self.assertEquals(self.service._meta.db_table, 'Service')
		self.assertEquals(self.service._meta.verbose_name_plural, 'Services')
		self.assertEquals(self.service._meta.verbose_name, 'Service')
		self.assertEquals(self.service._meta.ordering, ['-updated_at'])


	def testCustomPermissionModel(self):
		#name
		self.assertEquals(self.perm._meta.get_field('name').verbose_name, 'Official_name')
		self.assertEquals(self.perm._meta.get_field('name').max_length, 60)
		self.assertTrue(self.perm._meta.get_field('name').unique)

		#codename
		self.assertEquals(self.perm._meta.get_field('codename').verbose_name, 'Codename')
		self.assertEquals(self.perm._meta.get_field('codename').max_length, 150)
		self.assertTrue(self.perm._meta.get_field('codename').unique)

		#created_at
		self.assertEquals(self.perm._meta.get_field('created_at').verbose_name, 'Created_at')
		self.assertTrue(self.perm._meta.get_field('created_at').auto_now_add)

		#Meta-class
		self.assertEquals(self.perm._meta.unique_together, (("name","codename"),))
		self.assertEquals(self.perm._meta.db_table, 'CustomPermission')
		self.assertEquals(self.perm._meta.verbose_name_plural, 'CustomPermissions')
		self.assertEquals(self.perm._meta.verbose_name, 'CustomPermission')
		self.assertEquals(self.perm._meta.ordering, ['-created_at'])


	def testRoleModel(self):
		#name
		self.assertEquals(self.role._meta.get_field('name').verbose_name, 'Name')
		self.assertEquals(self.role._meta.get_field('name').max_length, 100)
		self.assertTrue(self.role._meta.get_field('name').unique)

		#permissions
		self.assertEquals(self.role._meta.get_field('permissions').verbose_name, 'Permissions')
		self.assertEquals(self.role.permissions.first().__class__, self.perm.__class__)
		self.assertEquals(self.perm.permission_roles.first(), self.role)

		#organization
		self.assertEquals(self.role._meta.get_field('organization').verbose_name, 'Organization')
		self.assertEquals(self.role.organization.__class__, self.organization.__class__)
		self.assertEquals(self.organization.organization_roles.first(), self.role)

		#Meta-class
		self.assertEquals(self.role._meta.unique_together, (("name","organization"),))
		self.assertEquals(self.role._meta.db_table, 'Role')
		self.assertEquals(self.role._meta.verbose_name_plural, 'Roles')
		self.assertEquals(self.role._meta.verbose_name, 'Role')
		self.assertEquals(self.role._meta.ordering, ['-updated_at'])


	def testOrganization_memberModel(self):
		#user
		self.assertEquals(self.organization_member._meta.get_field('user').verbose_name, 'User')
		self.assertEquals(self.organization_member.user.__class__, get_user_model())
		self.assertEquals(self.user.user_member.first(), self.organization_member)

		#role
		self.assertEquals(self.organization_member._meta.get_field('role').verbose_name, 'Role')
		self.assertEquals(self.organization_member.role.__class__, self.role.__class__)
		self.assertEquals(self.role.role_member.first(), self.organization_member)

		#organization
		self.assertEquals(self.organization_member._meta.get_field('organization').verbose_name, 'Organization')
		self.assertEquals(self.organization_member.organization.__class__, self.organization.__class__)
		self.assertEquals(self.organization.organization_members.first(), self.organization_member)

		#Meta-class
		self.assertEquals(self.organization_member._meta.unique_together, (("user","organization"),))
		self.assertEquals(self.organization_member._meta.db_table, 'Organization_member')
		self.assertEquals(self.organization_member._meta.verbose_name_plural, 'Organizations members')
		self.assertEquals(self.organization_member._meta.verbose_name, 'Organization member')
		self.assertEquals(self.organization_member._meta.ordering, ['-updated_at'])


	def testOrderModel(self):
		#order_code
		self.assertEquals(self.order._meta.get_field('order_code').verbose_name, 'Order_code')
		self.assertTrue(self.order._meta.get_field('order_code').unique)

		#description
		self.assertEquals(self.order._meta.get_field('description').verbose_name, 'Description')
		self.assertEquals(self.order._meta.get_field('description').max_length, 500)

		#client
		self.assertEquals(self.order._meta.get_field('client').verbose_name, 'Client')
		self.assertEquals(self.order.client.__class__, self.user.__class__)
		self.assertEquals(self.user.client_orders.first(), self.order)

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

		#blocked
		self.assertFalse(self.order._meta.get_field('blocked').default)

		#Meta-class
		self.assertEquals(self.order._meta.db_table, 'Order')
		self.assertEquals(self.order._meta.verbose_name_plural, 'Orders')
		self.assertEquals(self.order._meta.verbose_name, 'Order')
		self.assertEquals(self.order._meta.ordering, ['-updated_at'])


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