from django.conf import settings

from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.response import Response

from .serializers import *
from crm.views import *
from Organizations.serializers import OrderSerializer



class ClientViewSet(ViewSet):

    def list_orders_as_client(self, requests):
        if check_authHeader(requests):
            user_data = get_userData(requests)

            try:
                client_orders = User.objects.get(id = user_data['user_id']).client_orders..all()
                serializer = OrderSerializer(client_orders, many = True)

                return Response(serializer.data, status = status.HTTP_200_OK)

            except:
                return Response(status = status.HTTP_400_BAD_REQUEST)

        return Response(status = status.HTTP_401_UNAUTHORIZED)


    def update_client(self, requests):
        try:
            user_data = get_userData(requests)
            if check_UsrClient(user_data['user_id']):

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