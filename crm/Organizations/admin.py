from django.contrib import admin

from Organizations.models import *
from django.contrib.auth.models import Permission



admin.site.register(Organization)
admin.site.register(Organization_link)
admin.site.register(Organization_number)
admin.site.register(CustomPermission)
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(Organization_member)
admin.site.register(Service)