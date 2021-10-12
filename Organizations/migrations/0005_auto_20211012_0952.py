# Generated by Django 3.2.7 on 2021-10-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0004_alter_role_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization_member',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='role',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
