from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from Organizations.models import Organization, MainMixin, Service
from Clients.models import ClientCard
from Handbook.models import ServicePrice
from Orders.models import Order



class ProductCategory(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')

	def __str__(self):
		return str(self.name)

	class Meta:
		db_table = 'Category'.lower()
		verbose_name_plural = 'Categories'
		verbose_name = 'Category'
		ordering = ['-updated_at']



class Product(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	code = models.CharField(max_length = 150, null = True, verbose_name = 'Code')
	barcode = models.CharField(max_length = 150, null = True, verbose_name = 'Barcode')
	purchase_price = models.DecimalField(max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Purchase price')
	sale_price = models.DecimalField(max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Sale price')
	count = models.IntegerField(verbose_name = 'Quantity')
	supplier = models.CharField(max_length = 150, verbose_name = 'Supplier')
	irreducible_balance = models.DecimalField(max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Irreducible balance')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_product', verbose_name = 'Organization')
	category = models.ForeignKey(ProductCategory, on_delete = models.SET_NULL, related_name = 'category_product', null = True, verbose_name = 'Category')
	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_product', verbose_name = 'Service')

	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id} category: {self.category}'


	class Meta:
		db_table = 'Product'.lower()
		verbose_name_plural = "Products"
		verbose_name = "Product"
		ordering = ['-updated_at']



class Cashbox(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	cash = models.DecimalField(max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Cash')
	account_money = models.DecimalField(max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Account money')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_cashbox', verbose_name = 'Organization')
	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_cashbox', verbose_name = 'Service')

	def __str__(self):
		return f'id: {self.id} | organization: {self.organization.id} | cash: {self.cash} bank: {self.account_money} | service: {self.service.id}'

	@property
	def calculate_min_money(self):
		return min([self.cash, self.account_money])

	class Meta:
		db_table = 'Cashbox'.lower()
		verbose_name_plural = 'Cashboxes'
		verbose_name = 'Cashbox'
		ordering = ['-updated_at']



class PurchaseRequest(MainMixin):
	price = models.DecimalField(max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Price')
	count = models.IntegerField(verbose_name = 'Quantity')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_purchase_request', verbose_name = 'Organization')
	cashbox = models.ForeignKey(Cashbox, on_delete = models.CASCADE, related_name = 'cashbox_purchase_request', verbose_name = 'Cashbox')
	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_purchase_request', verbose_name = 'Service')
	product = models.ForeignKey(Product, on_delete = models.PROTECT, related_name = 'product_purchase_request', verbose_name = 'Product')

	is_deferred = models.BooleanField(default = False, verbose_name = 'Deferred')
	is_cash = models.BooleanField(verbose_name = 'Is cash')

	def __str__(self):
		return f'id: {self.id} | organization: {self.organization.id} | cashbox: {self.cashbox.id} price: {self.price}'


	@property
	def calculate_quantity(self):
		return (product.count - count) > 0


	class Meta:
		db_table = 'PurchaseRequest'.lower()
		verbose_name_plural = 'PurchaseRequests'
		verbose_name = 'PurchaseRequest'
		ordering = ['-updated_at']



class PurchaseAccept(MainMixin):
	purchase_request = models.OneToOneField(PurchaseRequest, on_delete = models.CASCADE, related_name = 'purchase_purchase_accept', verbose_name = 'PurchaseRequest')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_purchase_accept', verbose_name = 'Organization')

	is_cash = models.BooleanField(default = False)
	accept = models.BooleanField(default = False)

	def __str__(self):
		return f'id: {self.id} | purchase_request: {self.purchase_request.id} | organization: {self.organization.id} | accept: {self.accept}'


	class Meta:
		db_table = 'PurchaseAccept'.lower()
		verbose_name_plural = 'PurchaseAccepts'
		verbose_name = 'PurchaseAccept'
		ordering = ['-updated_at']



class SaleProduct(MainMixin):
	cash = models.DecimalField(max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Cash')
	card = models.DecimalField(max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Card')
	bank_transfer = models.DecimalField(max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Bank transfer')
	discount = models.DecimalField(max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Discount')

	client = models.ForeignKey(ClientCard, on_delete = models.SET_NULL, related_name = 'client_card_sale_product', null = True, verbose_name = 'ClientCard')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_sale_product', verbose_name = 'Organization')
	cashbox = models.ForeignKey(Cashbox, on_delete = models.CASCADE, related_name = 'cashbox_sale_product', verbose_name = 'Cashbox')
	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_sale_product', verbose_name = 'Service')
	product = models.ForeignKey(Product, on_delete = models.PROTECT, related_name = 'product_sale_product', verbose_name = 'Product')

	def __str__(self):
		return f'id: {self.id} | organization: {self.organization.id} | cashbox: {self.cashbox.id} cash: {self.cash} card: {self.card} | bank_transfer: {self.bank_transfer} | discount: {self.discount} | product: {self.product}'


	class Meta:
		db_table = 'SaleProduct'.lower()
		verbose_name_plural = 'SaleProducts'
		verbose_name = 'SaleProduct'
		ordering = ['-updated_at']



class SaleOrder(MainMixin):
	cash = models.DecimalField(default = 0, max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Cash')
	card = models.DecimalField(default = 0, max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Card')
	bank_transfer = models.DecimalField(default = 0, max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Bank transfer')
	discount = models.DecimalField(default = 0, max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Discount')

	client = models.ForeignKey(ClientCard, on_delete = models.SET_NULL, related_name = 'client_card_sale_order', null = True, verbose_name = 'ClientCard')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_sale_order', verbose_name = 'Organization')
	cashbox = models.ForeignKey(Cashbox, on_delete = models.CASCADE, related_name = 'cashbox_sale_order', verbose_name = 'Cashbox')
	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_sale_order', verbose_name = 'Service')
	product_order = models.ForeignKey('ProductOrder', on_delete = models.PROTECT, related_name = 'product_sale_order', verbose_name = 'ProductOrder')

	def __str__(self):
		return f'id: {self.id} | organization: {self.organization.id} | cashbox: {self.cashbox.id} cash: {self.price} card: {self.card} | bank_transfer: {self.bank_transfer} | discount: {self.discount}'


	class Meta:
		db_table = 'SaleOrder'.lower()
		verbose_name_plural = 'SaleOrders'
		verbose_name = 'SaleOrder'
		ordering = ['-updated_at']



class WorkDone(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	price = models.DecimalField(default = 0, max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Price')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_work_done', verbose_name = 'Organization')
	service_price = models.ForeignKey(ServicePrice, on_delete = models.SET_NULL, related_name = 'service_price_work_done', null = True, verbose_name = 'ServicePrice')
	user = models.ForeignKey(get_user_model(), on_delete = models.PROTECT, related_name = 'user_work_done', verbose_name = 'User')
	order = models.ForeignKey(Order, on_delete = models.PROTECT, related_name = 'order_work_done', verbose_name = 'Order')
	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_work_done', verbose_name = 'Service')

	def __str__(self):
		return f'id: {self.id} | organization: {self.organizatin.id} | user: {self.user.id} | order: {self.order.id} | price: {self.price}'


	class Meta:
		db_table = 'WorkDone'.lower()
		verbose_name_plural = 'WorkDones'
		verbose_name = 'WorkDone'
		ordering = ['-updated_at']



class ProductOrder(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	price = models.DecimalField(max_digits = 100, decimal_places = 2, validators=[MinValueValidator(0.0)], verbose_name = 'Price')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_product_order', verbose_name = 'Organization')
	products = models.ManyToManyField(Product, related_name = 'product_product_order', verbose_name = 'Product')
	order = models.OneToOneField(Order, on_delete = models.PROTECT, related_name = 'order_product_order', verbose_name = 'Order')
	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_product_order', verbose_name = 'Service')

	def __str__(self):
		return f'id: {self.id} | price: {self.price} | organization: {self.organization.id}'


	def calculate_price(self, products_list):
		cost = 0
		for item in products_list:
			cost += item.sale_price

		self.price = cost
		return self.price


	class Meta:
		db_table = 'ProductOrder'.lower()
		verbose_name_plural = 'ProductOrders'
		verbose_name = 'ProductOrder'
		ordering = ['-updated_at']



class Transaction(MainMixin):
	cashbox = models.ForeignKey(Cashbox, on_delete = models.PROTECT, related_name = 'cashbox_transaction', verbose_name = 'Cashbox')
	purchase = models.ForeignKey(PurchaseRequest, on_delete = models.SET_NULL, related_name = 'purchase_transaction', null = True, verbose_name = 'Purchase')
	sale_product = models.ForeignKey(SaleProduct, on_delete = models.SET_NULL, related_name = 'cashbox_sale', null = True, verbose_name = 'SaleProduct')
	sale_order = models.ForeignKey(SaleOrder, on_delete = models.SET_NULL, related_name = 'cashbox_sale', null = True, verbose_name = 'SaleOrder')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_transaction', verbose_name = 'Organization')

	def __str__(self):
		sale = ''
		purchase = ''

		if self.sale_product:
			sale = f'| sale_product: {self.sale_product.id}'

		elif self.sale_order:
			sale =f'| sale_order: {self.sale_order.id}'

		elif self.purchase:
			purchase = f'| purchase: {self.purchase.id}'

		return f'id: {self.id} | organization: {self.organization.id} {purchase} {sale}'


	class Meta:
		db_table = 'Transaction'.lower()
		verbose_name_plural = 'Transactions'
		verbose_name = 'Transaction'
		ordering = ['-updated_at']