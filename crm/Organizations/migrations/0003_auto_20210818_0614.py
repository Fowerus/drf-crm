# Generated by Django 3.2.6 on 2021-08-18 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Organizations', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='user',
        ),
        migrations.CreateModel(
            name='Organization_member',
            fields=[
                ('mainmixin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Organizations.mainmixin')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='role_member', to='Organizations.role', verbose_name='Role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_member', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Organization_member',
                'verbose_name_plural': 'Organization_members',
                'db_table': 'Organization_member',
                'ordering': ['-updated_at'],
            },
            bases=('Organizations.mainmixin',),
        ),
    ]
