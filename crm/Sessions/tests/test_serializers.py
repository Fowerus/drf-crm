from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

from Sessions.serializers import *



class TestSessionsSerializers(APITestCase):

	def testSessionSerializer(self):
		session_serializer = SessionSerializer()

		self.assertEquals(session_serializer.fields['user'].__class__, UserSerializer)

		self.assertEquals(session_serializer.Meta.fields, ['id', 'user', 'device'])
		self.assertEquals(session_serializer.Meta.model, Session)