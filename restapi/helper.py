from django.db import models


class MainMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
    updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')

    data = models.JSONField(null = True, blank = True)


    class Meta:
        abstract = True



def defaultMProviderData():
    return {
    "name":"name",
    "price":"price",
    "count":"available_all",
    "provider_site":"url",
    "url_product":"url",
    "url_photo":"picture",
    "address":"available"
    }
