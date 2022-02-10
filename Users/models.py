import uuid

from django.contrib.auth.models import GroupManager, Permission

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core import validators

from phonenumber_field.modelfields import PhoneNumberField

from .mixins import GroupPermissionMixin

from core.utils.atomic_exception import MyCustomError


class MyGroup(models.Model):

    name = models.CharField('name', max_length=150)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name='permissions',
        related_name="mygroup_permissions",
        blank=True,
    )
    organization = models.ForeignKey(
        'Organizations.Organization', on_delete=models.CASCADE, related_name='mygroup_organizations')
    service = models.ForeignKey(
        'Organizations.Service', blank=True, on_delete=models.CASCADE,  null=True, related_name='mygroup_services')

    objects = GroupManager()

    class Meta:
        unique_together = ('name', 'organization', 'service')
        db_table = 'mygroup'
        verbose_name = 'MyGroup'
        verbose_name_plural = 'MyGroups'
        permissions = [('change_user_group', 'Can change user group')]

    def __str__(self):
        return f'id: {self.id} | name {self.name} | {self.organization} | service {self.service}'

    def save(self, *args, **kwargs):
        if self.service == None:
            if self.__class__.objects.filter(~models.Q(id=self.id)).filter(name=self.name, organization=self.organization, service=None):
                raise MyCustomError(
                    'The fields name, organization, service must make a unique set.', 400)
        
        super().save(*args, **kwargs)


    def natural_key(self):
        return (self.name,)


    def calculateName(self):
        self.name += f'_{self.organization.id}_{self.service.id}' if self.service else f'_{self.organization.id}'

    def getService(self):
        if self.service is None:
            return self.service
        return self.service.id


class UserManager(BaseUserManager):
    def _create_user(self, surname=None, first_name=None, second_name=None, email=None, phone=None, address=None, password=None, **extra_fields):
        if email is not None:
            email = self.normalize_email(email)
        user = self.model(surname=surname, first_name=first_name, second_name=second_name,
                          address=address, email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, surname=None, first_name=None, second_name=None, email=None, phone=None, address=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(surname=surname, first_name=first_name, second_name=second_name, address=address, email=email, phone=phone, password=password, **extra_fields)

    def create_superuser(self, surname=None, first_name=None, second_name=None, email=None, phone=None, address=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(surname=surname, first_name=first_name, second_name=second_name, address=address, email=email, phone=phone, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, GroupPermissionMixin):
    surname = models.CharField(
        max_length=150, null=True, verbose_name='Surname')
    first_name = models.CharField(
        max_length=150, null=True, verbose_name='First name')
    second_name = models.CharField(
        max_length=150, null=True, verbose_name='Second name')

    email = models.CharField(validators=[validators.EmailValidator], max_length=100,
                             unique=True, blank=True, null=True, verbose_name='Email')
    phone = PhoneNumberField(unique=True, blank=True,
                             null=True, verbose_name='Phone')
    address = models.CharField(
        max_length=200, verbose_name='Address', null=True)

    avatar = models.ImageField(
        upload_to='avatars/', max_length=255, null=False,
        blank=False,
        verbose_name='Avatar',
        default='https://thumbs.dreamstime.com/z/' +
        'no-sign-vector-no-sign-vector-icon-art-101329606.jpg')

    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created_at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated_at')

    current_org = models.IntegerField(null = True)
    groups = models.ManyToManyField(MyGroup, blank = True,
        related_name = 'mygroups_users',
        verbose_name = 'Groups')

    confirmed_email = models.BooleanField(default=False)
    confirmed_phone = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    data = models.JSONField(null=True, blank=True)

    sessions = models.JSONField(blank = True, default = list)
    services = models.JSONField(blank = True, default = list)

    code = models.IntegerField(null = True, blank = True, verbose_name = 'Code')
    code_expired_at = models.DateTimeField(null = True, blank = True, verbose_name = 'Code expired time')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ('surname', 'first_name', 'second_name', 'address')

    objects = UserManager()

    def __str__(self):
        return f'id: {self.id} | email: {self.email} | phone: {self.phone}'

    @property
    def confirmed(self):
        if self._check_confirmed() == False: 
            raise MyCustomError('Account not confirmed', 403)

        return self._check_confirmed

    def _check_confirmed(self):
        return bool(self.confirmed_phone or self.confirmed_email)

    class Meta:
        db_table = 'User'.lower()
        verbose_name_plural = 'Users'
        verbose_name = 'User'
        ordering = ['-created_at']
