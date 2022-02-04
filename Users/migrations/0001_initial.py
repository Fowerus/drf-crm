# Generated by Django 4.0.1 on 2022-02-04 13:28

import Users.mixins
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mygroup_organizations', to='Organizations.organization')),
                ('permissions', models.ManyToManyField(blank=True, related_name='mygroup_permissions', to='auth.Permission', verbose_name='permissions')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mygroup_services', to='Organizations.service')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
                'db_table': 'group',
                'permissions': [('change_user_group', 'Can change user group')],
                'unique_together': {('name', 'organization', 'service')},
            },
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('surname', models.CharField(max_length=150, null=True, verbose_name='Surname')),
                ('first_name', models.CharField(max_length=150, null=True, verbose_name='First name')),
                ('second_name', models.CharField(max_length=150, null=True, verbose_name='Second name')),
                ('email', models.CharField(blank=True, max_length=100, null=True, unique=True, validators=[django.core.validators.EmailValidator], verbose_name='Email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True, verbose_name='Phone')),
                ('address', models.CharField(max_length=200, null=True, verbose_name='Address')),
                ('avatar', models.ImageField(default='https://thumbs.dreamstime.com/z/no-sign-vector-no-sign-vector-icon-art-101329606.jpg', max_length=255, upload_to='avatars/', verbose_name='Avatar')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('current_org', models.IntegerField(null=True)),
                ('confirmed_email', models.BooleanField(default=False)),
                ('confirmed_phone', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('data', models.JSONField(blank=True, null=True)),
                ('sessions', models.JSONField(blank=True, null=True)),
                ('services', models.JSONField(blank=True, null=True)),
                ('groups', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mygroups_users', to='Users.mygroup', verbose_name='Groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
                'ordering': ['-created_at'],
            },
            bases=(models.Model, Users.mixins.GroupPermissionMixin),
        ),
    ]
