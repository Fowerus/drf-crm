# Generated by Django 4.0 on 2021-12-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0004_alter_order_id_alter_orderstatus_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='orderstatus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]