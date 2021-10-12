from django.contrib import admin

from .models import *


admin.site.register(DeviceType)
admin.site.register(DeviceMaker)
admin.site.register(DeviceModel)
admin.site.register(DeviceKit)
admin.site.register(DeviceAppearance)
admin.site.register(DeviceDefect)
admin.site.register(ServicePrice)
admin.site.register(ActionHistory)
admin.site.register(OrderHistory)