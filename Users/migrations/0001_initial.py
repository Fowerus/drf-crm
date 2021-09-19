# Generated by Django 3.2.7 on 2021-09-05 07:41

import django.core.validators
from django.db import migrations, models
import django_resized.forms
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('surname', models.CharField(max_length=150, verbose_name='Surname')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('patronymic', models.CharField(max_length=150, verbose_name='Patronymic')),
                ('email', models.CharField(blank=True, max_length=100, null=True, unique=True, validators=[django.core.validators.EmailValidator], verbose_name='Email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Phone')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='../static/Users/default-user-image.jpeg', force_format=None, keep_meta=True, quality=0, size=[1920, 1080], upload_to='../static/Users/', verbose_name='Image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('confirmed_email', models.BooleanField(default=False)),
                ('confirmed_phone', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'User',
                'ordering': ['-created_at'],
            },
        ),
    ]