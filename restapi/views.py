import jwt
from bson.objectid import ObjectId

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.conf import settings
from django.shortcuts import render

from Users.models import User
from Organizations.models import Organization
from Sessions.models import Session_user, Session_client 
from Handbook.models import OrderHistory, ActionHistory
from Marketplace.models import MCourier

from restapi.atomic_exception import MyCustomError



def index_home(request):
    return render(request, 'base.html', {})


# #Blocking injections
# def script_injection(value):
#     if value.find('<script>') != -1:
#         raise ValidationError(_('Script injection in %(value)s'),
#                               params={'value': value})


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
    try:
        if requests.method == 'GET':
            organization = requests._request.resolver_match.kwargs.get('organization')
        else:
            if type(requests.data['organization']) == list:
                organization = requests.data['organization'][0]
            elif type(requests.data['organization']) == dict:
                organization = requests.data['organization'].get('id')
            else:
                organization = requests.data['organization']

        return organization
    except:
        raise MyCustomError('The organization field is required', 400)


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
            member_role = current_org.organization_members.all().get(user = user_id).role
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


#Create OrderHistory
def create_orderHistory(method, model, order, organization, body = None):
    action_history = ActionHistory.objects.filter(model = model).get(method = method)

    order_history = OrderHistory.objects.create(action_history = action_history, order = order, organization = organization, data = body)

    return order_history


# <Client>---------------------------------------------------------------

#Checking an organizaions's client
def check_orgClient(client_id, org_id):
    return Organization.objects.get(id = org_id).organization_clients.all().filter(id = client_id).exists()


#Checking an organizaions's ClientCard
def check_orgClientCard(client_id, org_id):
    return Organization.objects.get(id = org_id).organization_client_card.all().filter(id = client_id).exists()


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


#Checking an Executor
def check_orgExecutor(executor_id, org_id):
    return bool(check_confirmed(executor_id) and check_orgMember(executor_id, org_id))


# <Market>---------------------------------------------------------------

#Checking an organizaions's cashbox
def check_orgCashbox(cashbox_id, org_id):
    return Organization.objects.get(id = org_id).organization_cashbox.all().filter(id = cashbox_id).exists() 

#Checking an organizaions's purchase
def check_orgPurchase(purchase_id, org_id):
    return Organization.objects.get(id = org_id).organization_purchase.all().filter(id = purchase_id).exists() 


#Checking an organization's saleProduct
def check_orgSaleProduct(saleproduct_id, org_id):
    return Organization.objects.get(id = org_id).organization_sale_product.all().filter(id = saleproduct_id).exists() 


#Checking an organization's saleOrder
def check_orgSaleOrder(saleorder_id, org_id):
    return Organization.objects.get(id = org_id).organization_sale_order.all().filter(id = saleorder_id).exists()


#Checking an organization's product
def check_orgProduct(product_id, org_id):
    return Organization.objects.get(id = org_id).organization_product.all().filter(id = product_id).exists()


#Checking an organization's ProductOrder
def check_orgProductOrder(productorder_id, org_id):
    return Organization.objects.get(id = org_id).organization_product_order.all().filter(id = productorder_id).exists()


#Checkign an organization's WorkDone
def check_orgWorkDone(workdone_id, org_id):
    return Organization.objects.get(id = org_id).organization_work_done.all().filter(id = workdone_id).exists()


#Checking an organization's PurchaseRequest
def check_orgPurchaseRequest(purchaserequest_id, org_id):
    return Organization.objects.get(id = org_id).organization_purchase_request.all().filter(id = purchaserequest_id).exists()


#Checking an organization's PurchaseAccept
def check_orgPurchaseAccept(purchaseaccept_id, org_id):
    return Organization.objects.get(id = org_id).organization_purchase_accept.all().filter(id = purchaseaccept_id).exists()


# <Marketplace>----------------------------------------------------------

#Checking an organization's MCourier
def check_orgMCourier(mcourier_id, org_id):
    return MCourier.objects.filter(_id = ObjectId(mcourier_id)).filter(organization = {'id':org_id}).exists()




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
    'clientcard': check_orgClientCard,
    'executor': check_orgExecutor,
    'order': check_orgOrder,
    'role':check_orgRole,
    'service':check_orgService,
    'organization_member':check_orgMember,
    'purchaserequest':check_orgPurchaseRequest,
    'purchaseaccept':check_orgPurchaseAccept,
    'serviceprice':check_orgServicePrice,
    'purchase':check_orgPurchase,
    'saleproduct':check_orgSaleProduct,
    'saleorder':check_orgSaleOrder,
    'productorder':check_orgProductOrder,
    'workdone':check_orgWorkDone,
    'cashbox':check_orgCashbox,
    'order_status':check_orgOrderStatus,
    'product': check_orgProduct,
    'devicetype':check_orgDeviceType,
    'devicemaker':check_orgDeviceMaker,
    'devicemodel':check_orgDeviceModel,
    'devicekit':check_orgDeviceKit,
    'deviceappearance':check_orgDeviceAppearance,
    'devicedefect':check_orgDeviceDefect,
    'mcourier':check_orgMCourier
}   