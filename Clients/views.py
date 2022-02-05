from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions

from .serializers import *
from .models import Client
from core.utils.customPerm import CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation, CustomPermissionCheckRelated

from core.views import *
from core.utils.customPerm import CustomPermissionGetUser
from Orders.serializers import OrderSerializer
from Users.serializers import UserSerializer

from core.utils.customGet_object import *


class ClientLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientLoginSerializer

    def post(self, requests):
        try:
            data = dict(requests.data)
            data['device'] = requests.headers['User-Agent']

            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ClientUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [CustomPermissionGetUser]
    queryset = Client.objects.all()
    lookup_field = 'id'
    serializer_class = ClientSerializer.ClientUSerializer


class ClientCardListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = ClientCard.objects.all()
    serializer_class = ClientCardSerializer

    def get_queryset(self):
        if 'phone' in self.kwargs:
            return self.queryset.select_related('organization').filter(organization=self.kwargs.get(
                'organization')).filter(phone=self.kwargs.get('phone'))

        elif 'fio' in self.kwargs:
            return self.queryset.select_related('organization').filter(organization=self.kwargs.get(
                'organization')).filter(name=self.kwargs.get('fio'))
        else:
            return self.queryset.select_related('organization').filter(organization=self.kwargs.get('organization'))


class ClientCardCreateAPIView(generics.CreateAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    queryset = ClientCard.objects.all()
    serializer_class = ClientCardSerializer.ClientCardCSerializer


class ClientCardRetrieveAPIView(CustomGetObject, generics.RetrieveAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    lookup_field = 'id'
    queryset = ClientCard.objects.all()
    serializer_class = ClientCardSerializer


class ClientCardUpdateAPIView(CustomGetObject, generics.UpdateAPIView, generics.DestroyAPIView):
    permission_classes = [CustomPermissionVerificationRole, CustomPermissionCheckRelated]
    lookup_field = 'id'
    queryset = ClientCard.objects.all()
    serializer_class = ClientCardSerializer.ClientCardUSerializer
