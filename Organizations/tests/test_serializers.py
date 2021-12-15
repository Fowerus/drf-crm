from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

from Organizations.models import *
from Organizations.serializers import *
from Users.serializers import UserSerializer
from Clients.models import Client



class TestOrganizationsSerializers(APITestCase):

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
		permission = CustomPermission.objects.create(id = 1, name = 'Can add role', codename = 'role_create')
		role = Role(id = 1, name = 'test', organization = organization)
		role.permissions.set({permission})
		role.save()
		service = Service.objects.create(id = 1, name = 'Test', address = 'phone', phone = '+79967364916', organization = organization)
		client_data = {
			'id':1000,
			'surname':'client1',
			'name':'client1',
			'patronymic':'client1',
			'address':'client1',
			'phone':'+79968376291'
		}
		client = Client(**client_data)
		client.set_password('client1client1')
		client.organization.add(organization.id)


	def testOrganizationSerializer(self):
		#OrganizationSerializer for list
		organization_serializer = OrganizationSerializer()

		self.assertEquals(organization_serializer.fields['creator'].__class__, UserSerializer)
		self.assertEquals(organization_serializer.Meta.fields,['id','name','description', 'address', 'creator', 'created_at', 'numbers','links', 'updated_at'])
		self.assertEquals(organization_serializer.Meta.model, Organization)

		#OrganizationSerializer for create
		org_data = {
			'name':'Relevant organization',
			'discription':'Clowns',
			'address':'Austria',
			'creator':1
		}
		organization_serializer_create = organization_serializer.OrganizationCSerializer(data = org_data)

		self.assertEquals(organization_serializer_create.Meta.fields, ['name','description', 'address', 'links', 'numbers', 'creator'])
		self.assertEquals(organization_serializer_create.Meta.model, Organization)

		self.assertTrue(organization_serializer_create.is_valid())
		self.assertEquals(organization_serializer_create.errors, {})
		


	def testPermissionSerializer(self):
		#PermissionSerializer for list
		permission_serializer = PermissionSerializer()

		self.assertEquals(permission_serializer.Meta.fields, ['id', 'name', 'codename'])
		self.assertEquals(permission_serializer.Meta.model, CustomPermission)


	def testRoleSerializer(self):
		#RoleSerializer for list
		role_serializer = RoleSerializer()

		self.assertEquals(role_serializer.fields['organization'].__class__, OrganizationSerializer)
		self.assertEquals(role_serializer.Meta.fields, ['id','name','permissions', 'organization', 'created_at', 'updated_at'])
		self.assertEquals(role_serializer.Meta.model, Role)

		#RoleSerializer for create
		org_role_data = {
			'name':'Test_role',
			'permissions':{1},
			'organization':1
		}
		role_serializer_create = role_serializer.RoleCSerializer(data = org_role_data)

		self.assertEquals(role_serializer_create.Meta.fields, ['name', 'permissions', 'organization'])
		self.assertEquals(role_serializer_create.Meta.model, Role)

		self.assertTrue(role_serializer_create.is_valid())
		self.assertEquals(role_serializer_create.errors, {})


	def testOrganization_memberSerializer(self):
		#Organization_memberSerializer for list
		organization_member_serializer = Organization_memberSerializer()

		self.assertEquals(organization_member_serializer.fields['user'].__class__, UserSerializer)
		self.assertEquals(organization_member_serializer.fields['role'].__class__, RoleSerializer)
		self.assertEquals(organization_member_serializer.fields['organization'].__class__, OrganizationSerializer)

		self.assertEquals(organization_member_serializer.Meta.fields, ['id', 'user','role', 'organization', 'created_at', 'updated_at'])
		self.assertEquals(organization_member_serializer.Meta.model, Organization_member)

		#Organization_memberSerializer for create
		org_member_data = {
			'user':1,
			'role':1,
			'organization':1
		}
		orgaization_member_create = organization_member_serializer.Organization_memberCSerializer(data =org_member_data)

		self.assertEquals(orgaization_member_create.Meta.fields, ['user','role', 'organization'])
		self.assertEquals(orgaization_member_create.Meta.model, Organization_member)

		self.assertTrue(orgaization_member_create.is_valid())
		self.assertEquals(orgaization_member_create.errors, {})


	def testServiceSerializer(self):
		#ServiceSerializer for list
		service_serializer = ServiceSerializer()

		self.assertEquals(service_serializer.fields['organization'].__class__, OrganizationSerializer)
		self.assertEquals(service_serializer.Meta.fields, ['id', 'name', 'address', 'phone', 'organization', 'created_at', 'updated_at'])
		self.assertEquals(service_serializer.Meta.model, Service)

		#ServiceSerializer for create
		org_service_data = {
			'name':'Test service',
			'address':'Neznau',
			'phone':'+79185245612',
			'organization':1
		}
		service_serializer_create = service_serializer.ServiceCSerializer(data = org_service_data)

		self.assertEquals(service_serializer_create.Meta.fields, ['name', 'address', 'phone', 'organization'])
		self.assertEquals(service_serializer_create.Meta.model, Service)

		self.assertTrue(service_serializer_create.is_valid())
		self.assertEquals(service_serializer_create.errors, {})


	def tearDown(self):
		Client.objects.all().delete()
		Service.objects.all().delete()
		Organization_member.objects.all().delete()
		Role.objects.all().delete()
		CustomPermission.objects.all().delete()
		Organization.objects.all().delete()
		get_user_model().objects.all().delete()
		