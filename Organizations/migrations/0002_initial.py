# Generated by Django 3.2.7 on 2021-10-21 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization_member',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_member', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='organization',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_organizations', to=settings.AUTH_USER_MODEL, verbose_name='Creator'),
        ),
        migrations.AlterUniqueTogether(
            name='custompermission',
            unique_together={('name', 'codename')},
        ),
        migrations.AlterUniqueTogether(
            name='service',
            unique_together={('name', 'organization')},
        ),
        migrations.AlterUniqueTogether(
            name='role',
            unique_together={('name', 'organization')},
        ),
        migrations.AlterUniqueTogether(
            name='organization_member',
            unique_together={('user', 'organization')},
        ),
        migrations.AlterUniqueTogether(
            name='organization',
            unique_together={('name', 'address')},
        ),
    ]
