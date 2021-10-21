from django.db import models
from django.contrib.auth import get_user_model

from Organizations.models import MainMixin, Service, Organization
from Clients.models import Client



class OrderStatus(MainMixin):
	TYPES = (
		(0, 'New'),
		(1, 'Pending'),
		(2, 'In progress'),
		(3, 'Completed'),
		(4, 'Issued'),
	)
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	color = models.CharField(max_length = 150, null = True, verbose_name = 'Color')
	icon = models.CharField(max_length = 300, null = True, verbose_name = 'Image')
	description = models.TextField(null = True, verbose_name = 'Description')
	type = models.CharField(max_length = 150, null = True, choices = TYPES, verbose_name = 'Type')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_order_status', verbose_name = 'Organization')

	is_default = models.BooleanField(default = True)
	is_payment_required = models.BooleanField(default = False)
	is_comment_required = models.BooleanField(default = False)

	def __str__(self):
		return f'id: {self.id} | type: {self.type} | organization: {self.organization.id} | is_default: {self.is_default} | is_payment_required: {self.is_payment_required} | is_comment_required: {self.is_comment_required}'


	class Meta:
		db_table = 'OrderStatus'.lower()
		verbose_name_plural = 'OrderStatuses'
		verbose_name = 'OrderStatus'
		ordering = ['-updated_at']



class Order(MainMixin):
	order_code = models.CharField(max_length = 300, unique = True, verbose_name = 'Order_code')
	description = models.CharField(max_length = 500, verbose_name = 'Description')
	client = models.ForeignKey(Client, on_delete = models.PROTECT, related_name = 'client_orders', verbose_name = 'Client')
	executor = models.ForeignKey(get_user_model(), on_delete = models.PROTECT, related_name = 'user_executor', verbose_name = 'Executor')
	creator = models.ForeignKey(get_user_model(), on_delete = models.PROTECT, related_name = 'user_creator', verbose_name = 'Creator')

	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_orders', verbose_name = 'Service')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name='organization_orders', verbose_name = 'Organization')
	order_status = models.ForeignKey(OrderStatus, null = True, on_delete = models.PROTECT, related_name = 'order_status_order', verbose_name = 'OrderStatus')

	device_type = models.CharField(max_length = 300, null = True, verbose_name = 'DeviceType')
	device_maker = models.CharField(max_length = 300, null = True, verbose_name = 'DeviceMaker')
	device_model = models.CharField(max_length = 300, null = True, verbose_name = 'DeviceModel')
	device_kit = models.TextField(null = True, verbose_name = 'DeviceKit')
	device_appearance = models.TextField(null = True,verbose_name = 'DeviceAppearance')
	device_defect = models.TextField(null = True, verbose_name = 'DeviceDefect')

	done = models.BooleanField(default = False)
	is_rush = models.BooleanField(default = False)


	@property
	def calculate_order_code(self):
		last = self.__class__.objects.filter(service = self.service).filter(organization = self.organization)

		if last.exists():
			core_split = last.last().order_code.split('-')
			self.order_code = '-'.join([core_split[0],str(int(core_split[1])+1)])

		else:
			self.order_code = self.service.prefix+'-'+'1'

		return self.order_code


	def __str__(self):
		return f'id: {self.id} | order code: {self.order_code} |creator: {self.creator} | client: {self.client} | executor: {self.executor}'

	class Meta:
		db_table = 'Order'.lower()
		verbose_name_plural = "Orders"
		verbose_name = "Order"
		ordering = ['-updated_at']
