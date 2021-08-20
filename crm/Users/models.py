from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators

from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField



class UserManager(BaseUserManager):
	def _create_user(self, surname, name, patronymic, email, address= None, password = None, **extra_fields):
		email = self.normalize_email(email)
		user = self.model(surname = surname, name = name, patronymic = patronymic, address = address, email = email, **extra_fields)
		user.set_password(password)
		user.save(using = self._db)

		return user


	def create_user(self, surname, name, patronymic, email, address= None, password = None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)

		return self._create_user(surname = surname, name = name, patronymic = patronymic, address = address, email = email, password = password, **extra_fields)


	def create_superuser(self, surname, name, patronymic, email, address= None, password = None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		return self._create_user(surname = surname, name = name, patronymic = patronymic, address = address, email = email, password = password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
	surname = models.CharField(max_length = 150, verbose_name = 'Surname')
	name = models.CharField(max_length = 150, verbose_name = 'Name')
	patronymic = models.CharField(max_length = 150, verbose_name = 'Patronymic')

	email = models.CharField(validators = [validators.EmailValidator], max_length = 100, unique = True, blank = True, verbose_name = 'Email')
	address = models.CharField(max_length = 200, verbose_name = 'Address', blank = True)

	full_image = ResizedImageField(crop=['middle', 'center'], upload_to = '../static/Users/', blank = True, default = '../static/Users/default-user-image.jpeg', verbose_name = 'Image')
	small_image = ResizedImageField(size = [255,255], crop = ['middle', 'center'], upload_to = '../static/Users/', blank = True, default = '../static/Users/default-user-image.jpeg', verbose_name = 'Image')

	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')

	is_staff = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)
	
	USERNAME_FIELD = "email"

	REQUIRED_FIELDS = ('surname','name', 'patronymic', 'address')

	objects = UserManager()


	class Meta:
		db_table = 'User'
		verbose_name_plural = 'Users'
		verbose_name = 'User'
		ordering = ['-created_at']