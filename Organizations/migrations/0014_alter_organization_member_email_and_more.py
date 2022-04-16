# Generated by Django 4.0 on 2021-12-27 17:01

import django.core.validators
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0013_alter_mprovider_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization_member',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.EmailValidator], verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='organization_member',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Phone'),
        ),
    ]