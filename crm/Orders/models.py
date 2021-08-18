from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
from django.contrib.auth.models import PermissionsMixin
from django.core import validators

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField
from Organizations.models import MainMixin


class Order(models.Model):
	order_code = models.BigIntegerField()
	client = models.ForeignKey(get_user_model(), on_delete = models.PROTECT, related_name = 'client_orders')
	executor = models.ForeignKey(get_user_model(), on_delete = models.PROTECT, related_name = 'user_executor')
	creator = models.ForeignKey(get_user_model(), on_delete = models.PROTECT, related_name = 'user_creator')

	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')


	class Meta:
		db_table = 'Order'
		verbose_name_plural = "Orders"
		verbose_name = "Order"
		ordering = ['-updated_at']
