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
                client = Client.objects.get(id = user_data['user_id']).client_orders.all()
                serializer = OrderSerializer(orders, many = True)

                return Response(serializer.data, status = status.HTTP_200_OK)

            except:
                return Response(status = status.HTTP_400_BAD_REQUEST)

        return Response(status = status.HTTP_401_UNAUTHORIZED)