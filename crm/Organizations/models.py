from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator

from phonenumber_field.modelfields import PhoneNumberField



class Organization(models.Model):
	name = models.CharField(max_length = 150, unique = True, verbose_name = 'Name')
	description = models.CharField(max_length = 500, blank = True, verbose_name = 'Description')
	address = models.CharField(max_length = 200, verbose_name = 'Address')

	creator = models.ForeignKey(get_user_model(), on_delete = models.PROTECT, related_name = 'my_organizations', verbose_name = 'creator')

	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')

	def __str__(self):
		return f'id: {self.id} | creator: {self.creator}'


	class Meta:
		db_table = 'Organization'
		unique_together = (("name"),("address"))
		verbose_name_plural = "Organizations"
		verbose_name = "Organization"
		ordering = ['-updated_at']



class MainMixin(models.Model):
	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')


	class Meta:
		abstract = True



class Organization_number(MainMixin):
	number = PhoneNumberField(unique = True)
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_numbers', verbose_name = 'Organization')

	def __str__(self):
		return f'id: {self.id} | number: {self.number} | org: {self.organization}'

	class Meta:
		unique_together = (('number'), ('organization'))
		db_table = 'Organization_number'
		verbose_name_plural = "Organizations' numbers"
		verbose_name = "Organization's number"
		ordering = ['-updated_at']



class Organization_link(MainMixin):
	name = models.CharField(max_length = 50, verbose_name = 'Name')
	link = models.CharField(validators = [RegexValidator(regex = r"^(https?:\/\/)?([\w-]{1,32}\.[\w-]{1,32})[^\s@]*$")], max_length = 200, verbose_name = 'Link')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_links', verbose_name = 'Organization')

	def __str__(self):
		return f'id: {self.id} | org: {self.org}'

	class Meta:
		unique_together = (('link'), ('organization'))
		db_table = 'Organization_link'
		verbose_name_plural = "Organizations' link"
		verbose_name = "Organization's link"
		ordering = ['-updated_at']



class Service(MainMixin):
	name = models.CharField(max_length = 150, unique = True, verbose_name = 'Name')
	number = PhoneNumberField(unique = True, verbose_name = 'Number')
	address = models.CharField(max_length = 200, verbose_name = 'Address')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_services', verbose_name = 'Organization')

	def __str__(self):
		return f'id: {self.id} | name: {self.name} | org: {self.organization}'

	class Meta:
		unique_together = (('name'), ('organization'))
		db_table = 'Service'
		verbose_name_plural = "Services"
		verbose_name = "Service"
		ordering = ['-updated_at']



class Permission(models.Model):
	official_perm_name = models.CharField(max_length = 60, verbose_name = 'Offical_name')
	name = models.CharField(max_length = 150, verbose_name = 'Technical_name')
	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')

	def __str__(self):
		return f'id: {self.id} | name: {self.name}'

	class Meta:
		db_table = 'Permission'
		verbose_name_plural = 'Permissions'
		verbose_name = 'Permission'
		ordering = ['-created_at']



class Role(MainMixin):
	name = models.CharField(max_length = 100, verbose_name = 'Name')
	permissions = models.ManyToManyField(Permission, related_name = 'permission_roles', verbose_name = 'Permissions')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_roles', verbose_name = 'Organization')


	def __str__(self):
		return f'id: {self.id} | name: {self.name} | org: {self.organization}'

	class Meta:
		db_table = 'Role'
		verbose_name_plural = 'Roles'
		verbose_name = 'Role'
		ordering = ['-updated_at']



class Organization_member(MainMixin):
	user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name = 'user_member', verbose_name = 'User')
	role = models.ForeignKey(Role, on_delete = models.PROTECT, related_name = 'role_member', verbose_name = 'Role')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_members', verbose_name = 'Organization')

	def __str__(self):
		return f'id: {self.id} | user: {self.user} | role: {self.role}'

	class Meta:
		unique_together = (('user'), ('organization'))
		db_table = 'Organization_member'
		verbose_name_plural = 'Organization_members'
		verbose_name = 'Organization_member'
		ordering = ['-updated_at']



class Order(MainMixin):
	order_code = models.BigIntegerField(verbose_name = 'Order_code')
	description = models.CharField(max_length = 100, verbose_name = 'Description')
	client = models.ForeignKey(get_user_model(), on_delete = models.PROTECT, related_name = 'client_orders', verbose_name = 'Client')
	executor = models.ForeignKey(get_user_model(), on_delete = models.PROTECT, related_name = 'user_executor', verbose_name = 'Executor')
	creator = models.ForeignKey(get_user_model(), on_delete = models.PROTECT, related_name = 'user_creator', verbose_name = 'Creator')

	service = models.ForeignKey(Service, on_delete = models.PROTECT, related_name = 'service_orders', verbose_name = 'Service')

	done = models.BooleanField(default = False)


	class Meta:
		db_table = 'Order'
		verbose_name_plural = "Orders"
		verbose_name = "Order"
		ordering = ['-updated_at']