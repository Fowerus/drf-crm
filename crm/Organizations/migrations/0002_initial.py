# Generated by Django 3.2.6 on 2021-08-19 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Organizations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='organization_member',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_member', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='organization_link',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_links', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='organization',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='my_organizations', to=settings.AUTH_USER_MODEL, verbose_name='creator'),
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_orders', to=settings.AUTH_USER_MODEL, verbose_name='Client'),
        ),
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
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service_orders', to='Organizations.service', verbose_name='Service'),
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together={('name', 'organization')},
        ),
        migrations.AlterUniqueTogether(
            name='organization_number',
            unique_together={('number', 'organization')},
        ),
        migrations.AlterUniqueTogether(
            name='organization_member',
            unique_together={('user', 'organization')},
        ),
        migrations.AlterUniqueTogether(
            name='organization_link',
            unique_together={('link', 'organization')},
        ),
        migrations.AlterUniqueTogether(
            name='organization',
            unique_together={('name', 'address')},
        ),
    ]
