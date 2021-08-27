from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

from Organizations.models import *
from Organizations.serializers import *
from Users.serializers import UserSerializer
from Clients.models import Client
from Sessions.models import Session



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
			'number':'+79513450183'
		}
		user = get_user_model()(**user_data)
		user.set_password('1995')
		user.save()

		organization = Organization.objects.create(id = 1, name = 'Test', description = 'description', address = 'address', creator = user)
		permission = CustomPermission.objects.create(id = 1, name = 'Can add role', codename = 'role_create')
		role = Role(id = 1, name = 'test', organization = organization)
		role.permissions.set({permission})
		role.save()
		service = Service.objects.create(id = 1, name = 'Test', address = 'number', number = '+79967364916', organization = organization)
		client = Client.objects.create(id = 1, user = user, organization = organization)


	def testOrganizationSerializer(self):
		#OrganizationSerializer for list
		organization_serializer = OrganizationSerializer()

		self.assertEquals(organization_serializer.fields['creator'].__class__, UserSerializer)
		self.assertEquals(organization_serializer.Meta.fields, ['id','name','description', 'address', 'creator', 'created_at', 'updated_at'])
		self.assertEquals(organization_serializer.Meta.model, Organization)

		#OrganizationSerializer for create
		org_data = {
			'name':'Relevant organization',
			'discription':'Clowns',
			'address':'Austria',
			'creator':1
		}
		organization_serializer_create = organization_serializer.OrganizationCSerializer(data = org_data)

		self.assertEquals(organization_serializer_create.Meta.fields, ['name','description', 'address', 'creator'])
		self.assertEquals(organization_serializer_create.Meta.model, Organization)

		self.assertTrue(organization_serializer_create.is_valid())
		self.assertEquals(organization_serializer_create.errors, {})



	def testOrganization_numberSerializer(self):
		#Organization_numberSerializer for list
		organization_number_serializer = Organization_numberSerializer()

		self.assertEquals(organization_number_serializer.fields['organization'].__class__, OrganizationSerializer)
		self.assertEquals(organization_number_serializer.Meta.fields, ['id','number','organization', 'created_at', 'updated_at'])
		self.assertEquals(organization_number_serializer.Meta.model, Organization_number)

		#Organization_numberSerializer for create
		org_number_data = {
			'number':'+79185245612',
			'organization':1
		}
		organization_number_serializer_create = organization_number_serializer.Organization_numberCSerializer(data = org_number_data)

		self.assertEquals(organization_number_serializer_create.Meta.fields, ['number','organization'])
		self.assertEquals(organization_number_serializer_create.Meta.model, Organization_number)

		self.assertTrue(organization_number_serializer_create.is_valid())
		self.assertEquals(organization_number_serializer_create.errors, {})


	def testOrganization_linkSerializer(self):
		#Organization_linkSerializer for list
		organization_link_serializer = Organization_linkSerializer()

		self.assertEquals(organization_link_serializer.fields['organization'].__class__, OrganizationSerializer)
		self.assertEquals(organization_link_serializer.Meta.fields, ['id','name', 'link','organization', 'created_at', 'updated_at'])
		self.assertEquals(organization_link_serializer.Meta.model, Organization_link)

		#Organization_linkSerializer for create
		org_link_data = {
			'name':'vk',
			'link':'http://vk.com',
			'organization':1
		}
		organization_link_serializer_create = organization_link_serializer.Organization_linkCSerializer(data = org_link_data)

		self.assertEquals(organization_link_serializer_create.Meta.fields, ['name', 'link','organization'])
		self.assertEquals(organization_link_serializer_create.Meta.model, Organization_link)

		self.assertTrue(organization_link_serializer_create.is_valid())
		self.assertEquals(organization_link_serializer_create.errors, {})


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
		self.assertEquals(service_serializer.Meta.fields, ['id', 'name', 'address', 'number', 'organization', 'created_at', 'updated_at'])
		self.assertEquals(service_serializer.Meta.model, Service)

		#ServiceSerializer for create
		org_service_data = {
			'name':'Test service',
			'address':'Neznau',
			'number':'+79185245612',
			'organization':1
		}
		service_serializer_create = service_serializer.ServiceCSerializer(data = org_service_data)

		self.assertEquals(service_serializer_create.Meta.fields, ['name', 'address', 'number', 'organization'])
		self.assertEquals(service_serializer_create.Meta.model, Service)

		self.assertTrue(service_serializer_create.is_valid())
		self.assertEquals(service_serializer_create.errors, {})


	def testOrderSerializer(self):
		#OrderSerializer for list
		order_serializer = OrderSerializer()

		self.assertEquals(order_serializer.fields['creator'].__class__, UserSerializer)
		self.assertEquals(order_serializer.fields['executor'].__class__, UserSerializer)
		self.assertEquals(order_serializer.fields['service'].__class__, ServiceSerializer)

		self.assertEquals(order_serializer.Meta.fields, ['id', 'order_code', 'description', 'creator', 'executor', 'client', 'done', 'blocked', 'service', 'created_at', 'updated_at'])
		self.assertEquals(order_serializer.Meta.model, Order)

		#OrderSerializer for create
		org_order_data = {
			'order_code':1234212,
			'description':'test',
			'client':1,
			'creator':1,
			'executor':1,
			'service':1
		}
		order_serializer_create = order_serializer.OrderCSerializer(data = org_order_data)

		self.assertEquals(order_serializer_create.Meta.fields, ['order_code', 'description', 'creator', 'executor', 'client', 'service'])
		self.assertEquals(order_serializer_create.Meta.model, Order)

		self.assertTrue(order_serializer_create.is_valid())
		self.assertEquals(order_serializer_create.errors, {})



	def tearDown(self):
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