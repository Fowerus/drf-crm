from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .serializers import *
from crm.views import *
from crm.customPerm import CustomPermissionGetUser



class Session_userListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionGetUser]
	queryset = Session_user.objects.all()
	serializer_class = Session_userSerializer

	def get_queryset(self):
		return self.queryset.filter(user = self.kwargs['id'])


class Session_userDestroyAPIView(generics.DestroyAPIView):
	permission_classes = [CustomPermissionGetUser]
	lookup_field = 'id'
	queryset = Session_user.objects.all()



class Session_clientListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionGetUser]
	queryset = Session_user.objects.all()
	serializer_class = Session_clientSerializer

	def get_queryset(self):
		return self.queryset.filter(client = self.kwargs['id'])


class Session_clientDestroyAPIView(generics.DestroyAPIView):
	permission_classes = [CustomPermissionGetUser]
	lookup_field = 'id'
	queryset = Session_user.objects.all()