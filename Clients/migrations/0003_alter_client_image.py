# Generated by Django 3.2.7 on 2021-10-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Clients', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='image',
            field=models.CharField(max_length=300, null=True, verbose_name='Image'),
        ),
    ]
