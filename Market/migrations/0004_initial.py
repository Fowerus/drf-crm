# Generated by Django 3.2.7 on 2021-10-21 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clients', '0002_initial'),
        ('Orders', '0002_initial'),
        ('Organizations', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Market', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='workdone',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_work_done', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='cashbox',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cashbox_transaction', to='Market.cashbox', verbose_name='Cashbox'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_transaction', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='purchase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_transaction', to='Market.purchaserequest', verbose_name='Purchase'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sale_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cashbox_sale', to='Market.saleorder', verbose_name='SaleOrder'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sale_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cashbox_sale', to='Market.saleproduct', verbose_name='SaleProduct'),
        ),
        migrations.AddField(
            model_name='saleproduct',
            name='cashbox',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cashbox_sale_product', to='Market.cashbox', verbose_name='Cashbox'),
        ),
        migrations.AddField(
            model_name='saleproduct',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_card_sale_product', to='Clients.clientcard', verbose_name='ClientCard'),
        ),
        migrations.AddField(
            model_name='saleproduct',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_sale_product', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='saleproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_sale_product', to='Market.product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='saleproduct',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service_sale_product', to='Organizations.service', verbose_name='Service'),
        ),
        migrations.AddField(
            model_name='saleorder',
            name='cashbox',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cashbox_sale_order', to='Market.cashbox', verbose_name='Cashbox'),
        ),
        migrations.AddField(
            model_name='saleorder',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='client_card_sale_order', to='Clients.clientcard', verbose_name='ClientCard'),
        ),
        migrations.AddField(
            model_name='saleorder',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_sale_order', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='saleorder',
            name='product_order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_sale_order', to='Market.productorder', verbose_name='ProductOrder'),
        ),
        migrations.AddField(
            model_name='saleorder',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service_sale_order', to='Organizations.service', verbose_name='Service'),
        ),
        migrations.AddField(
            model_name='purchaserequest',
            name='cashbox',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cashbox_purchase', to='Market.cashbox', verbose_name='Cashbox'),
        ),
        migrations.AddField(
            model_name='purchaserequest',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_purchase', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='purchaserequest',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='product_purchase', to='Market.product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='purchaserequest',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service_purchase', to='Organizations.service', verbose_name='Service'),
        ),
        migrations.AddField(
            model_name='purchaseaccept',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_purchase_accept', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='purchaseaccept',
            name='purchase_request',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='purchase_purchase_accept', to='Market.purchaserequest', verbose_name='PurchaseRequest'),
        ),
        migrations.AddField(
            model_name='productorder',
            name='order',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='order_product_order', to='Orders.order', verbose_name='Order'),
        ),
        migrations.AddField(
            model_name='productorder',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_product_done', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='productorder',
            name='products',
            field=models.ManyToManyField(related_name='product_product_order', to='Market.Product', verbose_name='Product'),
        ),
        migrations.AddField(
            model_name='productorder',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service_product_order', to='Organizations.service', verbose_name='Service'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_product', to='Market.productcategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_product', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='product',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service_product', to='Organizations.service', verbose_name='Service'),
        ),
        migrations.AddField(
            model_name='cashbox',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization_cashbox', to='Organizations.organization', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='cashbox',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service_cashbox', to='Organizations.service', verbose_name='Service'),
        ),
    ]
