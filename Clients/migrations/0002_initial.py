# Generated by Django 3.2.7 on 2021-10-21 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clients', '0001_initial'),
        ('Organizations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcard',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_client_card', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='client',
            name='organization',
            field=models.ManyToManyField(related_name='organization_clients', to='Organizations.Organization', verbose_name='Organization'),
        ),
        migrations.AlterUniqueTogether(
            name='clientcard',
            unique_together={('organization', 'phone')},
        ),
    ]