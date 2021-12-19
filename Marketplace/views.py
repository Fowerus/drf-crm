import jwt

from django.contrib.auth import get_user_model

from rest_framework import status, permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
from restapi.customPerm import *



class MCourierListAPIView(generics.ListAPIView):
	permissions = [CustomPermissionVerificationRole]
	queryset = MCourier.objects.all()
	serializer = MCourierSerializer

	def get_queryset(self):
		return self.queryset.filter(organization__contains({'id': self.kwargs.get('organization')}))


class MCourierCreateAPIView(generics.CreateAPIView):
	permissions = [CustomPermissionVerificationRole]
	serializer = MCourierSerializer.MCourierCSerializer


class MCourierDestroyAPIView(generics.DestroyAPIView):
	permissions = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	queryset = MCourier.objects.all()
	lookup_field = '_id'