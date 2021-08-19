import jwt
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import *
from crm.views import *
# {
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjMwNDE1OTI0LCJqdGkiOiJmYWRlOTkxZjNjYmU0ZWVkOWFkM2E0NzdmNzljOTAxNCIsInVzZXJfaWQiOjJ9.0ZQGq57AOHoy6CocQ4nxQ7pU7mvvvnZ25tyMlQeNgE4",
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyOTM3OTEyNCwianRpIjoiMjM0N2ZlZjE5YjIwNGRiNDk3ZmM4Y2NhNGY4YWQwNzYiLCJ1c2VyX2lkIjoyfQ.1WY1IZ0aZyFqm7NF51KmreU0htLpNI_IJa72wxENfMo",
#     "expire": 0
# }


class OrganizationAPIView(APIView):
	serializer_class = OrganizationSerializer

	def get(self, requests):
		if check_authHeader(requests):
			try:
				all_organizations = Organization.objects.all()
			except:
				return Response(status = status.HTTP_400_BAD_REQUEST)

			serializer = self.serializer_class(all_organizations, many = True)
			return Response(serializer.data, status = status.HTTP_200_OK)
		return Response(status, status = status.HTTP_401_UNAUTHORIZED)


	def post(self, requests):
		if check_authHeader(requests):
			serializer = self.serializer_class(data = requests.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serialzier.data, status = status.HTTP_201_CREATE)

			return Response(status = status.HTTP_400_BAD_REQUEST)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def patch(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)
			current_org = Organization.objects.get(id = requests.data['org_id'])
			if user_data['user_id'] == current_org.creator.id or is_valid_member(user_data['user_id'], current_org.id):

				return Response(status = status.HTTP_200_OK)