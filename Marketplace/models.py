from django.contrib.auth import get_user_model
from django.core.validators import URLValidator
from django import forms

from djongo import models

from Organizations.forms import MOrganizationForm, MOrganization_memberForm
from Users.forms import MUserForm

from Organizations.models import Organization

from restapi.views import script_injection



class MarketMainMixin(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


	class Meta:
		abstract = True



class MProduct(MarketMainMixin):
	_id = models.ObjectIdField()
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	count = models.IntegerField(verbose_name = 'Count')
	price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Price')
	price_opt = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Wholesale price')
	url_product = models.URLField(validators=[URLValidator, script_injection], verbose_name = 'Product url')
	url_photo = models.URLField(validators=[URLValidator, script_injection], verbose_name = 'Photo url')
	address = models.CharField(max_length = 300, verbose_name = 'Address')
	provider_site = models.CharField(max_length = 300, verbose_name = 'MProvider')
	
	organization = models.JSONField(verbose_name = 'Organization')

	objects = models.DjongoManager()

	def __str__(self):
		return f'_id: {self._id} | name: {self.name} | price: {self.price}'


	class Meta:
		db_table = 'mproduct'
		verbose_name_plural = 'MPoducts'
		verbose_name = 'MPoduct'
		ordering  = ['-created_at']


class MProductForm(forms.ModelForm):
	organization = forms.JSONField()

	class Meta:
		model = MProduct
		fields = ['name', 'count', 'price',
		'url_product', 'url_photo', 'address', 'provider_site', 'organization']




class MBusket(MarketMainMixin):
	_id = models.ObjectIdField()
	count = models.IntegerField(verbose_name = 'Count')
	price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Price')

	products = models.ArrayReferenceField(to = MProduct, verbose_name = 'Products')
	author = models.JSONField(verbose_name = 'Author')

	organization = models.JSONField(verbose_name = 'Organization')

	objects = models.DjongoManager()

	def __str__(self):
		return f'_id: {self._id} | products: {len(self.products)} items'


	class Meta:
		db_table = 'mbusket'
		verbose_name_plural = 'MBuskets'
		verbose_name = 'MBusket'
		ordering  = ['-created_at']


class MBusketForm(forms.ModelForm):
	author = forms.JSONField()
	organization = forms.JSONField()

	class Meta:
		model = MBusket
		fields = ['count', 'price', 'products', 'author', 'organization']




class MCourier(MarketMainMixin):
	_id = models.ObjectIdField()
	
	courier = models.JSONField(verbose_name = 'Courier')
	organization = models.JSONField(verbose_name = 'Organization')

	objects = models.DjongoManager()

	def __str__(self):
		return f'_id: {self._id}'


	class Meta:
		db_table = 'mcourier'
		verbose_name_plural = 'MCouriers'
		verbose_name = 'MCourier'
		ordering = ['-created_at']


class MCourierForm(forms.ModelForm):
	courier = forms.JSONField()
	organization = forms.JSONField()

	class Meta:
		model = MCourier
		fields = ['courier', 'organization']




class MOrder(MarketMainMixin):
	_id = models.ObjectIdField()
	price = models.DecimalField(max_digits = 10, decimal_places = 2, verbose_name = 'Price')
	address = models.CharField(max_length = 150, verbose_name = 'Address')
	description = models.CharField(max_length = 5000, verbose_name = 'Description')
	comment = models.CharField(max_length = 1000, verbose_name = 'Comment')

	products = models.ArrayReferenceField(to = MProduct, verbose_name = 'Products')
	courier = models.EmbeddedField(model_container = MCourier, verbose_name = 'Courier')

	author = models.JSONField(verbose_name = 'Author')
	organization = models.JSONField(verbose_name = 'Organization')

	objects = models.DjongoManager()

	def __str__(self):
		return f'_id: {self._id} | products: {len(self.products)} items'


	class Meta:
		db_table = 'morder'
		verbose_name_plural = 'MOrders'
		verbose_name = 'MOrder'
		ordering = ['-created_at']


class MOrderForm(forms.ModelForm):
	organization = forms.JSONField()
	courier = forms.JSONField()

	class Meta:
		model = MOrder
		fields = ['_id','price', 'address', 'description', 'comment', 'author', 'products', 'courier', 'organization']