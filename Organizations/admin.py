from django.contrib import admin

from Organizations.models import *
from django.contrib.auth.models import Permission


admin.site.register(Organization)
admin.site.register(Permission)
admin.site.register(Organization_member)
admin.site.register(Service)
admin.site.register(MProvider)
admin.site.register(MyGroup)
