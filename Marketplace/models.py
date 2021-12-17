from django.contrib.auth import get_user_model
from django import forms
from djongo import models

from Organizations.forms import MOrganizationForm, MOrganization_memberForm
from Users.forms import MUserForm



class MarketMainMixin(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)


	class Meta:
		abstract = True




class MProduct(MarketMainMixin):
	_id = models.ObjectIdField()
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	count = models.IntegerField(verbose_name = 'Count')
	price = models.DecimalField(max_digits = 100, decimal_places = 2, verbose_name = 'Price')
	price_opt = models.DecimalField(max_digits = 100, decimal_places = 2, verbose_name = 'Wholesale price')
	url_product = models.CharField(max_length = 300, verbose_name = 'Product url')
	url_photo = models.CharField(max_length = 300, verbose_name = 'Photo url')
	address = models.CharField(max_length = 300, verbose_name = 'Address')
	provider_site = models.CharField(max_length = 300, verbose_name = 'MProvider')
	
	organization = models.EmbeddedField(model_container = MOrganizationForm._meta.model, model_form_class = MOrganizationForm, verbose_name = 'Organization')

	objects = models.DjongoManager()

	def __str__(self):
		return f'_id: {self._id} | name: {self.name} | price: {self.price}'


	class Meta:
		db_table = 'mproduct'
		verbose_name_plural = 'Marketplace products'
		verbose_name = 'Marketplace product'
		ordering  = ['-created_at']


class MProductForm(forms.ModelForm):
	class Meta:
		model = MProduct
		fields = ['_id', 'name', 'count', 'price',
		'url_product', 'url_photo', 'address', 'provider_site', 'organization']




class MBusket(MarketMainMixin):
	_id = models.ObjectIdField()
	count = models.IntegerField(verbose_name = 'Count')
	price = models.DecimalField(max_digits = 100, decimal_places = 2, verbose_name = 'Price')

	products = models.ArrayField(model_container = MProductForm._meta.model, model_form_class = MProductForm, verbose_name = 'Products')
	author = models.EmbeddedField(model_container = MUserForm._meta.model, model_form_class = MUserForm, verbose_name = 'Author')
	organization = models.EmbeddedField(model_container = MOrganizationForm._meta.model, model_form_class = MOrganizationForm, verbose_name = 'Organization')

	objects = models.DjongoManager()

	def __str__(self):
		return f'_id: {self._id} | products: {len(self.products)} items'


	class Meta:
		db_table = 'mbusket'
		verbose_name_plural = 'Marketplace buskets'
		verbose_name = 'Marketplace busket'
		ordering  = ['-created_at']




class MCourier(MarketMainMixin):
	_id = models.ObjectIdField()
	
	user = models.EmbeddedField(model_form_class = MUserForm, verbose_name = 'User')
	organization = models.EmbeddedField(model_container = MOrganizationForm._meta.model, model_form_class = MOrganizationForm, verbose_name = 'Organization')

	objects = models.DjongoManager()

	def __str__(self):
		return f'_id: {self._id}'


	class Meta:
		db_table = 'mcourier'
		verbose_name_plural = 'Marketplace couriers'
		verbose_name = 'Marketplace courier'
		ordering = ['-created_at']


class MCourierForm(MarketMainMixin):

	class Meta:
		model = MCourier
		fields = ['_id', 'user', 'organization']



class MProductOrderForm(forms.ModelForm):
	done = forms.BooleanField(default = False)

	class Meta:
		model = MProduct
		fields = ['_id', 'name', 'count', 'price',
		'url_product', 'url_photo', 'address', 'done', 'provider_site', 'organization']


class MOrder(MarketMainMixin):
	_id = models.ObjectIdField()
	price = models.DecimalField(max_digits = 100, decimal_places = 2, verbose_name = 'Price')
	address = models.CharField(max_length = 150, verbose_name = 'Address')
	description = models.CharField(max_length = 5000, verbose_name = 'Description')
	comment = models.CharField(max_length = 1000, verbose_name = 'Comment')

	author = models.EmbeddedField(model_container = MUserForm._meta.model, model_form_class = MUserForm, verbose_name = 'Author')
	products = models.ArrayField(model_container = MProductOrderForm._meta.model, model_form_class = MProductOrderForm, verbose_name = 'Products')
	courier = models.EmbeddedField(model_container = MCourier._meta.model, model_form_class = MCourierForm, verbose_name = 'Courier')
	organization = models.EmbeddedField(model_container = MOrganizationForm._meta.model, model_form_class = MOrganizationForm, verbose_name = 'Organization')

	objects = models.DjongoManager()

	def __str__(self):
		return f'_id: {self._id} | products: {len(self.products)} items'


	class Meta:
		db_table = 'morder'
		verbose_name_plural = 'Marketplace orders'
		verbose_name = 'Marketplace order'
		ordering = ['-created_at']