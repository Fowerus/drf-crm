from django.http.response import JsonResponse
from django.db.models import Count


import uuid
import jwt
from bson.objectid import ObjectId

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from django.conf import settings
from django.shortcuts import render

from Users.models import User
from Organizations.models import Organization, Organization_member, Service
from Sessions.models import Session_user, Session_client
from Handbook.models import OrderHistory, ActionHistory
from Marketplace.models import MCourier, MProduct, MBusket, MOrder

from core.utils.atomic_exception import MyCustomError
from .models.postgres_models import Post
from .tasks import create_random_posts


def post_generator(request):
    v = create_random_posts.delay()
    print(v)
    return JsonResponse({"success": f'{v}'})


def post_test(request):
    v = Post.objects.all().aggregate(Count('id'))
    print(v)
    return JsonResponse({"success": f'{v}'})
######################################


def index_home(request):
    return render(request, 'base.html', {})


# #Blocking injections
# def script_injection(value):
#     if value.find('<script>') != -1:
#         raise ValidationError(_('Script injection in %(value)s'),
#                               params={'value': value})


# Get information about user from access token
def get_userData(requests):
    try:
        access_token = requests.headers['Authorization'].split(' ')[1].strip()
        access_token_decode = jwt.decode(access_token, settings.SECRET_KEY, algorithms=[
                                         settings.SIMPLE_JWT['ALGORITHM']])

        Session_user.objects.select_related('user').filter(
            user=access_token_decode['user_id']).get(device=requests.headers['user-agent'])
        return access_token_decode
    except Exception as e:
        raise MyCustomError('The `Authorization` header is required', 400)


# Get information about client from token
def get_clientData(requests):
    try:
        access_token = requests.headers['Token'].split(' ')[1].strip()
        access_token_decode = jwt.decode(access_token, settings.SECRET_KEY, algorithms=[
                                         settings.SIMPLE_JWT['ALGORITHM']])

        Session_client.objects.select_related('client').filter(
            client=access_token_decode['client_id']).get(device=requests.headers['user-agent'])

        return access_token_decode
    except Exception as e:
        raise MyCustomError('The `Token` header is required', 400)


# Get information about mprovider from token
def get_mproviderData(requests):
    try:
        access_token = requests.headers['Token'].split(' ')[1].strip()
        access_token_decode = jwt.decode(access_token, settings.SECRET_KEY, algorithms=[
                                         settings.SIMPLE_JWT['ALGORITHM']])

        return access_token_decode
    except Exception as e:
        raise MyCustomError('The `Token` header is required', 400)


# Get organization id
def get_orgId(requests):
    try:
        if requests.method == 'GET':
            organization = requests._request.resolver_match.kwargs.get(
                'organization')
        else:
            if type(requests.data['organization']) == list:
                organization = requests.data['organization'][0]
            elif type(requests.data['organization']) == dict:
                organization = requests.data['organization'].get('id')
            else:
                organization = requests.data['organization']

        return organization
    except Exception as e:
        raise MyCustomError('The organization field is required', 400)


# Get author data
def get_authorData(author_user_id:int, org_id:int, **kwargs):
    organization_member = Organization_member.objects.select_related(
        'organization', 'user').filter(organization=org_id).filter(user=author_user_id)

    if organization_member.exists():
        return organization_member.values()[0]

    raise MyCustomError('Organization_member does not exist', 400)


# Get organization data
def get_organizationData(org_id:int):
    organization = Organization.objects.filter(id=org_id)

    if organization.exists():
        return organization.values()[0]

    raise MyCustomError('Organization does not exist', 400)


# Get service data
def get_serviceData(service_id:int):
    service = Service.objects.filter(id = service_id)

    if service.exists():
        return service.values()[0]

    raise MyCustomError('Service does not exist', 400)


# Get products data
def get_productsData(products:list, **kwargs):
    new_product = []
    providers = []
    for product in products:
        try:
            mproduct = MProduct.objects.get(_id=ObjectId(product.get('_id')))
        except Exception as e:
            raise MyCustomError(
                f"The product with _id `{product.get('_id')}` does not exist", 400)

        if product.get('count') > mproduct.count or product.get('count') < 0:
            raise MyCustomError(
                f"The quantity of product with _id `{product.get('_id')}` is not enough", 400)
        try:
            item = {
                "_id": mproduct._id,
                "count": product.get('count'),
                "name": mproduct.name,
                "price": mproduct.price,
                "price_opt": mproduct.price_opt,
                "url_product": mproduct.url_product,
                "url_photo": mproduct.url_photo,
                "address": mproduct.address,
                "provider_site": mproduct.provider_site,
                "organization": mproduct.organization,
                "service": mproduct.service
            }
            if kwargs.get('is_order'):
                item['done'] = False
                mproduct.count -= item.get('count')
                mproduct.save()

            providers.append(mproduct.organization.get('id'))

            new_product.append(item)

        except Exception as e:
            raise MyCustomError(
                "Creation product list error (Did you add the count field into each dict in array?)", 400)

    return new_product, list(set(providers))


# Get courier data
def get_courierData(mcourier_data, providers, org_id:int, **kwargs):
    mcourier = MCourier.objects.filter(_id=ObjectId(mcourier_data.get('_id')))
    if mcourier.exists() and (mcourier.first().organization.get('id') in providers or mcourier.first().organization.get('id') == org_id):
        return {
            "_id": mcourier.first()._id,
            "organization": mcourier.first().organization,
            "member": mcourier.first().member,
            "service": mcourier.first().service
        }

    raise MyCustomError('Courier does not exist', 400)


# Accept order point
def accept_orderPoint(done_list:list, products:list, count_success:int):
    try:
        for item in done_list:

            for product in products:
                if item == product.get('_id'):
                    mproduct = MProduct.objects.get(
                        _id=ObjectId(product.get('_id')))

                    if not product['done']:
                        product['done'] = True
                        count_success += 1

        return products, count_success

    except Exception as e:
        raise MyCustomError('Product id in done_list does not exist', 400)


# Calculate order price and item count
def calculate_orderPriceAndCount(products:list):
    try:
        price = 0
        count = 0
        for product in products:
            price += product.get('count') * product.get('price')
            count += 1

        return price, count
    except Exception as e:
        raise MyCustomError('Price and count calculation error', 500)


# Get organization member data
def get_organization_memberData(member_id:int, org_id:int, **kwargs):
    try:
        member = Organization.objects.get(
            id=org_id).organization_members.all().filter(id=member_id)
    except Exception as e:
        raise MyCustomError(
            'Member id field not supplied or Organization does not exist', 400)
    if member.exists():
        return member.values()[0]
    else:
        raise MyCustomError('Organization_member does not exist', 400)


def check_confirmed(user_id):
    return User.objects.get(id=user_id).confirmed


# <Organization>---------------------------------------------------------

# User verification for work in the organization
def check_orgMember(member_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_members.all().filter(id=member_id).exists()


# Checking the role of an organization
def check_orgRole(role_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_roles.all().filter(id=role_id).exists()


# Checking the service of organizaion
def check_orgService(service_id:int, org_id:int, **kwargs):
    return service_id in kwargs.get('requests').user.services


# Checking an organization's mprovider
def check_orgMProvider(mprovider_id:int, org_id:int):
    return Organization.objects.get(id=org_id).organization_mprovider.all().filter(id=mprovider_id).exists()


# <Order>----------------------------------------------------------------

# Checking an organizaions's order
def check_orgOrder(order_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_orders.all().filter(id=order_id).exists()


# Checking an organization's order status
def check_orgOrderStatus(order_status_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_order_status.all().filter(id=order_status_id).exists()


# Create OrderHistory
def create_orderHistory(method, model, order, organization, body=None):
    action_history = ActionHistory.objects.filter(
        model=model).get(method=method)

    order_history = OrderHistory.objects.create(
        action_history=action_history, order=order, organization=organization, data=body)

    return order_history


# <Client>---------------------------------------------------------------

# Checking an organizaions's client
def check_orgClient(client_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_clients.all().filter(id=client_id).exists()


# Checking an organizaions's ClientCard
def check_orgClientCard(client_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_client_card.all().filter(id=client_id).exists()


# <Handbook>-------------------------------------------------------------

# Checking an organizaions's device type
def check_orgDeviceType(devicetype_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_device_type.all().filter(id=devicetype_id).exists()


# Checking an organizaions's device maker
def check_orgDeviceMaker(devicemaker_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_device_maker.all().filter(id=devicemaker_id).exists()


# Checking an organizaions's device model
def check_orgDeviceModel(devicemodel_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_device_model.all().filter(id=devicemodel_id).exists()


# Checking an organizaions's device kit
def check_orgDeviceKit(devicekit_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_device_kit.all().filter(id=devicekit_id).exists()


# Checking an organizaions's device appearance
def check_orgDeviceAppearance(deviceappearance_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_device_appearance.all().filter(id=deviceappearance_id).exists()


# Checking an organizaions's device defect
def check_orgDeviceDefect(devicedefect_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_device_defect.all().filter(id=devicedefect_id).exists()


# Checking an organizaions's service price
def check_orgServicePrice(serviceprice_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_service_price.all().filter(id=serviceprice_id).exists()


# Checking an Executor
def check_orgExecutor(executor_id:int, org_id:int, **kwargs):
    return bool(check_confirmed(executor_id) and check_orgMember(executor_id, org_id))


# <Market>---------------------------------------------------------------

# Checking an organizaions's cashbox
def check_orgCashbox(cashbox_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_cashbox.all().filter(id=cashbox_id).exists()

# Checking an organizaions's purchase


def check_orgPurchase(purchase_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_purchase.all().filter(id=purchase_id).exists()


# Checking an organization's saleProduct
def check_orgSaleProduct(saleproduct_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_sale_product.all().filter(id=saleproduct_id).exists()


# Checking an organization's saleOrder
def check_orgSaleOrder(saleorder_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_sale_order.all().filter(id=saleorder_id).exists()


# Checking an organization's product
def check_orgProduct(product_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_product.all().filter(id=product_id).exists()


# Checking an organization's ProductOrder
def check_orgProductOrder(productorder_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_product_order.all().filter(id=productorder_id).exists()


# Checkign an organization's WorkDone
def check_orgWorkDone(workdone_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_work_done.all().filter(id=workdone_id).exists()


# Checking an organization's PurchaseRequest
def check_orgPurchaseRequest(purchaserequest_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_purchase_request.all().filter(id=purchaserequest_id).exists()


# Checking an organization's PurchaseAccept
def check_orgPurchaseAccept(purchaseaccept_id:int, org_id:int, **kwargs):
    return Organization.objects.get(id=org_id).organization_purchase_accept.all().filter(id=purchaseaccept_id).exists()


# <Marketplace>----------------------------------------------------------

# Checking an organization's MCourier
def check_orgMCourier(mcourier_id:int, org_id:int, **kwargs):
    return MCourier.objects.filter(_id=ObjectId(mcourier_id)).filter(organization={'id': org_id}).exists()


# Checking an organization's MProduct
def check_orgMProduct(mproduct_id:int, org_id:int, **kwargs):
    return MProduct.objects.filter(_id=ObjectId(mproduct_id)).filter(organization={'id': org_id}).exists()


# Checking an organization's MBusket
def check_orgMBusket(mbusket_id:int, org_id:int, **kwargs):
    return MBusket.objects.filter(_id=ObjectId(mbusket_id)).filter(organization={'id': org_id}).exists()


# Checking an organization's MOrder
def check_orgMOrder(morder_id:int, org_id:int, **kwargs):
    return MOrder.objects.filter(_id=ObjectId(morder_id)).filter(organization={'id': org_id}).exists()


# Checking an organization's MOrder for courier
def check_orgMOrderForCourier(morder_id:int, org_id:int, **kwargs):
    try:
        user_id = kwargs.get('requests').user.id
        member_id = MOrder.objects.get(_id=ObjectId(
            morder_id)).courier.get('courier').get('id')
        return Organization_member.objects.filter(id=member_id).filter(user__id=user_id).exists()
    except Exception as e:
        return False


# Checking an organization's mbusket and user's mbusket
def check_orgUserMBusket(mbusket_id:int, org_id:int, **kwargs):
    try:
        user_id = kwargs.get('requests').user.id
        member_id = Organization.objects.get(
            id=org_id).organization_members.all().filter(user__id=user_id)
        return MBusket.objects.get(_id=ObjectId(mbusket_id)).organization.get('id') == org_id
    except Exception as e:
        return False


# Checking an organization's morder and user's morder
def check_orgUserMOrder(morder_id:int, org_id:int, **kwargs):
    try:
        user_id = kwargs.get('requests').user.id
        member_id = Organization.objects.get(
            id=org_id).organization_members.all().filter(user__id=user_id)
        return MOrder.objects.get(_id=ObjectId(morder_id)).organization.get('id') == org_id
    except Exception as e:
        return False


#Extend the token with necessary fields
def extend_tokenFields(token, user, device:str, session:dict):
    try:
        token['first_name'] = user.first_name
        token['surname'] = user.surname
        token['second_name'] = user.second_name

        token['email'] = user.email
        token['phone'] = user.phone
        if user.phone is not None:
            token['phone'] = user.phone.raw_input

        token['session'] = session

        return token
    except:
        raise MyCustomError('Token extenstion error', 400)


#User code verification
def user_code_verification(user, field:str, code:int, password:str):
    confirmed_fields = {'email': user.confirmed_email, 'phone': user.confirmed_phone}

    if not confirmed_fields[field]:
        if code is not None:
            if not user.code_is_expired:

                if field == 'email':
                    user.confirmed_email = True
                elif field == 'phone':
                    user.confirmed_phone = True

                if user.code != int(code):
                    raise MyCustomError('Code is incorrect', 400)
                user.code = None
                user.code_expired_at = None
                user.save()
                return True

        user.send_code(field)
        raise MyCustomError('The account is not confirmed. Code sent', 400)
        
    if not user.check_password(password):
        raise MyCustomError('No active account found with the given credentials', 400)

    return True


# Get view name without prifex(like ListAPIView)
def get_viewName(view):
    if hasattr(view, 'perm_view_name'):
        return view.perm_view_name.lower()
    else:
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


# List with all functions in crm.views.py
validate_func_map = {
    'client': check_orgClient,
    'clientcard': check_orgClientCard,
    'executor': check_orgExecutor,
    'order': check_orgOrder,
    'role': check_orgRole,
    'service': check_orgService,
    'organization_member': check_orgMember,
    'purchaserequest': check_orgPurchaseRequest,
    'purchaseaccept': check_orgPurchaseAccept,
    'serviceprice': check_orgServicePrice,
    'purchase': check_orgPurchase,
    'saleproduct': check_orgSaleProduct,
    'saleorder': check_orgSaleOrder,
    'productorder': check_orgProductOrder,
    'workdone': check_orgWorkDone,
    'cashbox': check_orgCashbox,
    'order_status': check_orgOrderStatus,
    'product': check_orgProduct,
    'devicetype': check_orgDeviceType,
    'devicemaker': check_orgDeviceMaker,
    'devicemodel': check_orgDeviceModel,
    'devicekit': check_orgDeviceKit,
    'deviceappearance': check_orgDeviceAppearance,
    'devicedefect': check_orgDeviceDefect,
    'mprovider': check_orgMProvider,
    'courier': check_orgMCourier,
    'mproduct': check_orgMProduct,
    'mbusket': check_orgMBusket,
    'morder': check_orgMOrder,
    'morderforcourier': check_orgMOrderForCourier,
    'mbusketcourier': check_orgUserMBusket,
    'mordermcourier': check_orgUserMOrder,
    'member': check_orgMember
}
