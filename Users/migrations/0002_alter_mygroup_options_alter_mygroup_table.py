# Generated by Django 4.0.1 on 2022-02-05 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mygroup',
            options={'permissions': [('change_user_group', 'Can change user group')], 'verbose_name': 'MyGroup', 'verbose_name_plural': 'MyGroups'},
        ),
        migrations.AlterModelTable(
            name='mygroup',
            table='mygroup',
        ),
    ]