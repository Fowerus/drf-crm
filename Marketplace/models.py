from djongo import models



class MarketMainMixin(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


	class Meta:
		abstract = True



class MProduct(MarketMainMixin):
	_id = models.ObjectIdField()
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	count = models.IntegerField(verbose_name = 'Count')
	price = models.FloatField(null = True, verbose_name = 'Price')
	price_opt = models.FloatField(null = True, verbose_name = 'Wholesale price')
	url_product = models.CharField(max_length = 300, verbose_name = 'Product url')
	url_photo = models.CharField(max_length = 300, verbose_name = 'Photo url')
	address = models.CharField(max_length = 300, verbose_name = 'Address')
	organization = models.IntegerField(verbose_name = 'Organization')


	class Meta:
		db_table = 'mproduct'
		verbose_name_plural = 'Marketplace products'
		verbose_name = 'Marketplace product'