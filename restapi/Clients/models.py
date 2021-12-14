import jwt

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField

from Organizations.models import Organization
from restapi.helper import MainMixin



class Client(AbstractBaseUser):
	surname = models.CharField(max_length = 150, verbose_name = 'Surname', blank = True)
	first_name = models.CharField(max_length = 150, verbose_name = 'First name')
	second_name = models.CharField(max_length = 150, verbose_name = 'Second name', blank = True)
	address = models.CharField(max_length = 200, verbose_name = 'Address', blank = True)
	phone = PhoneNumberField(unique = True,  verbose_name = 'Phone')
	avatar = models.CharField(max_length = 300, null = True, blank = True, verbose_name = 'Avatar')

	links = models.JSONField(null = True, blank = True)
	data = models.JSONField(null = True, blank = True)
	
	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')

	confirmed_phone = models.BooleanField(default = False)

	organization = models.ManyToManyField(Organization, related_name = 'organization_clients', verbose_name = 'Organization')

	USERNAME_FIELD = "phone"

	REQUIRED_FIELDS = ('first_name',)


	def __str__(self):
		return f"id: {self.id} | phone: {self.phone}"


	class Meta:
		db_table = 'Client'.lower()
		verbose_name_plural = 'Clients'
		verbose_name = 'Client'
		ordering = ['-updated_at']


		
class ClientCard(MainMixin):
	client = models.ForeignKey(Client, on_delete = models.SET_NULL, related_name = 'client_client_card', null = True, verbose_name = 'Client')

	surname = models.CharField(max_length = 150, verbose_name = 'Surname', blank = True)
	first_name = models.CharField(max_length = 150, verbose_name = 'First name')
	second_name = models.CharField(max_length = 150, verbose_name = 'Second name', blank = True)
	address = models.CharField(max_length = 200, verbose_name = 'Address', blank = True)
	phone = PhoneNumberField(verbose_name = 'Phone')
	links = models.JSONField(null = True)
	avatar = models.CharField(max_length = 300, null = True, verbose_name = 'Avatar')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_client_card', verbose_name = 'Organization')


	def __str__(self):
		return f"id: {self.id} | client: {self.client} | organization : {self.organization.id}"


	class Meta:
		db_table = 'ClientCard'.lower()
		unique_together = ('organization', 'phone')
		verbose_name_plural = 'ClientsCards'
		verbose_name = 'ClientCard'
		ordering = ['-updated_at']