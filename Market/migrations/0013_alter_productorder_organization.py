# Generated by Django 3.2.7 on 2021-10-25 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0005_alter_organization_member_second_name'),
        ('Market', '0012_auto_20211025_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productorder',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_product_order', to='Organizations.organization', verbose_name='Organization'),
        ),
    ]
