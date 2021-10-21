# Generated by Django 3.2.7 on 2021-10-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0005_alter_orderstatus_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='type',
            field=models.CharField(choices=[('0', 'New'), ('1', 'Pending'), ('2', 'In progress'), ('3', 'Completed'), ('4', 'Issued')], max_length=150, null=True, verbose_name='Type'),
        ),
    ]
