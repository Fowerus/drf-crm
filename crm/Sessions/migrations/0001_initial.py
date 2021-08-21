# Generated by Django 3.2.6 on 2021-08-21 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.CharField(max_length=150, verbose_name='Device')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_sessions', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Session',
                'verbose_name_plural': 'Sessions',
                'db_table': 'Session',
                'ordering': ['-updated_at'],
                'unique_together': {('user', 'device')},
            },
        ),
    ]
