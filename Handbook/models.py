from django.db import models

from Organizations.models import Organization, Service
from Orders.models import Order
from core.utils.helper import MainMixin



class DeviceType(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	description = models.TextField(verbose_name = 'Description')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_device_type', verbose_name = 'Organization')
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, null = True, blank = True, 
                                related_name='service_devicetype', verbose_name='Service')


	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id}'


	class Meta:
		db_table = 'DeviceType'.lower()
		verbose_name_plural = "DeviceTypes"
		verbose_name = "DeviceType"
		ordering = ['-updated_at']



class DeviceMaker(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_device_maker', verbose_name = 'Organization')
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, null = True, blank = True, 
                                related_name='service_devicemaker', verbose_name='Service')

	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id}'


	class Meta:
		db_table = 'DeviceMaker'.lower()
		verbose_name_plural = "DeviceMakers"
		verbose_name = "DeviceMaker"
		ordering = ['-updated_at']




class DeviceModel(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_device_model', verbose_name = 'Organization')
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, null = True, blank = True, 
                                related_name='service_devicemodel', verbose_name='Service')

	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id}'


	class Meta:
		db_table = 'DeviceModel'.lower()
		verbose_name_plural = "DeviceModels"
		verbose_name = "DeviceModel"
		ordering = ['-updated_at']



class DeviceKit(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	devicetype = models.ForeignKey(DeviceType, on_delete = models.CASCADE, related_name = 'device_type_device_kit', verbose_name = 'DeviceType')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_device_kit', verbose_name = 'Organization')
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, null = True, blank = True, 
                                related_name='service_devicekit', verbose_name='Service')

	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id} | device type: {self.devicetype}'


	class Meta:
		db_table = 'DeviceKit'.lower()
		verbose_name_plural = "DeviceKits"
		verbose_name = "DeviceKit"
		ordering = ['-updated_at']



class DeviceAppearance(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_device_appearance', verbose_name = 'Organization')
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, null = True, blank = True, 
                                related_name='service_deviceappearance', verbose_name='Service')

	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id}'


	class Meta:
		db_table = 'DeviceAppearance'.lower()
		verbose_name_plural = "DeviceAppearances"
		verbose_name = "DeviceAppearance"
		ordering = ['-updated_at']



class DeviceDefect(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_device_defect', verbose_name = 'Organization')
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, null = True, blank = True, 
                                related_name='service_devicedefect', verbose_name='Service')

	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id}'


	class Meta:
		db_table = 'DeviceDefect'.lower()
		verbose_name_plural = "DeviceDefects"
		verbose_name = "DeviceDefect"
		ordering = ['-updated_at']



class ServicePrice(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	price = models.FloatField()

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_service_price', verbose_name = 'Organization')
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, null = True, blank = True, 
                                related_name='service_deviceprice', verbose_name='Service')

	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id}'


	class Meta:
		db_table = 'ServicePrice'.lower()
		verbose_name_plural = "ServicePrices"
		verbose_name = "ServicePrice"
		ordering = ['-updated_at']



class ActionHistory(MainMixin):
	model_name = (
		('0', 'ProductOrder'),
		('1', 'WorkDone'),
		('2', 'SaleOrder'),
		('3', 'Order'),
		('4', 'OrderHistory'),
	)

	method = models.CharField(max_length = 150, null = True, verbose_name = 'Method')
	process = models.CharField(max_length = 150, verbose_name = 'Process')
	model = models.CharField(max_length = 150, choices = model_name, verbose_name = 'Model name')

	def __str__(self):
		return f'id: {self.id} | process: {self.process} | model: {self.model_name[int(self.model)][1]}'


	class Meta:
		unique_together = ('method','model')
		db_table = 'ActionHistory'.lower()
		verbose_name_plural = "ActionHistories"
		verbose_name = "ActionHistory"
		ordering = ['-updated_at']



class OrderHistory(MainMixin):
	order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = 'order_order_history', verbose_name = 'Order')
	comment = models.TextField(null = True, verbose_name = 'Comment')
	body = models.JSONField(null = True),
	action_history = models.ForeignKey(ActionHistory, on_delete = models.PROTECT, related_name = 'action_history_order_history', verbose_name = 'Action history')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_order_history', verbose_name = 'Organization')
	service = models.ForeignKey(Service, on_delete=models.SET_NULL, null = True, blank = True, 
                                related_name='service_devicehistory', verbose_name='Service')

	def __str__(self):
		return f'id: {self.id} | organization: {self.organization} | action_history: {self.action_history.process}'


	class Meta:
		db_table = 'OrderHistory'.lower()
		verbose_name_plural = 'OrderHistories'
		verbose_name = 'OrderHistory'
		ordering = ['-updated_at']