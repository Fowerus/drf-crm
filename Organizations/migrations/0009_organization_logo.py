# Generated by Django 4.0 on 2021-12-23 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0008_alter_organization_member_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='logo',
            field=models.TextField(blank=True, null=True, verbose_name='Logo'),
        ),
    ]
