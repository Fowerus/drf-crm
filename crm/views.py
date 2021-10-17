import jwt
from django.conf import settings

from Users.models import User
from Organizations.models import Organization
from Sessions.models import Session_user, Session_client 
from Handbook.models import OrderHistory, ActionHistory

from crm.atomic_exception import MyCustomError



#Get information about user from access token
def get_userData(requests):
	access_token = requests.headers['Authorization'].split(' ')[1].strip()
	access_token_decode = jwt.decode(access_token, settings.SECRET_KEY, algorithms = [settings.SIMPLE_JWT['ALGORITHM']])

	Session_user.objects.filter(user = access_token_decode['user_id']).get(device = requests.headers['user-agent'])

	return access_token_decode


#Get information about client from token
def get_clientData(requests):
	access_token = requests.headers['Token'].split(' ')[1].strip()
	access_token_decode = jwt.decode(access_token, settings.SECRET_KEY, algorithms = [settings.SIMPLE_JWT['ALGORITHM']])

	Session_client.objects.filter(client = access_token_decode['client_id']).get(device = requests.headers['user-agent'])

	return access_token_decode


#Get organization id
def get_orgId(requests):
	if requests.method == 'GET':
		organization = requests._request.resolver_match.kwargs.get('organization')
	else:
		if type(requests.data['organization']) == list:
			organization = requests.data['organization'][0]
		else:
			organization = requests.data['organization']

	return organization


#Checking the required permissions
def check_ReqPerm(role, permissions:list):
	for i in role.permissions.all():
		for j in permissions:
			if j == i.codename:
				return True

	return False


def check_confirmed(user_id):
	return User.objects.get(id = user_id).confirmed


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


# <Organization>---------------------------------------------------------

#User verification for work in the organization
def check_orgMember(member_id, org_id):
	return Organization.objects.get(id = org_id).organization_members.all().filter(id = member_id).exists()


#Checking the role of an organization
def check_orgRole(role_id, org_id):
	return Organization.objects.get(id = org_id).organization_roles.all().filter(id = role_id).exists()


#Checking the service of organizaion
def check_orgService(service_id, org_id):
	return Organization.objects.get(id = org_id).organization_services.all().filter(id = service_id).exists()


# <Order>----------------------------------------------------------------

#Checking an organizaions's order
def check_orgOrder(order_id, org_id):
	return Organization.objects.get(id = org_id).organization_orders.all().filter(id = order_id).exists()


#Checking an organization's order status
def check_orgOrderStatus(order_status_id, org_id):
	return Organization.objects.get(id = org_id).organization_order_status.all().filter(id = order_status_id).exists()


# <Client>---------------------------------------------------------------

#Checking an organizaions's client
def check_orgClient(client_id, org_id):
	return Organization.objects.get(id = org_id).organization_clients.all().filter(id = client_id).exists()


# <Handbook>-------------------------------------------------------------

#Checking an organizaions's device type
def check_orgDeviceType(devicetype_id, org_id):
	return Organization.objects.get(id = org_id).organization_device_type.all().filter(id = devicetype_id).exists()


#Checking an organizaions's device maker
def check_orgDeviceMaker(devicemaker_id, org_id):
	return Organization.objects.get(id = org_id).organization_device_maker.all().filter(id = devicemaker_id).exists()


#Checking an organizaions's device model
def check_orgDeviceModel(devicemodel_id, org_id):
	return Organization.objects.get(id = org_id).organization_device_model.all().filter(id = devicemodel_id).exists()


#Checking an organizaions's device kit
def check_orgDeviceKit(devicekit_id, org_id):
	return Organization.objects.get(id = org_id).organization_device_kit.all().filter(id = devicekit_id).exists()


#Checking an organizaions's device appearance
def check_orgDeviceAppearance(deviceappearance_id, org_id):
	return Organization.objects.get(id = org_id).organization_device_appearance.all().filter(id = deviceappearance_id).exists()


#Checking an organizaions's device defect
def check_orgDeviceDefect(devicedefect_id, org_id):
	return Organization.objects.get(id = org_id).organization_device_defect.all().filter(id = devicedefect_id).exists()


#Checking an organizaions's service price
def check_orgServicePrice(serviceprice_id, org_id):
	return Organization.objects.get(id = org_id).organization_service_price.all().filter(id = serviceprice_id).exists()


# <Market>---------------------------------------------------------------

#Checking an organizaions's cashbox
def check_orgCashbox(cashbox_id, org_id):
	return Organization.objects.get(id = org_id).organization_cashbox.all().filter(id = cashbox_id).exists() 

#Checking an organizaions's purchase
def check_orgPurchase(purchase_id, org_id):
	return Organization.objects.get(id = org_id).organization_purchase.all().filter(id = purchase_id).exists() 


#Checking an organizaions's sale
def check_orgSale(sale_id, org_id):
	return Organization.objects.get(id = org_id).organization_sale.all().filter(id = sale_id).exists() 


def check_orgProduct(product_id, org_id):
	return Organization.objects.get(id = org_id).organization_product.all().filter(id = product_id).exists()


def check_orgExecutor(executor_id, org_id):
	return bool(check_confirmed(executor_id) and check_orgMember(executor_id, org_id))


#Create OrderHistory


#Get view name without prifex(like ListAPIView)
def get_viewName(view):
	view_name = view.__class__.__name__

	if 'Serializer' in view_name:
		return view_name.lower()[:view_name.index('Serializer')-1].capitalize()

	elif 'RetrieveUpdateDestroyAPIView' in view_name:
		return view_name.lower()[:view_name.index('RetrieveUpdateDestroyAPIView')]
		
	elif 'ListCreateAPIView' in view_name:
		return view_name.lower()[:view_name.index('ListCreateAPIView')]

	elif 'CreatorListAPIView' in view_name:
		return view_name.lower()[:view_name.index('CreatorListAPIView')]

	elif 'UpdateDestroyAPIView' in view_name:
		return view_name.lower()[:view_name.index('UpdateDestroyAPIView')]

	elif 'CreateAPIView' in view_name:
		return view_name.lower()[:view_name.index('CreateAPIView')]

	elif 'ListAPIView' in view_name:
		return view_name.lower()[:view_name.index('ListAPIView')]

	elif 'RetrieveAPIView' in view_name:
		return view_name.lower()[:view_name.index('RetrieveAPIView')]

	elif 'UpdateAPIView' in view_name:
		return view_name.lower()[:view_name.index('UpdateAPIView')]

	elif 'DestroyAPIView' in view_name:
		return view_name.lower()[:view_name.index('DestroyAPIView')]
		



#List with all functions in crm.views.py
validate_func_map = {
	'client': check_orgClient,
	'executor': check_orgExecutor,
	'product': check_orgProduct,
	'order': check_orgOrder,
	'role':check_orgRole,
	'service':check_orgService,
	'organization_member':check_orgMember,
	'serviceprice':check_orgServicePrice,
	'purchase':check_orgPurchase,
	'sale':check_orgSale,
	'cashbox':check_orgCashbox,
	'order_status':check_orgOrderStatus,
	'devicetype':check_orgDeviceType,
	'devicemaker':check_orgDeviceMaker,
	'devicemodel':check_orgDeviceModel,
	'devicekit':check_orgDeviceKit,
	'deviceappearance':check_orgDeviceAppearance,
	'devicedefect':check_orgDeviceDefect,
}	