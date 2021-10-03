from django.db import models

from Organizations.models import Organization, MainMixin



class DeviceType(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_device_type', verbose_name = 'Organization')
	description = models.TextField(verbose_name = 'Description')


	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id}'


	class Meta:
		db_table = 'DeviceType'
		verbose_name_plural = "DeviceTypes"
		verbose_name = "DeviceType"
		ordering = ['-updated_at']



class DeviceMaker(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_device_maker', verbose_name = 'Organization')


	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id}'


	class Meta:
		db_table = 'DeviceMaker'
		verbose_name_plural = "DeviceMakers"
		verbose_name = "DeviceMaker"
		ordering = ['-updated_at']



class DeviceModel(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_device_model', verbose_name = 'Organization')


	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id}'


	class Meta:
		db_table = 'DeviceModel'
		verbose_name_plural = "DeviceModels"
		verbose_name = "DeviceModel"
		ordering = ['-updated_at']



class DeviceKit(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_device_kit', verbose_name = 'Organization')
	device_type = models.ForeignKey(DeviceType, on_delete = models.CASCADE, related_name = 'device_type_device_kit', verbose_name = 'DeviceType')


	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id} | device type: {self.device_type}'


	class Meta:
		db_table = 'DeviceKit'
		verbose_name_plural = "DeviceKits"
		verbose_name = "DeviceKit"
		ordering = ['-updated_at']



class DeviceAppearance(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_device_appearance', verbose_name = 'Organization')


	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id}'


	class Meta:
		db_table = 'DeviceAppearance'
		verbose_name_plural = "DeviceAppearances"
		verbose_name = "DeviceAppearance"
		ordering = ['-updated_at']



class DeviceDefect(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_device_defect', verbose_name = 'Organization')


	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id}'


	class Meta:
		db_table = 'DeviceDefect'
		verbose_name_plural = "DeviceDefects"
		verbose_name = "DeviceDefect"
		ordering = ['-updated_at']



class ServicePrice(MainMixin):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_service_price', verbose_name = 'Organization')
	price = models.FloatField()


	def __str__(self):
		return f'id: {self.id} | name: {self.name} | organization: {self.organization.id}'


	class Meta:
		db_table = 'ServicePrice'
		verbose_name_plural = "ServicePrices"
		verbose_name = "ServicePrice"
		ordering = ['-updated_at']