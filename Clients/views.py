from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from .serializers import *
from .models import Client
from crm.customPerm import CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionCheckRelated

from crm.views import *
from crm.customPerm import CustomPermissionGetUser
from Orders.serializers import OrderSerializer
from Users.serializers import UserSerializer



class ClientLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientLoginSerializer

    def post(self, requests):
        try:
            data = dict(requests.data)
            data['device'] = requests.headers['User-Agent']

            serializer = self.serializer_class(data = data)
            if serializer.is_valid():
                return Response(serializer.data, status = status.HTTP_200_OK)
            
            return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST)




class ClientListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        return self.queryset.filter(organization = self.kwargs.get('organization'))


class ClientCreateAPIView(generics.CreateAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    serializer_class = ClientSerializer.ClientCSerializer


class ClientRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
    lookup_field = 'id'
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = Client.objects.all()
    serializer_class = ClientSerializer.ClientUSerializer
    