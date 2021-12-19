import jwt
from bson.objectid import ObjectId

from django.contrib.auth import get_user_model

from rest_framework import status, permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
from restapi.customPerm import *



class MCourierListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = MCourier.objects.all()
	serializer_class = MCourierSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = {'id':self.kwargs.get('organization')})


class MCourierCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = MCourierSerializer.MCourierCSerializer


class MCourierDestroyAPIView(generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	queryset = MCourier.objects.all()
	lookup_field = '_id'

	def delete(self, requests, _id, **kwargs):
		try:
			self.queryset.get(_id = ObjectId(_id)).delete()
			return Response(status = status.HTTP_204_NO_CONTENT)
		except:
			return Response(status = status.HTTP_404_NOT_FOUND)