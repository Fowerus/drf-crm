# Generated by Django 4.0.1 on 2022-02-02 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('data', models.JSONField(blank=True, null=True)),
                ('method', models.CharField(max_length=150, null=True, verbose_name='Method')),
                ('process', models.CharField(max_length=150, verbose_name='Process')),
                ('model', models.CharField(choices=[('0', 'ProductOrder'), ('1', 'WorkDone'), ('2', 'SaleOrder'), ('3', 'Order'), ('4', 'OrderHistory')], max_length=150, verbose_name='Model name')),
            ],
            options={
                'verbose_name': 'ActionHistory',
                'verbose_name_plural': 'ActionHistories',
                'db_table': 'actionhistory',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='DeviceAppearance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('data', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'DeviceAppearance',
                'verbose_name_plural': 'DeviceAppearances',
                'db_table': 'deviceappearance',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='DeviceDefect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('data', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'DeviceDefect',
                'verbose_name_plural': 'DeviceDefects',
                'db_table': 'devicedefect',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='DeviceKit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('data', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'DeviceKit',
                'verbose_name_plural': 'DeviceKits',
                'db_table': 'devicekit',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='DeviceMaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('data', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'DeviceMaker',
                'verbose_name_plural': 'DeviceMakers',
                'db_table': 'devicemaker',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='DeviceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('data', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'DeviceModel',
                'verbose_name_plural': 'DeviceModels',
                'db_table': 'devicemodel',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='DeviceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('data', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
                'verbose_name': 'DeviceType',
                'verbose_name_plural': 'DeviceTypes',
                'db_table': 'devicetype',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('data', models.JSONField(blank=True, null=True)),
                ('comment', models.TextField(null=True, verbose_name='Comment')),
            ],
            options={
                'verbose_name': 'OrderHistory',
                'verbose_name_plural': 'OrderHistories',
                'db_table': 'orderhistory',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='ServicePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('data', models.JSONField(blank=True, null=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('price', models.FloatField()),
            ],
            options={
                'verbose_name': 'ServicePrice',
                'verbose_name_plural': 'ServicePrices',
                'db_table': 'serviceprice',
                'ordering': ['-updated_at'],
            },
        ),
    ]
