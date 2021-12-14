import uuid

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators

from phonenumber_field.modelfields import PhoneNumberField



class UserManager(BaseUserManager):
	def _create_user(self, surname = None, first_name = None, second_name = None, email = None, phone = None, address = None, password = None, **extra_fields):
		if not email is None:
			email = self.normalize_email(email)
		user = self.model(surname = surname, first_name = first_name, second_name = second_name, address = address, email = email, phone = phone, **extra_fields)
		user.set_password(password)
		user.save(using = self._db)

		return user


	def create_user(self, surname = None, first_name = None, second_name = None, email = None, phone = None, address= None, password = None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)

		return self._create_user(surname = surname, first_name = first_name, second_name = second_name, address = address, email = email,phone = phone, password = password, **extra_fields)


	def create_superuser(self, surname = None, first_name = None, second_name = None, email = None, phone = None, address= None, password = None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		return self._create_user(surname = surname, first_name = first_name, second_name = second_name, address = address, email = email, phone = phone, password = password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
	surname = models.CharField(max_length = 150, null = True, verbose_name = 'Surname')
	first_name = models.CharField(max_length = 150, null = True, verbose_name = 'First name')
	second_name = models.CharField(max_length = 150, null = True, verbose_name = 'Second name')

	email = models.CharField(validators = [validators.EmailValidator], max_length = 100, unique = True, blank = True, null = True, verbose_name = 'Email')
	phone = PhoneNumberField(unique = True, blank = True, null = True, verbose_name = 'Phone')
	address = models.CharField(max_length = 200, verbose_name = 'Address', null = True)

	avatar = models.CharField(max_length = 300, null = True, blank = True, verbose_name = 'Avatar')

	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')

	confirmed_email = models.BooleanField(default = False)
	confirmed_phone = models.BooleanField(default = False)

	is_staff = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)

	data = models.JSONField(null = True, blank = True)
	
	USERNAME_FIELD = "email"

	REQUIRED_FIELDS = ('surname','first_name', 'second_name', 'address')

	objects = UserManager()


	def __str__(self):
		return f'id: {self.id} | email: {self.email} | phone: {self.phone}'
		

	@property
	def confirmed(self):
		return self._check_confirmed()


	def _check_confirmed(self):
		return bool(self.confirmed_phone or self.confirmed_email)


	class Meta:
		db_table = 'User'.lower()
		verbose_name_plural = 'Users'
		verbose_name = 'User'
		ordering = ['-created_at']
	
