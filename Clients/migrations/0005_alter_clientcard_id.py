# Generated by Django 4.0 on 2021-12-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0004_alter_clientcard_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcard',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
