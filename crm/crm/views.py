import jwt
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response

from Organizations.models import *
from Clients.models import *



#Get information about user from access token
def get_userData(requests):
	access_token = requests.headers['Authorization'].split(' ')[1]
	access_token_decode = jwt.decode(access_token, settings.SECRET_KEY, algorithms = [settings.SIMPLE_JWT['ALGORITHM']])
	return access_token_decode


#Checking the required permissions
def check_ReqPerm(role, permissions:list):
	for i in role.permissions.all():
		for j in permissions:
			if j == i.name:
				return True

	return False


#Checking the user as a client
def check_UsrClient(user_id):
	try:
		if User.objects.get(user = user_id).user_client:
			return True
	except:
		return False


def check_confirmed(user_id):
	try:
		user = User.objects.get(id = user_id)
		return user.confirmed_number + user.confirmed_email
	except:
		return False


#Member rule confirmation
def is_valid_member(user_id, org_id, permissions:list):
	try:
		if not check_UsrClient(user_id) and check_confirmed(user_id):
			current_org = Organization.objects.get(id = org_id)
			if user_id == current_org.creator.id:
				return True

			member_role	= current_org.organization_members.all().get(user = user_id).role
			return check_ReqPerm(member_role, permissions)
		return False
	except:
		return False


#Checking the number of an organization
def check_orgNumber(number_id, org_id):
	try:
		current_number = Organization.objects.get(id = org_id).organization_numbers.all().filter(id = number_id)
		if current_number:
			return True

		return False

	except:
		return False


#Checking the link of an organization
def check_orgLink(link_id, org_id):
	try:
		current_link = Organization.objects.get(id = org_id).organization_links.all().filter(id = link_id)
		if current_link:
			return True

		return False

	except:
		return False


#User verification for work in the organization
def check_orgMember(member_id, org_id):
	try:
		current_member = Organization.objects.get(id = org_id).organization_members.all().filter(id = member_id)
		if current_member:
			return True

		return False

	except:
		return False


#Checking the role of an organization
def check_orgRole(role_id, org_id):
	try:
		current_role = Organization.objects.get(id = org_id).organization_roles.all().filter(id = role_id)
		if current_role:
			return True

		return False

	except:
		return False


#Checking the service of organizaion
def check_orgService(service_id, org_id):
	try:
		current_service = Organization.objects.get(id = org_id).organization_services.all().filter(id = service_id)
		if current_service:
			return True

		return False

	except:
		return False


#Checking a user as a client of organization
def check_orgClient(client_id, org_id):
	try:
		current_client = Organization.objects.get(id = org_id).organization_services.all().filter(id = client_id)
		if current_client:
			return True

		return False

	except:
		return False


#Checking an organizaions's order
def check_orgOrder(order_code, org_id):
	try:
		current_order = Order.objects.get(order_code = order_code)
		if current_order.service.organization.id == org_id:
			return True

		return False

	except:
		return False