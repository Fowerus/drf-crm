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


class MyTokenObtainPairView(TokenViewBase):

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        headers = request.headers.copy()
        data['device'] = headers['user-agent']

        if 'code' in request.data:
            data['password'] = '#'

        if 'phone' in request.data:
            data['email'] = '@'
        elif 'email' in request.data:
            data['phone'] = '+'

        serializer = MyTokenObtainPairSerializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
            if 'detail' in serializer.data:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data | {'expired_at': settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds}, status=status.HTTP_200_OK)


class MyCustomTokenForRefresh(TokenViewBase):

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        headers = request.headers.copy()
        data['device'] = headers['user-agent']

        serializer = MyTokenRefreshSerializer(data=data)

        try:
            serializer.is_valid(raise_exception=True)
            if 'detail' in serializer.data:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data | {'expired_at': settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds}, status=status.HTTP_200_OK)



class MyTokenRefreshView(MyCustomTokenForRefresh):
    serializer_class = MyTokenRefreshSerializer


class UserRegistrationAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        if 'phone' in request.data and 'email' not in request.data:
            serializer = UserRegistrationSerializer.UserRegistrationForPhone(
                data=request.data)
        elif 'email' in request.data and 'phone' not in request.data:
            serializer = UserRegistrationSerializer.UserRegistrationForEmail(
                data=request.data)
        else:
            serializer = UserRegistrationSerializer(data=request.data)
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

    def patch(self, request, **kwargs):
        self.serializer_class = UserSerializer.UserUSerializer
        return super().patch(request, kwargs)

    def put(self, request, **kwargs):
        self.serializer_class = UserSerializer.UserUSerializer
        return super().put(request, kwargs)


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
