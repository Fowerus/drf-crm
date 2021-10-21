# Generated by Django 3.2.7 on 2021-10-21 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Organizations', '0001_initial'),
        ('Orders', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_creator', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AddField(
            model_name='order',
            name='executor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_executor', to=settings.AUTH_USER_MODEL, verbose_name='Executor'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order_status_order', to='Orders.orderstatus', verbose_name='OrderStatus'),
        ),
        migrations.AddField(
            model_name='order',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_orders', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='order',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service_orders', to='Organizations.service', verbose_name='Service'),
        ),
    ]
