from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.core import validators

from phonenumber_field.modelfields import PhoneNumberField



class Organization(models.Model):
	name = models.CharField(max_length = 150, unique = True, verbose_name = 'Name')
	description = models.CharField(max_length = 500, verbose_name = 'Description')
	address = models.CharField(max_length = 200, verbose_name = 'Address')

	creator = models.ForeignKey(get_user_model(), on_delete = models.SET_NULL, null = True, related_name = 'my_organizations', verbose_name = 'Creator')
	numbers = models.JSONField(null = True, blank = True)
	links = models.JSONField(null = True, blank = True)

	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')

	def __str__(self):
		return f'id: {self.id} | creator: {self.creator}'


	class Meta:
		db_table = 'Organization'.lower()
		unique_together = ("name","address")
		verbose_name_plural = "Organizations"
		verbose_name = "Organization"
		ordering = ['-updated_at']



class MainMixin(models.Model):
	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')

	data = models.JSONField(null = True, blank = True)


	class Meta:
		abstract = True



class Service(MainMixin):
	prefix = models.CharField(max_length = 10, unique = True, verbose_name = 'Prefix')
	name = models.CharField(max_length = 150, unique = True, verbose_name = 'Name')
	phone = PhoneNumberField(unique = True, verbose_name = 'Phone')
	address = models.CharField(max_length = 200, verbose_name = 'Address')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_services', verbose_name = 'Organization')

	def __str__(self):
		return f'id: {self.id} | name: {self.name} | org: {self.organization}'

	class Meta:
		unique_together = ('name', 'organization')
		db_table = 'Service'.lower()
		verbose_name_plural = "Services"
		verbose_name = "Service"
		ordering = ['-updated_at']



class CustomPermission(models.Model):
	name = models.CharField(max_length = 60, unique = True, verbose_name = 'Official_name')
	codename = models.CharField(max_length = 150, unique = True, verbose_name = 'Codename')
	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')

	def __str__(self):
		return f'id: {self.id} | name: {self.name}'

	class Meta:
		unique_together = ('name', 'codename')
		db_table = 'CustomPermission'.lower()
		verbose_name_plural = 'CustomPermissions'
		verbose_name = 'CustomPermission'
		ordering = ['-created_at']



class Role(MainMixin):
	name = models.CharField(max_length = 100, verbose_name = 'Name')
	permissions = models.ManyToManyField(CustomPermission, related_name = 'permission_roles', verbose_name = 'Permissions')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_roles', verbose_name = 'Organization')


	def __str__(self):
		return f'id: {self.id} | name: {self.name} | org: {self.organization}'

	class Meta:
		unique_together = ('name', 'organization')
		db_table = 'Role'.lower()
		verbose_name_plural = 'Roles'
		verbose_name = 'Role'
		ordering = ['-updated_at']



class Organization_member(MainMixin):
	user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name = 'user_member', verbose_name = 'User')
	role = models.ForeignKey(Role, on_delete = models.SET_NULL, null = True, related_name = 'role_member', verbose_name = 'Role')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_members', verbose_name = 'Organization')

	surname = models.CharField(max_length = 150, null = True, blank = True, verbose_name = 'Surname')
	name = models.CharField(max_length = 150, null = True, blank = True, verbose_name = 'Name')
	second_name = models.CharField(max_length = 150, null = True, blank = True, verbose_name = 'Second name')

	email = models.CharField(validators = [validators.EmailValidator], max_length = 100, unique = True, blank = True, null = True, verbose_name = 'Email')
	phone = PhoneNumberField(unique = True, blank = True, null = True, verbose_name = 'Phone')
	address = models.CharField(max_length = 200, null = True, blank = True, verbose_name = 'Address')

	image = models.CharField(max_length = 300, null = True, blank = True, verbose_name = 'Image')

	pass_series = models.CharField(max_length = 4, null = True, blank = True, verbose_name = 'Passport series')
	pass_number = models.CharField(max_length = 6, null = True, blank = True, verbose_name = 'Passport number')

	def __str__(self):
		return f'id: {self.id} | user: {self.user} | role: {self.role}'

	class Meta:
		unique_together = ('user', 'organization')
		db_table = 'Organization_member'.lower()
		verbose_name_plural = 'Organizations members'
		verbose_name = 'Organization member'
		ordering = ['-updated_at']
		