# Generated by Django 3.2.7 on 2021-10-24 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_rename_patronymic_user_second_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='second_name',
            field=models.CharField(max_length=150, verbose_name='Second name'),
        ),
    ]
