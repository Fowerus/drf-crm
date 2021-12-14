from django.contrib.auth import get_user_model
from django.core import validators

from rest_framework.test import APITestCase

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

from Organizations.models import *
from Users.models import User
from Clients.models import Client



class TestOrganizationsModels(APITestCase):

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

		self.organization = Organization.objects.create(id = 1000, name = 'Test', description = 'Test', address = 'Test', creator = self.user)

		self.service = Service.objects.create(name = 'Test service', phone = '+79994763851', address = 'Test address', organization = self.organization)

		self.perm = CustomPermission.objects.create(id = 1000, name = 'Can and client', codename = 'client_create')

		self.role = Role(id = 1000, name = 'Test role', organization = self.organization)
		self.role.permissions.set({self.perm.id})
		self.role.save()

		self.organization_member = Organization_member.objects.create(id = 1000, user = self.user, role = self.role, organization = self.organization)


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



	def tearDown(self):
		self.organization_link.delete()
		self.organization_number.delete()


	def testServiceModel(self):
		#name
		self.assertEquals(self.service._meta.get_field('name').verbose_name, 'Name')
		self.assertEquals(self.service._meta.get_field('name').max_length, 150)
		self.assertTrue(self.service._meta.get_field('name').unique)

		#phone
		self.assertEquals(self.service._meta.get_field('phone').verbose_name, 'Phone')
		self.assertTrue(self.service._meta.get_field('phone').unique)

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



	def tearDown(self):
		Service.objects.all().delete()
		Organization_member.objects.all().delete()
		Role.objects.all().delete()
		CustomPermission.objects.all().delete()
		Organization.objects.all().delete()
		get_user_model().objects.all().delete()
		