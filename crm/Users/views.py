from rest_framework.viewsets import ViewSet
from rest_framework import status
from django.conf import settings
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import *
from crm.views import *
from Organizations.serializers import OrderSerializer
# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyOTUxNTczMSwianRpIjoiZmIxMWEzZTNjZGI2NDI0MTk2YWI0OGQ5MmFmMWQxYjkiLCJ1c2VyX2lkIjoyfQ.NpqsAxf2vhMS57xMOBV3g1GN4Xm2oWH-dGl0Clo3uBg",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwNTUyNTMxLCJqdGkiOiI1NThmNDE0MjgxMGE0MDBiODI2OGIxNTE0Yzc2ODQyYSIsInVzZXJfaWQiOjJ9.ZGG4NtbrpH-Srz7oEapSoWIQ8z_c_BiOYra5ed2cKhw",
#     "expire_at": 0
# }


class MyCustomToken(TokenViewBase):

    def post(self, requests, *args, **kwargs):
        requests.data['device'] = requests.headers['User-Agent']
        serializer = self.get_serializer(data=requests.data)

        try:
            serializer.is_valid(raise_exception=True)
            if 'error' in serializer.data:
                return Response(status = status.HTTP_400_BAD_REQUEST)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data | {'expire_at': settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds}, status=status.HTTP_200_OK)



class MyTokenObtainPairView(MyCustomToken):
    serializer_class = MyTokenObtainPairSerializer



class MyTokenRefreshView(MyCustomToken):
    serializer_class = MyTokenRefreshSerializer
    


# not a client users
class UserViewSet(ViewSet):
    serializer_class = UserRegistrationSerializer

    def registration_user(self, requests):
        serializer = self.serializer_class(data = requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATE)

        return Response(status = status.HTTP_400_BAD_REQUEST)


    def list_user_executorOrders(self, requests):
        if check_authHeader(requests):
            user_data = get_userData(requests)

            try:
                orders = User.objects.get(id = user_data['user_id']).user_executor.all()
                serializer = OrderSerializer(orders, many = True)

                return Response(serializer.data, status = status.HTTP_200_OK)

            except:
                return Response(status = status.HTTP_400_BAD_REQUEST)

        return Response(status = status.HTTP_401_UNAUTHORIZED)


    def update_user(self, requests):
        if check_authHeader(requests):
            user_data = get_userData(requests)

            try:
                if not check_UsrClient(user_data['user_id']):
    
                    current_user = User.objects.get(id = 1)

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


                    if len(output['success']) > 0:
                        current_org.save()

                    return Response(output, status = status.HTTP_200_OK)

                else:
                    return Response(status = status.HTTP_403_FORBIDDEN)

            except:
                return Response(status = status.HTTP_400_BAD_REQUEST)

        return Response(status = status.HTTP_401_UNAUTHORIZED)


    def delete_user(self, requests):
        if check_authHeader(requests):
            user_data = get_userData(requests)
            if not check_UsrClient(user_data['user_id']):
                try:
                    User.objects.get(order_code = requests.data['order_code']).delete()

                    return Response(status = status.HTTP_200_OK)

                except:
                    return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response(status = status.HTTP_403_FORBIDDEN)

        return Response(status = status.HTTP_401_UNAUTHORIZED)