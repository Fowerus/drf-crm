from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from django.conf import settings
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import TokenError

from .serializers import *
from crm.views import *
from Organizations.serializers import OrderSerializer



class MyCustomToken(TokenViewBase):

    def post(self, requests, *args, **kwargs):
        data = requests.data.copy()
        headers = requests.headers.copy()
        data['device'] = headers['User-Agent']
        serializer = self.get_serializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
            if 'error' in serializer.data:
                return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data | {'expire_at': settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds}, status=status.HTTP_200_OK)



class MyTokenObtainPairView(MyCustomToken):
    serializer_class = MyTokenObtainPairSerializer



class MyTokenRefreshView(MyCustomToken):
    serializer_class = MyTokenRefreshSerializer
    

class UserRegistration(APIView):
    serializer_class = UserRegistrationSerializer

    def registration_user(self, requests):
        try:
            serializer = self.serializer_class(data = requests.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = status.HTTP_201_CREATED)

            return Response(status = status.HTTP_400_BAD_REQUEST)
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


    def delete_user(self, requests):
        user_data = get_userData(requests)
        if not check_UsrClient(user_data['user_id']):
            try:
                User.objects.get(order_code = requests.data['order_code']).delete()

                return Response(status = status.HTTP_200_OK)

            except:
                return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status = status.HTTP_403_FORBIDDEN)