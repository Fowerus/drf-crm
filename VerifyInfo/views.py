from django.core.mail import send_mail
from django.conf import settings

from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from Users.models import User
from Clients.models import Client
from core.views import get_userData

from .models import *


class UserVerifyInfoSendEmailAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, requests):
        try:
            user_data = get_userData(requests)
            user = User.objects.get(id=user_data['user_id'])
            if not user.confirmed_email:
                try:
                    current_info = VerifyInfoUser.objects.select_related(
                        'user').filter(user=user.id).get(type_code='email')
                    current_info.raw_code
                except Exception as e:
                    try:
                        current_info = VerifyInfoUser(
                            user=user, type_code='email')
                        current_info.raw_code
                    except Exception as e:
                        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                message = f'Enter this code (-_-).\n\n{current_info.code}'

            else:
                return Response({'detail': 'Already confirmed'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': 'Invalid token or not exist'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            send_mail(
                'Test app',
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False
            )
            current_info.save()
        except Exception as err:
            return Response({'detail': f'Cannot send the mail, ERR_MESSAGE: {err}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_200_OK)


class UserResetPasswordAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, requests):
        try:
            user_data = get_userData(requests)
            user = User.objects.get(id=user_data['user_id'])
        except Exception as e:
            try:
                user = User.objects.get(email=requests.data['email'])
            except Exception as e:
                user = User.objects.get(phone=requests.data['phone'])
        try:
            current_info = VerifyInfoUser.objects.select_related(
                'user').filter(user=user.id).get(type_code='reset')
            current_info.raw_code
        except Exception as e:
            try:
                current_info = VerifyInfoUser(user=user, type_code='reset')
                current_info.raw_code
            except Exception as e:
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        message = f'Enter this code (-_-).\n\n{current_info.code}'

        try:
            send_mail(
                'Test app',
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False
            )
            current_info.save()
        except Exception as err:
            return Response({'detail': f'Cannot send the mail, ERR_MESSAGE: {err}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_200_OK)


class UserVerifyInfoAcceptAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, requests):
        try:
            try:
                user_data = get_userData(requests)
                user = User.objects.get(id=user_data['user_id'])
            except Exception as e:
                try:
                    user = User.objects.get(email=requests.data['email'])
                except Exception as e:
                    user = User.objects.get(phone=requests.data['phone'])

            verify_info = VerifyInfoUser.objects.select_related('user').filter(
                type_code=requests.data['type_code']).filter(user=user.id).get(code=requests.data['code'])

            if requests.data['type_code'] == 'phone':
                user.confirmed_phone = True
            elif requests.data['type_code'] == 'email':
                user.confirmed_email = True
            elif requests.data['type_code'] == 'reset':
                user.set_password(requests.data['password'])

            user.save()
            verify_info.delete()
            if requests.data['type_code'] == 'reset':
                return Response({'detail': 'Password changed'}, status=status.HTTP_200_OK)

            return Response({'detail': 'Successfully confirmed'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'detail': 'Invalid input data or not exist'}, status=status.HTTP_400_BAD_REQUEST)


class ClientVerifyInfoAcceptAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, requests):
        try:
            client_data = get_clientData(requests)

            client = Client.objects.get(id=client_data['client_id'])
            verify_info = VerifyInfoClient.objects.select_related(
                'client').filter(client=client.id)
            client.confirmed_number = True
            client.save()
            verify_info.delete()
            return Response({'detail': 'Successfully confirmed'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': 'Invalid input data or not exist'}, status=status.HTTP_400_BAD_REQUEST)
