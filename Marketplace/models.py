from bson.objectid import ObjectId

from django.contrib.auth import get_user_model
from django.core.validators import URLValidator, MinValueValidator
from django import forms

from djongo import models

from Organizations.forms import MOrganizationForm, MOrganization_memberForm
from Users.forms import MUserForm

from Organizations.models import Organization



class MarketMainMixin(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


	class Meta:
		abstract = True




class MProduct(MarketMainMixin):
	_id = models.ObjectIdField()
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	count = models.IntegerField(verbose_name = 'Count')
	price = models.FloatField(verbose_name = 'Price')
	price_opt = models.FloatField(verbose_name = 'Wholesale price')
	url_product = models.CharField(max_length = 300, verbose_name = 'Product url')
	url_photo = models.CharField(max_length = 300, verbose_name = 'Photo url')
	provider_site = models.CharField(max_length = 300, verbose_name = 'MProvider')

	address = models.JSONField(verbose_name = 'Address')
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
	address = forms.JSONField()

	class Meta:
		model = MProduct
		fields = ['name', 'count', 'price', 'price_opt',
		'url_product', 'url_photo', 'address', 'provider_site', 'organization']



class MBusket(MarketMainMixin):
	_id = models.ObjectIdField()
	count = models.IntegerField(verbose_name = 'Count')
	price = models.FloatField(verbose_name = 'Price')

	products = models.JSONField(verbose_name = 'Products')
	author = models.JSONField(verbose_name = 'Author')
	providers = models.JSONField(verbose_name = 'Providers')
	organization = models.JSONField(verbose_name = 'Organization')

	objects = models.DjongoManager()

	def __str__(self):
		return f'_id: {self._id} | products: {len(self.products)} items'

	@property
	def calculate_price(self):
		self.price = 0
		for product in self.products:
			self.price += product.get('count') * product.get('price')


	@property
	def calculate_count(self):
		self.count = len(self.products)
	


	class Meta:
		db_table = 'mbusket'
		verbose_name_plural = 'MBuskets'
		verbose_name = 'MBusket'
		ordering  = ['-created_at']


class MBusketForm(forms.ModelForm):
	author = forms.JSONField()
	organization = forms.JSONField()
	providers = forms.JSONField()
	products = forms.JSONField()

	class Meta:
		model = MBusket
		fields = ['count', 'price', 'products', 'author', 'organization', 'providers']




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
	_id = ObjectId()
	courier = forms.JSONField()
	organization = forms.JSONField()

	class Meta:
		model = MCourier
		fields = ['_id', 'courier', 'organization']




class MOrder(MarketMainMixin):
	_id = models.ObjectIdField()
	count = models.IntegerField(verbose_name = 'Count')
	count_success = models.IntegerField(default = 0, verbose_name = 'Count Success')
	price = models.FloatField(verbose_name = 'Price')

	address = models.CharField(max_length = 150, verbose_name = 'Address')
	description = models.CharField(max_length = 5000, verbose_name = 'Description')
	comment = models.CharField(max_length = 1000, verbose_name = 'Comment')

	products = models.JSONField(verbose_name = 'Products')
	courier = models.JSONField(verbose_name = 'Courier')
	providers = models.JSONField(verbose_name = 'Providers')
	author = models.JSONField(verbose_name = 'Author')
	organization = models.JSONField(verbose_name = 'Organization')

	done = models.BooleanField(default = False)

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
	products = forms.JSONField()
	author = forms.JSONField()

	class Meta:
		model = MOrder
		fields = ['_id','price', 'address', 'count', 'count_success', 'description', 'comment', 'author', 'products', 'courier', 'organization', 'providers', 'done']