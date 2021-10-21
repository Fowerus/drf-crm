# Generated by Django 3.2.7 on 2021-10-21 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Clients', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyInfoClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('client', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Clients.client', verbose_name='Client')),
            ],
            options={
                'verbose_name': 'VerifyInfoClient',
                'verbose_name_plural': 'VerifyInfoClient',
                'db_table': 'verifyinfoclient',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='VerifyInfoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(unique=True)),
                ('type_code', models.CharField(choices=[(0, 'phone'), (1, 'email'), (2, 'reset')], max_length=10, verbose_name='Type_code')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'VerifyInfoUser',
                'verbose_name_plural': 'VerifyInfoUsers',
                'db_table': 'verifyinfouser',
                'ordering': ['-created_at'],
                'unique_together': {('user', 'type_code')},
            },
        ),
    ]
