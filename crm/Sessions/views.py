from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import *
from crm.views import *



class SessionAPIView(APIView):
	serializer_class = SessionSerializer

	def get(self, requests):
		try:
			user_data = get_userData(requests)
			all_session = Organization.objects.filter(user = user_data['user_id'])
			serializer = self.serializer_class(all_session, many = True)	

			return Response(serializer.data, status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)



	def delete(self, requests):
		try:
			user_data = get_userData(requests)
			current_session = Session.objects.get(id = requests.data['session'])
			if user_data['user_id'] == current_session.user.id:
				current_session.delete()
			return Response(status = status.HTTP_200_OK)
		except:
			return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)