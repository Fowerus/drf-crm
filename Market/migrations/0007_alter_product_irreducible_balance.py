# Generated by Django 3.2.7 on 2021-10-25 08:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0006_remove_transaction_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='irreducible_balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Irreducible balance'),
        ),
    ]
