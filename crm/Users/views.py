import jwt
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



# class Registration(APIView):
# 	def get(self, requests):
# 		token = requests.headers['Authorization'].split(' ')[1]
# 		token = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
# 		print(token)
# 		return Response(status = status.HTTP_200_OK)



# not a client users
class Registration(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, requests):
        serializer = self.serializer_class(data = requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serialzier.data, status = status.HTTP_201_CREATE)

        return Response(status = status.HTTP_400_BAD_REQUEST)



class Login(APIView):
    serializer_class = UserLoginSerializer

    def post(self, requests):
        serializer = self.serializer_class(data = requests.data)
        if serializer.is_valid():

            return Response(serializer.data, status = status.HTTP_200_OK)

        return Response(status = status.HTTP_400_BAD_REQUEST)