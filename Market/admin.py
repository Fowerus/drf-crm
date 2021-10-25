from django.contrib import admin
from .models import *


admin.site.register(ProductCategory)
admin.site.register(ProductOrder)
admin.site.register(Product)
admin.site.register(Cashbox)
admin.site.register(PurchaseRequest)
admin.site.register(PurchaseAccept)
admin.site.register(SaleProduct)
admin.site.register(SaleOrder)
admin.site.register(WorkDone)
admin.site.register(Transaction)
