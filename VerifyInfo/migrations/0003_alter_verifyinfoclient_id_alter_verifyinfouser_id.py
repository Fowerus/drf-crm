# Generated by Django 4.0 on 2021-12-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VerifyInfo', '0002_auto_20211123_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifyinfoclient',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='verifyinfouser',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
