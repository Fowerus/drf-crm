from django.contrib.auth import get_user_model

from rest_framework import status, permissions
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import *

from Handbook.models import *
from crm.customPerm import *
