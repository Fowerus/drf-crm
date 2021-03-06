# Generated by Django 4.0.1 on 2022-02-04 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Handbook', '0001_initial'),
        ('Orders', '0001_initial'),
        ('Organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceprice',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_service_price', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='action_history',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='action_history_order_history', to='Handbook.actionhistory', verbose_name='Action history'),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_order_history', to='Orders.order', verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='orderhistory',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_order_history', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='devicetype',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_device_type', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='devicemodel',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_device_model', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='devicemaker',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_device_maker', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='devicekit',
            name='devicetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='device_type_device_kit', to='Handbook.devicetype', verbose_name='DeviceType'),
        ),
        migrations.AddField(
            model_name='devicekit',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_device_kit', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='devicedefect',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_device_defect', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='deviceappearance',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_device_appearance', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AlterUniqueTogether(
            name='actionhistory',
            unique_together={('method', 'model')},
        ),
    ]
