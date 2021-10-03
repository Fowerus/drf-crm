from django.db import models

from Organizations.models import Organization, MainMixin, Service
from Client.models import ClientCard


class ProductCategory(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')

	def __str__(self):
		return str(self.name)

	class Meta:
		db_table = 'Category'
		verbose_name_plural = 'Categories'
		verbose_name = 'Category'
		ordering = ['-updated_at']



class Product(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	code = models.CharField(max_length = 150, null = True, verbose_name = 'Code')
	barcode = models.CharField(max_length = 150, null = True, verbose_name = 'Barcode')
	purchase_price = models.FloatField(verbose_name = 'Purchase price')
	sale_price = models.FloatField(verbose_name = 'Sale price')
	count = models.IntegerField(verbose_name = 'Count')
	supplier = models.CharField(max_length = 150, verbose_name = 'Supplier')
	irreducible_balance = models.FloatField(null = True)

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_product', verbose_name = 'Organization')
	category = models.ForeignKey(ProductCategory, on_delete = models.SET_NULL, related_name = 'category_product', null = True, verbose_name = 'Category')
	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_product', verbose_name = 'Service')
	purchase = models.ForeignKey('Purchase', on_delete = models.PROTECT, related_name = 'purchase_product', verbose_name = 'Purchase')
	sale = models.ForeignKey('Sale', on_delete = models.SET_NULL, related_name = 'sale_product', null = True, verbose_name = 'Sale')

	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id} category: {self.category.name} purchase: {self.purchase.id}'


	class Meta:
		db_table = 'Product'
		verbose_name_plural = "Products"
		verbose_name = "Product"
		ordering = ['-updated_at']



class CashBox(MainMixin):
	name = models.CharField(verbose_name = 'Name')
	cash = models.FloatField(verbose_name = 'Cash')
	account_money = models.FloatField(verbose_name = 'Account money')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_cashbox', verbose_name = 'Organization')
	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_cashbox', verbose_name = 'Service')

	def __str__(self):
		return f'id: {self.id} | organization: {self.organization.id} | cash: {self.cash} bank: {self.account_money} | service: {self.service.id}'


	class Meta:
		db_table = 'Cashbox'
		verbose_name_plural = 'Cashboxes'
		verbose_name = 'Cashbox'
		ordering = ['-updated_at']



class Purchase(MainMixin):
	price = models.FloatField(verbose_name = 'Price')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_purchase', verbose_name = 'Organization')
	cashbox = models.ForeignKey(Cashbox, on_delete = models.CASCADE, related_name = 'cashbox_purchase', verbose_name = 'Purchase')
	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_purchase', verbose_name = 'Service')

	is_deferred = models.BooleanField(default = False, verbose_name = 'Deferred')

	def __str__(self):
		return f'id: {self.id} | organization: {self.organization.id} | cashbox: {self.cashbox.id} price: {self.price}'


	class Meta:
		db_table = 'Purchase'
		verbose_name_plural = 'Purchases'
		verbose_name = 'Purchase'
		ordering = ['-updated_at']



class Sale(MainMixin):
	cash = models.FloatField(default = 0, verbose_name = 'Cash')
	card = models.FloatField(default = 0, verbose_name = 'Card')
	bank_transfer = models.FloatField(default = 0, verbose_name = 'Bank transfer')
	discount = models.ForeignKey(default = 0, verbose_name = 'Discount')

	client = models.ForeignKey(ClientCard, on_delete = models.SET_NULL, related_name = 'client_card_sale', null = True, verbose_name = 'ClientCard')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_purchase', verbose_name = 'Organization')
	cashbox = models.ForeignKey(Cashbox, on_delete = models.CASCADE, related_name = 'cashbox_purchase', verbose_name = 'Purchase')
	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_purchase', verbose_name = 'Service')

	def __str__(self):
		return f'id: {self.id} | organization: {self.organization.id} | cashbox: {self.cashbox.id} cash: {self.price} card: {self.card} | discount: {self.discount}'


	class Meta:
		db_table = 'Sale'
		verbose_name_plural = 'Sales'
		verbose_name = 'Sale'
		ordering = ['-updated_at']



class WorkDone(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	price = models.FloatField(verbose_name = 'Price')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_work_done', verbose_name = 'Organization')
	service_price = models.ForeignKey(ServicePrice, on_delete = models.SET_NULL, related_name = 'service_price_workdone', null = True, verbose_name = 'ServicePrice')
	user = models.ForeignKey(get_user_model(), on_delete = models.PROTECT, related_name = 'user_work_done', verbose_name = 'User')
	order = models.ForeignKey(Order, on_delete = models.PROTECT, related_name = 'order_work_done', verbose_name = 'Order')
	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_work_done', verbose_name = 'Service')

	def __str__(self):
		return f'id: {self.id} | organization: {self.organizatin.id} | user: {self.user.id} | order: {self.order.id} | price: {self.price}'


	class Meta:
		db_table = 'WorkDone'
		verbose_name_plural = 'WorkDones'
		verbose_name = 'WorkDone'
		ordering = ['-updated_at']




class ProductOrder(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	price = models.FloatField(verbose_name = 'Price')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_product_order', verbose_name = 'Organization')
	product = models.ForeignKey(Product, on_delete = models.CASCADE)