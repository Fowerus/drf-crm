from django.contrib import admin
from .models import Session_user, Session_client


admin.site.register(Session_user)
admin.site.register(Session_client)
