import uuid
import datetime
from django.core.mail import send_mail
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
from core.views import *
from core.utils.customPerm import *


class MyCustomToken(TokenViewBase):

    def post(self, requests, *args, **kwargs):
        data = requests.data.copy()
        headers = requests.headers.copy()
        data['device'] = headers['user-agent']

        if 'phone' in requests.data and 'email' not in requests.data:
            data['email'] = '@'
            serializer = MyTokenObtainPairPhoneSerializer(data=data)
        elif 'email' in requests.data and 'phone' not in requests.data:
            serializer = MyTokenObtainPairEmailSerializer(data=data)
        else:
            serializer = MyTokenObtainPairAllSerializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
            if 'detail' in serializer.data:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data | {'expired_at': settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds}, status=status.HTTP_200_OK)


class MyCustomTokenForRefresh(TokenViewBase):

    def post(self, requests, *args, **kwargs):
        data = requests.data.copy()
        headers = requests.headers.copy()
        data['device'] = headers['user-agent']

        serializer = self.get_serializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
            if 'detail' in serializer.data:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
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
        if 'phone' in requests.data and 'email' not in requests.data:
            serializer = UserRegistrationSerializer.UserRegistrationForPhone(
                data=requests.data)
        elif 'email' in requests.data and 'phone' not in requests.data:
            serializer = UserRegistrationSerializer.UserRegistrationForEmail(
                data=requests.data)
        else:
            serializer = UserRegistrationSerializer(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [CustomPermissionGetUser]
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer


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


class TestSendEmail(APIView):
    def post(self, request):
        try:
            email = request.POST['email']
            message = request.POST['message']
            key = request.POST['key']
            if key != '789456':
                return Response(status=status.HTTP_400_BAD_REQUEST)

            print(f'sent to {email}')
            res = send_mail(
                'Test app', f'{message}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            print(f'count sent {res}')

        except Exception as err:
            return Response({'detail': f'Cannot send the mail, ERR_MESSAGE: {err}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_200_OK)
