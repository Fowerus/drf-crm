import jwt
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response



#Сheckштп the Authorization key in requests.headers
def check_authHeader(requests):
	return 'Authorization' in requests.headers


#Get information about user from access token
def get_userData(requests):
	access_token = requests.headers['Authorization'].split(' ')[1]
	access_token_decode = jwt.decode(access_token, settings.SECRET_KEY, algorithms = [settings.SIMPLE_JWT['ALGORITHM']])
	return access_token_decode


#Checking the required permissions
def check_ReqPerm(role, permissions:list):
	for i in role.permissions:
		pass


#Member rule confirmation
def is_valid_member(user_id, org_id, permissions:list):
	org_member = Organization_member.objects.filter(organization = org_id).get(user = user_id)
	return check_ReqPerm(org_member, permissions)