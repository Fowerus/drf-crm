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


	class Meta:
		db_table = 'Organization'
		unique_together = ("name","address")
		verbose_name_plural = "Organizations"
		verbose_name = "Organization"
		ordering = ['-updated_at']



class MainMixin(models.Model):
	organization = models.ForeignKey(Organization, on_delete = models.PROTECT, related_name = 'organization_staff_object', verbose_name = 'Organization')

	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')



class Organization_number(MainMixin):
	number = PhoneNumberField(unique = True)


	class Meta:
		db_table = 'Organization_number'
		verbose_name_plural = "Organizations' numbers"
		verbose_name = "Organization's number"
		ordering = ['-updated_at']



class Organization_link(MainMixin):
	link = RegexValidator(regex = r"^(https?:\/\/)?([\w-]{1,32}\.[\w-]{1,32})[^\s@]*$")


	class Meta:
		db_table = 'Organization_link'
		verbose_name_plural = "Organizations' link"
		verbose_name = "Organization's link"
		ordering = ['-updated_at']



class Service(MainMixin):
	name = models.CharField(max_length = 150, unique = True, verbose_name = 'Name')
	number = PhoneNumberField(unique = True, verbose_name = 'Number')
	address = models.CharField(max_length = 200, verbose_name = 'Address')


	class Meta:
		db_table = 'Service'
		verbose_name_plural = "Organizations' link"
		verbose_name = "Organization's link"
		ordering = ['-updated_at']



class Permission(models.Model):
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')


	class Meta:
		db_table = 'Permission'
		verbose_name_plural = 'Permissions'
		verbose_name = 'Permission'
		ordering = ['-created_at']



class Role(models.Model):
	permissions = models.ManyToManyField(Permission, related_name = 'permission_roles', verbose_name = 'Permissions')
	user = models.ForeignKey(get_user_model(), on_delete = models.PROTECT, related_name = 'user_role', verbose_name = 'User')
	organization = models.ForeignKey(Organization, on_delete = models.PROTECT, related_name = 'organization_roles', verbose_name = 'Organization')

	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')


	class Meta:
		db_table = 'Role'
		verbose_name_plural = 'Roles'
		verbose_name = 'Role'
		ordering = ['-updated_at']