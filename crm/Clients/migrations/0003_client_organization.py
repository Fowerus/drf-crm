# Generated by Django 3.2.6 on 2021-08-20 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0003_auto_20210820_1452'),
        ('Clients', '0002_client_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='organization',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_client', to='Organizations.organization', verbose_name='Organization'),
            preserve_default=False,
        ),
    ]
