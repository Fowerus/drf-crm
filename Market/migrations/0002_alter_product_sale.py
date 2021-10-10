# Generated by Django 3.2.7 on 2021-10-10 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Market', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sale_product', to='Market.sale', verbose_name='Sale'),
        ),
    ]
