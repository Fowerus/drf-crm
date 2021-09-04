from django.db import models
from django.contrib.auth import get_user_model

from Organizations.models import MainMixin, Service
from Clients.models import Client




class Order(MainMixin):
	order_code = models.BigIntegerField(unique = True, verbose_name = 'Order_code')
	description = models.CharField(max_length = 500, verbose_name = 'Description')
	client = models.ForeignKey(Client, on_delete = models.SET_NULL, null = True, related_name = 'client_orders', verbose_name = 'Client')
	executor = models.ForeignKey(get_user_model(), on_delete = models.SET_NULL, null = True, related_name = 'user_executor', verbose_name = 'Executor')
	creator = models.ForeignKey(get_user_model(), on_delete = models.SET_NULL, null = True, related_name = 'user_creator', verbose_name = 'Creator')

	service = models.ForeignKey(Service, on_delete = models.SET_NULL, null = True, related_name = 'service_orders', verbose_name = 'Service')

	done = models.BooleanField(default = False)


	class Meta:
		db_table = 'Order'
		verbose_name_plural = "Orders"
		verbose_name = "Order"
		ordering = ['-updated_at']