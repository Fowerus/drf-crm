import jwt
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework import status
from django.conf import settings
from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import *
# {
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyOTUxNTczMSwianRpIjoiZmIxMWEzZTNjZGI2NDI0MTk2YWI0OGQ5MmFmMWQxYjkiLCJ1c2VyX2lkIjoyfQ.NpqsAxf2vhMS57xMOBV3g1GN4Xm2oWH-dGl0Clo3uBg",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwNTUyNTMxLCJqdGkiOiI1NThmNDE0MjgxMGE0MDBiODI2OGIxNTE0Yzc2ODQyYSIsInVzZXJfaWQiOjJ9.ZGG4NtbrpH-Srz7oEapSoWIQ8z_c_BiOYra5ed2cKhw",
#     "expire_at": 0
# }


class MyCustomToken(TokenViewBase):

    def post(self, requests, *args, **kwargs):
        serializer = self.get_serializer(data=requests.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data | {'expire_at': settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].seconds}, status=status.HTTP_200_OK)


class MyTokenObtainPairView(MyCustomToken):
    serializer_class = TokenObtainPairSerializer



class MyTokenRefreshView(MyCustomToken):
    serializer_class = MyTokenRefreshSerializer
    


# not a client users
class Registration(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self, requests):
        serializer = self.serializer_class(data = requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATE)

        return Response(status = status.HTTP_400_BAD_REQUEST)



# class Login(APIView):
#     serializer_class = UserLoginSerializer

#     def post(self, requests):
#         serializer = self.serializer_class(data = requests.data)
#         if serializer.is_valid():

#             return Response(serializer.data, status = status.HTTP_200_OK)

#         return Response(status = status.HTTP_400_BAD_REQUEST)