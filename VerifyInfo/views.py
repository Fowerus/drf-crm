from django.core.mail import send_mail
from django.conf import settings

from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from Users.models import User
from Clients.models import Client
from crm.views import get_userData

from .models import *



class UserVerifyInfoSendEmailAPIView(APIView):
	permission_classes = [permissions.AllowAny]

	def post(self, requests):
		try:
			user_data = get_userData(requests)
			user = User.objects.get(id = user_data['user_id'])
			if not user.confirmed_email:
				try:
					current_info = VerifyInfoUser.objects.filter(user = user.id).get(type_code = 'email')
					current_info.raw_code
				except:
					try:
						current_info = VerifyInfoUser(user = user, type_code = 'email')
						current_info.raw_code
					except:
						return Response(status = status.HTTP_500_INTERNAL_SERVER_ERROR)

				message = f'Введите это куда надо, а куда не надо не вводите (-_-).\n\n{current_info.code}'

			else:
				return Response({'detail':'Already confirmed'}, status = status.HTTP_200_OK)
		except:
			return Response({'detail':'Invalid token or not exist'}, status = status.HTTP_400_BAD_REQUEST)

		try:
			send_mail(
				'Test app',
				message, 
				settings.EMAIL_HOST_USER,
				[user.email],
				fail_silently=False
			)
			current_info.save()
		except:
			return Response({'detail':'Cannot send the mail'}, status = status.HTTP_500_INTERNAL_SERVER_ERROR)

		return Response(status = status.HTTP_200_OK)




class UserVerifyInfoAcceptAPIView(APIView):
	permission_classes = [permissions.AllowAny]

	def post(self, requests):
		try:
			user_data = get_userData(requests)

			user = User.objects.get(id = user_data['user_id'])
			verify_info = VerifyInfoUser.objects.filter(type_code = requests.data['type_code']).filter(user = user.id).get(code = requests.data['code'])

			if requests.data['type_code'] == 'phone':
				user.confirmed_phone = True
			else:
				user.confirmed_email = True

			user.save()
			verify_info.delete()
			return Response({'detail':'Successfully confirmed'}, status = status.HTTP_200_OK)
 
		except:
			return Response({'detail':'Invalid code or not exist'}, status = status.HTTP_400_BAD_REQUEST)




class ClientVerifyInfoAcceptAPIView(APIView):
	permission_classes = [permissions.AllowAny]

	def post(self, requests):
		try:
			user_data = get_userData(requests)

			client = Client.objects.get(id = user_data['client_id'])
			verify_info = VerifyInfoClient.objects.filter(client = client.id)
			client.confirmed_number = True
			client.save()
			verify_info.delete()
			return Response({'detail':'Successfully confirmed'}, status = status.HTTP_200_OK)

		except:
			return Response({'error':'Invalid code or not exist'}, status = status.HTTP_400_BAD_REQUEST)
			
