# Generated by Django 3.2.7 on 2021-09-08 13:08

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20210908_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='../static/Users/default-user-image.jpeg', force_format=None, keep_meta=True, quality=0, size=[1920, 1080], upload_to='../static/Users/', verbose_name='Image'),
        ),
    ]