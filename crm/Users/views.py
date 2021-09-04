import uuid
import datetime

from django.conf import settings
from django.urls import reverse

from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics

from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.exceptions import TokenError

from .serializers import *
from crm.views import *
from crm.customPerm import *
from Orders.serializers import OrderSerializer



class MyCustomToken(TokenViewBase):

    def post(self, requests, *args, **kwargs):
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
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data | {'expired_at': settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds}, status=status.HTTP_200_OK)



class MyTokenObtainPairView(MyCustomToken):
    pass



class MyTokenRefreshView(MyCustomTokenForRefresh):
    serializer_class = MyTokenRefreshSerializer
    

class UserRegistrationAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, requests):
        try:
            if 'number' in requests.data and not 'email' in requests.data:
                serializer = UserRegistrationSerializer.UserRegistrationForNumber(data = requests.data)
            elif 'email' in requests.data and not 'number' in requests.data:
                serializer = UserRegistrationSerializer.UserRegistrationForEmail(data = requests.data)
            else:
                serializer = UserRegistrationSerializer(data = requests.data)

            if serializer.is_valid():
                try:
                    serializer.save()
                    return Response(serializer.data, status = status.HTTP_201_CREATED)
                except:
                    pass
            return Response({'detail':'Valid number or email not provided'}, status = status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)




class UserExecutorListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionGetUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.queryset.get(id = self.kwargs.get('id')).user_executor.all()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [CustomPermissionGetUser]
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def patch(self, requests, **kwargs):
        self.serializer_class = UserSerializer.UserUSerializer
        return super().patch(requests, kwargs)

    def put(self, requests, **kwargs):
        self.serializer_class = UserSerializer.UserUSerializer
        return super().put(requests, kwargs)