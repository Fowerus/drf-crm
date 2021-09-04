import jwt
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Organizations.models import *
from Clients.models import *
from Users.models import User
from rest_framework import permissions
from Organizations.models import *
from Sessions.models import Session_user, Session_client 



#Get information about user from access token
def get_userData(requests):
	try:
		access_token = requests.headers['Authorization'].split(' ')[1].strip()
		access_token_decode = jwt.decode(access_token, settings.SECRET_KEY, algorithms = [settings.SIMPLE_JWT['ALGORITHM']])

		Session_user.objects.filter(user = access_token_decode['user_id']).get(device = requests.headers['user-agent'])

		return access_token_decode

	except:
		return None



def get_clientData(requests):
	try:
		access_token = requests.headers['Authorization'].split(' ')[1].strip()
		access_token_decode = jwt.decode(access_token, settings.SECRET_KEY, algorithms = [settings.SIMPLE_JWT['ALGORITHM']])

		Session_client.objects.filter(client = access_token_decode['client_id']).get(device = requests.headers['user-agent'])

		return access_token_decode

	except:
		return None


#Checking the required permissions
def check_ReqPerm(role, permissions:list):
	for i in role.permissions.all():
		for j in permissions:
			if j == i.codename:
				return True

	return False


def check_confirmed(user_id):
	try:
		user = User.objects.get(id = user_id)
		return user.confirmed
	except:
		return False


#Member rule confirmation
def is_valid_member(user_id, org_id, permissions:list):
	try:
		if check_confirmed(user_id):
			current_org = Organization.objects.get(id = org_id)
			if user_id == current_org.creator.id:
				return True

			member_role	= current_org.organization_members.all().get(user = user_id).role
			return check_ReqPerm(member_role, permissions)
		return False
	except:
		return False


#User verification for work in the organization
def check_orgMember(member_id, org_id):
	try:
		current_member = Organization.objects.get(id = org_id).organization_members.all().get(id = member_id)
		return True
	except:
		return False


#Checking the role of an organization
def check_orgRole(role_id, org_id):
	try:
		current_role = Organization.objects.get(id = org_id).organization_roles.all().get(id = role_id)
		return True
	except:
		return False


#Checking the service of organizaion
def check_orgService(service_id, org_id):
	try:
		current_service = Organization.objects.get(id = org_id).organization_services.all().get(id = service_id)
		return True
	except:
		return False


#Checking an organizaions's order
def check_orgOrder(order_id, org_id):
	try:
		current_order = Order.objects.get(id = order_id)
		if current_order.service.organization.id == org_id:
			return True

		return False

	except:
		return False


#Checking an organizaions's client
def check_orgClient(client_id, org_id):
	try:
		current_client = Organization.objects.get(id = org_id).organization_clients.all().get(id = client_id)
		return True
	except:
		return False


def get_viewName(view):
	view_name = view.__class__.__name__
	
	if 'RetrieveUpdateDestroyAPIView' in view_name:
		view_name = view_name.lower()[:view_name.index('RetrieveUpdateDestroyAPIView')]
	if 'ListCreateAPIView' in view_name:
		view_name = view_name.lower()[:view_name.index('ListCreateAPIView')]
	elif 'CreateAPIView' in view_name:
		view_name = view_name.lower()[:view_name.index('CreateAPIView')]
	elif 'ListAPIView' in view_name:
		view_name = view_name.lower()[:view_name.index('ListAPIView')]
	elif 'RetrieveAPIView' in view_name:
		view_name = view_name.lower()[:view_name.index('RetrieveAPIView')]
	elif 'UpdateAPIView' in view_name:
		view_name = view_name.lower()[:view_name.index('UpdateAPIView')]

	return view_name