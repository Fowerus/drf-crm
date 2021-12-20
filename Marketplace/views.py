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



class MProductListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = MProduct.objects.all()
	serializer_class = MProductSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = {'id':self.kwargs.get('organization')})


class MProductCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = MProductSerializer.MProductCSerializer


class MProductRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = '_id'
	queryset = MProduct.objects.all()
	serializer_class = MProductSerializer

	def retrieve(self, requests, _id, **kwargs):
		try:
			return Response(self.serializer_class(self.queryset.get(_id = ObjectId(_id))).data, status = status.HTTP_200_OK)
		except:
			return Response({}, status = status.HTTP_200_OK)


class MProductUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = '_id'
	queryset = MProduct.objects.all()
	serializer_class = MProductSerializer.MProductUSerializer

	def update(self, requests, _id, **kwargs):
		try:
			instance = self.queryset.get(_id = ObjectId(_id))
			serializer = self.serializer_class(data = requests.data)
			if serializer.is_valid():
				serializer.update(instance, serializer.validated_data)
				return Response(serializer.data, status = status.HTTP_200_OK)
			return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
		except:
			return Response(status = status.HTTP_404_NOT_FOUND)


	def delete(self, requests, _id, **kwargs):
		try:
			self.queryset.get(_id = ObjectId(_id)).delete()
			return Response(status = status.HTTP_204_NO_CONTENT)
		except:
			return Response(status = status.HTTP_404_NOT_FOUND)



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
	lookup_field = '_id'
	queryset = MCourier.objects.all()

	def delete(self, requests, _id, **kwargs):
		try:
			self.queryset.get(_id = ObjectId(_id)).delete()
			return Response(status = status.HTTP_204_NO_CONTENT)
		except:
			return Response(status = status.HTTP_404_NOT_FOUND)



class MOrderListAPIView(generics.ListAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	queryset = MProduct.objects.all()
	serializer_class = MProductSerializer

	def get_queryset(self):
		return self.queryset.filter(organization = {'id':self.kwargs.get('organization')})


class MOrderCreateAPIView(generics.CreateAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	serializer_class = MOrderSerializer.MOrderCSerializer


class MOrderRetrieveAPIView(generics.RetrieveAPIView):
	permission_classes = [CustomPermissionVerificationRole]
	lookup_field = '_id'
	queryset = MOrder.objects.all()
	serializer_class = MOrderSerializer

	def retrieve(self, requests, _id, **kwargs):
		try:
			return Response(self.serializer_class(self.queryset.get(_id = ObjectId(_id))).data, status = status.HTTP_200_OK)
		except:
			return Response({}, status = status.HTTP_200_OK)


class MOrderUpdateDestroyAPIView(generics.UpdateAPIView, generics.DestroyAPIView):
	permission_classes = [CustomPermissionVerificationRole, CustomPermissionVerificationAffiliation]
	lookup_field = '_id'
	queryset = MOrder.objects.all()
	serializer_class = MOrderSerializer.MOrderUSerializer

	def update(self, requests, _id, **kwargs):
		try:
			instance = self.queryset.get(_id = ObjectId(_id))
			serializer = self.serializer_class(data = requests.data)
			if serializer.is_valid():
				serializer.update()
				return Response(serializer.data, status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_404_NOT_FOUND)

	def delete(self, requests, _id, **kwargs):
		try:
			self.queryset.get(_id = ObjectId(_id)).delete()
			return Response(status = status.HTTP_204_NO_CONTENT)
		except:
			return Response(status = status.HTTP_404_NOT_FOUND)