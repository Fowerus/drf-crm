# Generated by Django 4.0.1 on 2022-02-05 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_user_services_alter_user_sessions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='services',
            field=models.JSONField(blank=True, default=[]),
        ),
        migrations.AlterField(
            model_name='user',
            name='sessions',
            field=models.JSONField(blank=True, default=[]),
        ),
    ]
