# Generated by Django 3.2.7 on 2021-10-21 16:35

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('surname', models.CharField(blank=True, max_length=150, verbose_name='Surname')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('patronymic', models.CharField(blank=True, max_length=150, verbose_name='Patronymic')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Address')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Phone')),
                ('image', models.CharField(blank=True, max_length=300, null=True, verbose_name='Image')),
                ('links', models.JSONField(blank=True, null=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('confirmed_phone', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'client',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='ClientCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('data', models.JSONField(blank=True, null=True)),
                ('surname', models.CharField(blank=True, max_length=150, verbose_name='Surname')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('patronymic', models.CharField(blank=True, max_length=150, verbose_name='Patronymic')),
                ('address', models.CharField(blank=True, max_length=200, verbose_name='Address')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Phone')),
                ('links', models.JSONField(null=True)),
                ('image', models.CharField(max_length=300, null=True, verbose_name='Image')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_client_card', to='Clients.client', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'ClientCard',
                'verbose_name_plural': 'ClientsCards',
                'db_table': 'clientcard',
                'ordering': ['-updated_at'],
            },
        ),
    ]
