import uuid
import datetime

from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import TokenError

from .serializers import *
from .models import VerifyInfo
from crm.views import *
from Organizations.serializers import OrderSerializer
# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzMDk0NDIyNSwianRpIjoiNWZiODNhMTAwOWNhNGU4MGEwOTA2NGRmZmM3YTIyYWEiLCJ1c2VyX2lkIjoxfQ.r3w64dIiadUeBSkI8tq0JF_w7RHNap9ipVBFi1Vv5dA",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwOTQ0MjI1LCJqdGkiOiI1MjA2YzM3ZmY3N2E0ZTI2YWRlNzMxZjhhNmFmZmZlNCIsInVzZXJfaWQiOjF9.n77Jy2pXfEbmF3HiMjPAUZX8a-M02MVJheuGwfdVP60",
#     "expire_at": 0
# }

class MyCustomToken(TokenViewBase):

    def post(self, requests, *args, **kwargs):
        print(reverse('organization'))
        data = requests.data.copy()
        headers = requests.headers.copy()
        data['device'] = headers['user-agent']

        if 'email' in requests.data:
            serializer = MyTokenObtainPairEmailSerializer(data=data)

        else:
            data['email'] = '@'
            serializer = MyTokenObtainPairNumberSerializer(data = data)

        try:
            serializer.is_valid(raise_exception=True)
            if 'detail' in serializer.data:
                return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data | {'expired_at': settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds}, status=status.HTTP_200_OK)



class MyCustomTokenForRefresh(TokenViewBase):

    def post(self, requests, *args, **kwargs):
        data = requests.data.copy()
        headers = requests.headers.copy()
        data['device'] = headers['user-agent']

        serializer = self.get_serializer(data = data)

        try:
            serializer.is_valid(raise_exception=True)
            if 'detail' in serializer.data:
                return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        except TokenError as e:
            print('sdfdsf')
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data | {'expired_at': settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds}, status=status.HTTP_200_OK)



class MyTokenObtainPairView(MyCustomToken):
    pass



class MyTokenRefreshView(MyCustomTokenForRefresh):
    serializer_class = MyTokenRefreshSerializer
    

class UserRegistrationViewSet(ViewSet):
    permission_classes = [permissions.AllowAny]

    def registration_user(self, requests):
        try:
            if 'number' in requests.data and not 'email' in requests.data:
                serializer = UserRegistrationSerializer.UserRegistrationForNumber(data = requests.data)
            elif 'email' in requests.data and not 'number' in requests.data:
                serializer = UserRegistrationSerializer.UserRegistrationForEmail(data = requests.data)
            else:
                serializer = UserRegistrationSerializer(data = requests.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)

            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)


class UserViewSet(ViewSet):

    def information_about_user(self, requests):
        try:
            user_data = get_userData(requests)
            user = User.objects.get(id = user_data['user_id'])
            my_info = UserSerializer(user)

            return Response(my_info.data, status = status.HTTP_200_OK)

        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)



    def list_user_executorOrders(self, requests):
        try:
            user_data = get_userData(requests)
            orders = User.objects.get(id = user_data['user_id']).user_executor.all()
            serializer = OrderSerializer(orders, many = True)

            return Response(serializer.data, status = status.HTTP_200_OK)

        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)


    def update_user(self, requests):
        try:
            user_data = get_userData(requests)
            if not check_UsrClient(user_data['user_id']):

                current_user = User.objects.get(id = user_data['user_id'])

                output = {
                    'success':{},
                    'error':{}
                }

                if 'surname' in requests.data:
                    if 2 <= requests.data['surname'] <= 150:
                        current_user.surname = requests.data['surname']
                        output['success']['Surname'] = 'Surname successfully changed'
                    else:
                        output['error']['Surname'] = 'Surname is too short or too long'

                if 'name' in requests.data:
                    if 2 <= requests.data['name'] <= 150:
                        current_user.name = requests.data['name']
                        output['success']['Name'] = 'Name successfully changed'
                    else:
                        output['error']['Name'] = 'Name is too short or too long'

                if 'patronymic' in requests.data:
                    if 2 <= requests.data['patronymic'] <= 150:
                        current_user.patronymic = requests.data['patronymic']
                        output['success']['Patronymic'] = 'Patronymic successfully changed'
                    else:
                        output['error']['Patronymic'] = 'Patronymic is too short or too long'

                if 'address' in requests.data:
                    if 2 <= requests.data['address'] <= 150:
                        current_user.address = requests.data['address']
                        output['success']['Address'] = 'Address successfully changed'
                    else:
                        output['error']['Address'] = 'Address is too short or too long'

                if 'image' in requests.data:
                    if 2 <= requests.data['image'] <= 150:
                        current_user.image = requests.data['image']
                        output['success']['Image'] = 'Image successfully changed'
                    else:
                        output['error']['Image'] = 'Wrong image format'

                if 'email' in requests.data:
                    try:
                        current_user.email = requests.data['email']
                        output['success']['Email'] = 'Email successfully changed'
                        current_user.confirmed_email = False
                    except:
                        output['error']['Email'] = 'Wrong email format'


                if 'number' in requests.data:
                    try:
                        current_user.email = requests.data['number']
                        output['success']['Number'] = 'Number successfully changed'
                        current_user.confirmed_number = False
                    except:
                        output['error']['Number'] = 'Wrong number format'


                if len(output['success']) > 0:
                    current_user.save()

                return Response(output, status = status.HTTP_200_OK)

            else:
                return Response(status = status.HTTP_403_FORBIDDEN)

        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)


    def delete_user(self, requests):
        user_data = get_userData(requests)
        if not check_UsrClient(user_data['user_id']):
            try:
                User.objects.get(order_code = requests.data['order_code']).delete()

                return Response(status = status.HTTP_200_OK)

            except:
                return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status = status.HTTP_403_FORBIDDEN)



class VerifyNumberEmailViewSet(ViewSet):

    def verify_email_send(self, requests):
        try:
            user_data = get_userData(requests)
            user = User.objects.get(id = user_data['user_id'])
            if not user.confirmed_email:
                try:
                    current_info = VerifyInfo.objects.filter(user = user_data['user_id']).get(type_code = 'email')
                    current_info.code = int(str(uuid.uuid1().int)[:6])
            
                except:
                    try:
                        current_info = VerifyInfo(user = user, type_code = 'email', code = int(str(uuid.uuid1().int)[:6]))
                    except:
                        return Response(status = status.HTTP_400_BAD_REQUEST)

                link_to_verify = str(requests._current_scheme_host) + str(reverse('accept_email')) + str(current_info.code)
                message = f'Перейдите по ссылке для подтверждения вашей почты\n{link_to_verify}'

            return Response({'detail':'Already confirmed'}, status = status.HTTP_200_OK)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)

        try:
            send_mail(
                'Test app',
                message, 
                settings.EMAIL_HOST_USER,
                [current_info.user.email],
                fail_silently=False
            )
            current_info.save()
        except:
            return Response({'detail':'Unsuccessful code submission'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status = status.HTTP_200_OK)



    def accept_email(self, requests, code):
        try:
            user_data = get_userData(requests)
            try:
                user = User.objects.get(id = user_data['user_id'])
                verify_info = VerifyInfo.objects.get(code = code)
                if verify_info.user.id == user.id:
                    user = User.objects.get(id = user_data['user_id'])
                    user.confirmed_email = True
                    user.save()
                    verify_info.delete()
                    return Response({'detail':'Successfully confirmed'}, status = status.HTTP_200_OK)
            except:
                return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)


    def verify_number_send(self, requests):
        pass