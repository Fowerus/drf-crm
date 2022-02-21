from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions

from .serializers import *
from .models import Client
from core.utils.customPerm import CustomPermissionVerificationRole, CustomPermissionCheckRelated

from core.views import *
from core.utils.customPerm import CustomPermissionGetUser
from Orders.serializers import OrderSerializer
from Users.serializers import UserSerializer

from core.utils.customViewMethods import *


class ClientLoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientLoginSerializer

    def post(self, request):
        try:
            data = dict(request.data)
            data['device'] = request.headers['User-Agent']

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


class ClientCardListAPIView(CustomFilterQueryset, generics.ListAPIView):
    permission_classes = [CustomPermissionVerificationRole]
    queryset = ClientCard.objects.all()
    serializer_class = ClientCardSerializer
    filterset_fields = ['phone', 'email', 'service__id']


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
