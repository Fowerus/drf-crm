# Generated by Django 3.2.6 on 2021-08-25 07:03

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_auto_20210824_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Number'),
        ),
        migrations.AlterField(
            model_name='verifyinfo',
            name='type_code',
            field=models.CharField(max_length=10, verbose_name='Type_code'),
        ),
    ]
