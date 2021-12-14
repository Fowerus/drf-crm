from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

from Sessions.serializers import *
from Clients.serializers import ClientSerializer



class TestSessionsSerializers(APITestCase):

	def testSession_userSerializer(self):
		session_serializer = Session_userSerializer()

		self.assertEquals(session_serializer.fields['user'].__class__, UserSerializer)

		self.assertEquals(session_serializer.Meta.fields, ['id', 'user', 'device'])
		self.assertEquals(session_serializer.Meta.model, Session_user)


	def testSession_userSerializer(self):
		session_serializer = Session_clientSerializer()

		self.assertEquals(session_serializer.fields['client'].__class__, ClientSerializer)

		self.assertEquals(session_serializer.Meta.fields, ['id', 'client', 'device'])
		self.assertEquals(session_serializer.Meta.model, Session_client)
		