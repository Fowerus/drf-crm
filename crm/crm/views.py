import jwt
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response



#Сhecking the Authorization key in requests.headers
def check_authHeader(requests):
	return 'Authorization' in requests.headers


#Get information about user from access token
def get_userData(requests):
	access_token = requests.headers['Authorization'].split(' ')[1]
	access_token_decode = jwt.decode(access_token, settings.SECRET_KEY, algorithms = [settings.SIMPLE_JWT['ALGORITHM']])
	return access_token_decode


#Сhecking a user as a member of an organization or its creator
def check_memberships(user_id):
	try:
		user = get_user_model().objects.get(id = user_id)
		user_member = user.user_member.all()
		user_creator = user.my_organizations.all()

		if user_member or user_creator:
			return True

		return False
	except:
		return False


#Checking the required permissions
def check_ReqPerm(role, permissions:list):
	for i in role.permissions.all():
		for j in permissions:
			if j == i.name:
				return True

	return False


#Member rule confirmation
def is_valid_member(user_id, org_id, permissions:list):
	try:
		current_org = Organization.objects.get(id = org_id)
		if user_id == current_org.creator.id:
			return True

		member_role	= current_org.organization_members.all().get(user = user_id).role
		return check_ReqPerm(member_role, permissions)
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
def check_memOrg(member_id, org_id):
	try:
		current_link = Organization.objects.get(id = org_id).organization_members.all().filter(id = member_id)
		if current_link:
			return True

		return False

	except:
		return False


#Checking the role of an organization
def check_orgRole(role_id, org_id):
	try:
		current_link = Organization.objects.get(id = org_id).organization_roles.all().filter(id = role_id)
		if current_link:
			return True

		return False

	except:
		return False