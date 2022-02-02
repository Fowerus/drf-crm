from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .serializers import *
from core.views import *
from core.utils.customPerm import CustomPermissionSession
from .models import *


class Session_userListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionSession]
    queryset = Session_user.objects.all()
    serializer_class = Session_userSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.kwargs['id'])


class Session_userDestroyAPIView(APIView):

    def delete(self, requests, **kwargs):
        try:
            user = get_userData(requests)
            if 'id' in kwargs:
                session = Session_user.objects.get(id=kwargs['id'])
                if session.user.id == user['user_id']:
                    session.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)

                return Response({'detail': 'You can close only your session'}, status=status.HTTP_400_BAD_REQUEST)

            else:
                session = Session_user.objects.get(id=user['session'])
                session.delete()

                return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'detail': 'Session does not exist or problem on the server'}, status=status.HTTP_400_BAD_REQUEST)


class Session_clientListAPIView(generics.ListAPIView):
    permission_classes = [CustomPermissionSession]
    queryset = Session_client.objects.all()
    serializer_class = Session_clientSerializer

    def get_queryset(self):
        return self.queryset.filter(client=self.kwargs['id'])


class Session_clientDestroyAPIView(APIView):

    def delete(self, requests, **kwargs):
        try:
            client = get_clientData(requests)
            if 'id' in kwargs:
                session = Session_client.objects.get(id=kwargs['id'])
                if session.client.id == client['client_id']:
                    session.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)

                return Response({'detail': 'You can close only your session'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                session = Session_client.objects.get(id=client['session'])
                session.delete()

                return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'detail': 'Session does not exist or problem on the server'}, status=status.HTTP_400_BAD_REQUEST)
