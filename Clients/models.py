import jwt

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField

from Organizations.models import Organization



class Client(AbstractBaseUser):
	surname = models.CharField(max_length = 150, verbose_name = 'Surname', blank = True)
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	patronymic = models.CharField(max_length = 150, verbose_name = 'Patronymic', blank = True)
	address = models.CharField(max_length = 200, verbose_name = 'Address', blank = True)
	phone = PhoneNumberField(unique = True,  verbose_name = 'Phone')
	image = ResizedImageField(crop=['middle', 'center'], upload_to = '../static/Users/', default = '../static/Users/default-user-image.jpeg', verbose_name = 'Image')
	links = models.JSONField(null = True)
	
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
		db_table = 'Client'
		verbose_name_plural = 'Clients'
		verbose_name = 'Client'
		ordering = ['-updated_at']
		