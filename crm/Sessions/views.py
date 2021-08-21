from rest_framework.viewsets import ViewSet
from rest_framework  import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import *
from crm.views import *



class SessionAPIView(APIView):
	serializer_class = SessionSerializer

	def get(self, requests):
		if check_authHeader(requests):
			user_data = get_userData(requests)
			try:
				all_session = Organization.objects.filter(user = user_data['user_id'])
				serializer = self.serializer_class(all_session, many = True)	

				return Response(serializer.data, status = status.HTTP_200_OK)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status = status.HTTP_401_UNAUTHORIZED)


	def delete(self, requests):
		if check_authHeader(requests):
			try:
				Session.objects.get(id = requests.data['session']).delete()
				return Response(status = status.HTTP_200_OK)
			except:
				return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status = status.HTTP_401_UNAUTHORIZED)
