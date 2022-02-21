import uuid

from django.core.mail import send_mail
from django.utils import timezone
from django.core import validators
from django.conf import settings

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

from phonenumber_field.modelfields import PhoneNumberField

from .mixins import GroupPermissionMixin

from core.utils.atomic_exception import MyCustomError



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
    groups = models.ManyToManyField('Organizations.MyGroup', blank = True,
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

    code = models.IntegerField(null = True, blank = True,
        verbose_name = 'Code')
    code_expired_at = models.DateTimeField(null = True, blank = True,
        verbose_name = 'Code expired time')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ('surname', 'first_name', 'second_name', 'address')

    objects = UserManager()


    def __str__(self):
        return f'id: {self.id} | email: {self.email} | phone: {self.phone}'


    def __check_confirmed(self):
        return bool(self.confirmed_phone or self.confirmed_email)


    def __send_to_email(self):
        self.generate_code()

        send_mail(
            'Test app',
            settings.SEND_MESSAGE % self.code,
            settings.EMAIL_HOST_USER,
            [self.email],
            fail_silently=False
        )


    def __send_to_phone(self):
        pass


    @property
    def confirmed(self):
        if self.__check_confirmed() == False: 
            raise MyCustomError('Account not confirmed', 403)

        return self._check_confirmed


    @property
    def code_is_expired(self):
        return timezone.now() > self.code_expired_at


    def generate_code(self):
        code = int(str(uuid.uuid1().int)[:6])
        self.code = code
        self.code_expired_at = timezone.now() + settings.CODE_LIFETIME

        self.save() 


    def send_code(self, field:str):
        try:
            data = {'email':self.__send_to_email, 'phone':self.__send_to_phone}

            return data[field]()
        except:
            raise MyCustomError('Code send error', 500)


    def set_session(self, device, session):
        try:
            self.sessions.append(session)
            self.save()
        except Exception as e:
            raise MyCustomError('Set session error', 500)


    class Meta:
        db_table = 'User'.lower()
        verbose_name_plural = 'Users'
        verbose_name = 'User'
        ordering = ['-created_at']
