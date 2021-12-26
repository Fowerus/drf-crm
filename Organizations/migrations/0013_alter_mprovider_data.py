# Generated by Django 4.0 on 2021-12-26 10:49

from django.db import migrations, models
import restapi.helper


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0012_alter_mprovider_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mprovider',
            name='data',
            field=models.JSONField(default=restapi.helper.defaultMProviderData, verbose_name='Data'),
        ),
    ]
