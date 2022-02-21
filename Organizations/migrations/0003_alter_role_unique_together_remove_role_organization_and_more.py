# Generated by Django 4.0.1 on 2022-02-05 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0002_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='role',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='role',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='role',
            name='permissions',
        ),
        migrations.RemoveField(
            model_name='organization_member',
            name='role',
        ),
        migrations.AddField(
            model_name='organization_member',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='service_members', to='Organizations.service', verbose_name='Service'),
        ),
        migrations.DeleteModel(
            name='CustomPermission',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]