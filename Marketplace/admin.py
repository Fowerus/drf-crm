from django.contrib import admin
from djongo import models

from .models import *



class MProductAdminForm(admin.ModelAdmin):
	form = MProductForm

class MBusketAdminForm(admin.ModelAdmin):
	form = MBusketForm

class MCourierAdminForm(admin.ModelAdmin):
	form = MCourierForm

class MOrderAdminForm(admin.ModelAdmin):
	form = MOrderForm


admin.site.register(MProduct, MProductAdminForm)
admin.site.register(MBusket, MBusketAdminForm)
admin.site.register(MCourier, MCourierAdminForm)
admin.site.register(MOrder, MOrderAdminForm)