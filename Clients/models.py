import jwt

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField

from Organizations.models import Organization, MainMixin



class Client(AbstractBaseUser):
	surname = models.CharField(max_length = 150, verbose_name = 'Surname', blank = True)
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	patronymic = models.CharField(max_length = 150, verbose_name = 'Patronymic', blank = True)
	address = models.CharField(max_length = 200, verbose_name = 'Address', blank = True)
	phone = PhoneNumberField(unique = True,  verbose_name = 'Phone')
	image = models.CharField(max_length = 300, verbose_name = 'Image')
	links = models.JSONField(null = True)

	data = models.JSONField(null = True, blank = True)
	
	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')

	confirmed_phone = models.BooleanField(default = False)

	organization = models.ManyToManyField(Organization, related_name = 'organization_clients', verbose_name = 'Organization')

	USERNAME_FIELD = "phone"

	REQUIRED_FIELDS = ('name',)


	def __str__(self):
		return f"id: {self.id} | phone: {self.phone}"


	@property
	def token(self):
		return self._generate_jwt_token()


	def _generate_jwt_token(self):
		token_encode = jwt.encode({
			'client_id': self.pk,
			'surname':self.surname,
			'first_name':self.name,
			'patronymic':str(self.patronymic),
			'phone':self.phone.raw_input,
		}, settings.SECRET_KEY, algorithm='HS256')

		return token_encode


	class Meta:
		db_table = 'Client'.lower()
		verbose_name_plural = 'Clients'
		verbose_name = 'Client'
		ordering = ['-updated_at']


		
class ClientCard(MainMixin):
	client = models.ForeignKey(Client, on_delete = models.SET_NULL, related_name = 'client_client_card', null = True, verbose_name = 'Client')

	surname = models.CharField(max_length = 150, verbose_name = 'Surname', blank = True)
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	patronymic = models.CharField(max_length = 150, verbose_name = 'Patronymic', blank = True)
	address = models.CharField(max_length = 200, verbose_name = 'Address', blank = True)
	phone = PhoneNumberField(verbose_name = 'Phone')
	links = models.JSONField(null = True)
	image = models.CharField(max_length = 300, null = True, verbose_name = 'Image')

	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'organization_client_card', verbose_name = 'Organization')


	def __str__(self):
		return f"id: {self.id} | client: {self.client.id} | organization : {self.organization.id}"


	class Meta:
		db_table = 'ClientCard'.lower()
		unique_together = ('organization', 'phone')
		verbose_name_plural = 'ClientsCards'
		verbose_name = 'ClientCard'
		ordering = ['-updated_at']