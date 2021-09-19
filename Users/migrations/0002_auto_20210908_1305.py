# Generated by Django 3.2.7 on 2021-09-08 13:05

import django.core.validators
from django.db import migrations, models
import django_resized.forms
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, null=True, unique=True, validators=[django.core.validators.EmailValidator], verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='../static/Users/default-user-image.jpeg', force_format=None, keep_meta=True, quality=0, size=[1920, 1080], upload_to='../static/Users/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None, unique=True, verbose_name='Phone'),
        ),
    ]
