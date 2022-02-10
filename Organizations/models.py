import jwt
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.core import validators

from phonenumber_field.modelfields import PhoneNumberField

from core.utils.helper import MainMixin, defaultMProviderData


class Organization(MainMixin):
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    description = models.CharField(max_length=500, verbose_name='Description')
    address = models.CharField(max_length=200, verbose_name='Address')

    logo = models.TextField(null=True, blank=True, verbose_name='Logo')

    creator = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                                null=True, related_name='my_organizations', verbose_name='Creator')
    numbers = models.JSONField(null=True, blank=True)
    links = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f'id: {self.id} | creator: {self.creator}'

    class Meta:
        db_table = 'Organization'.lower()
        verbose_name_plural = "Organizations"
        verbose_name = "Organization"
        ordering = ['-updated_at']


class Service(MainMixin):
    prefix = models.CharField(
        max_length=10, unique=True, verbose_name='Prefix')
    name = models.CharField(max_length=150, unique=True, verbose_name='Name')
    phone = PhoneNumberField(unique=True, verbose_name='Phone')
    address = models.CharField(max_length=200, verbose_name='Address')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,
                                     related_name='organization_services', verbose_name='Organization')

    def __str__(self):
        return f'id: {self.id} | name: {self.name} | org: {self.organization}'

    class Meta:
        unique_together = ('name', 'organization')
        db_table = 'Service'.lower()
        verbose_name_plural = "Services"
        verbose_name = "Service"
        ordering = ['-updated_at']


class Organization_member(MainMixin):
    user = models.ForeignKey(get_user_model(
    ), on_delete=models.CASCADE, related_name='user_member', verbose_name='User')

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,
                                     related_name='organization_members', verbose_name='Organization')
    service = models.ForeignKey(Service, on_delete = models.SET_NULL, null = True, blank = True,
        related_name = 'service_members', verbose_name = 'Service')

    surname = models.CharField(
        max_length=150, null=True, blank=True, verbose_name='Surname')
    first_name = models.CharField(
        max_length=150, null=True, blank=True, verbose_name='First name')
    second_name = models.CharField(
        max_length=150, null=True, blank=True, verbose_name='Second name')

    email = models.CharField(validators=[
                             validators.EmailValidator], max_length=100, blank=True, null=True, verbose_name='Email')
    phone = PhoneNumberField(blank=True, null=True, verbose_name='Phone')
    address = models.CharField(
        max_length=200, null=True, blank=True, verbose_name='Address')

    avatar = models.TextField(null=True, blank=True, verbose_name='Avatar')

    pass_series = models.CharField(
        max_length=4, null=True, blank=True, verbose_name='Passport series')
    pass_number = models.CharField(
        max_length=6, null=True, blank=True, verbose_name='Passport number')

    def __str__(self):
        return f'id: {self.id} | user: {self.user}'

    class Meta:
        unique_together = ('user', 'organization')
        db_table = 'Organization_member'.lower()
        verbose_name_plural = 'Organizations members'
        verbose_name = 'Organization member'
        ordering = ['-updated_at']


class MProvider(MainMixin):
    site = models.CharField(max_length=300, verbose_name='Site')

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE,
                                     related_name='organization_mprovider', verbose_name='Organization')
    service = models.ForeignKey(Service, on_delete = models.SET_NULL, null = True, blank = True,
        related_name = 'service_mprovider', verbose_name = 'Service')

    data = models.JSONField(default=defaultMProviderData, verbose_name="Data")

    def __str__(self):
        return f'id: {self.id} | site: {self.site}'

    @property
    def generate_token(self):
        token_encode = jwt.encode({
            'id': self.id,
            'site': self.site,
            'organization': self.organization.id,
            'data': self.data
        }, settings.SECRET_KEY, algorithm='HS256')

        return token_encode

    class Meta:
        db_table = 'mprovider'
        verbose_name_plural = 'MProviders'
        verbose_name = 'MProvider'
        ordering = ['-updated_at']
