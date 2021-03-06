# Generated by Django 4.0.1 on 2022-02-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Organizations', '0006_mygroup'),
        ('Users', '0009_alter_user_code_alter_user_code_expired_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='mygroups_users', to='Organizations.MyGroup', verbose_name='Groups'),
        ),
        migrations.DeleteModel(
            name='MyGroup',
        ),
    ]
