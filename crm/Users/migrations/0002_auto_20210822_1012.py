# Generated by Django 3.2.6 on 2021-08-22 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='verifyinfo',
            options={'ordering': ['-updated_at'], 'verbose_name': 'VerifyInfo', 'verbose_name_plural': 'VerifyInfoes'},
        ),
        migrations.RenameField(
            model_name='verifyinfo',
            old_name='created_at',
            new_name='updated_at',
        ),
    ]