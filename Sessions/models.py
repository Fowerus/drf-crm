from django.db import models
from django.contrib.auth import get_user_model

from Clients.models import Client



class Session_user(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name = 'user_sessions', verbose_name = 'User')
	device = models.CharField(max_length = 150, verbose_name = 'Device')

	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')


	def __str__(self):
		return f'user: {self.user} | device: {self.device}'


	class Meta:
		unique_together = ('user', 'device')
		db_table = 'Session_user'
		verbose_name_plural = 'Sessions users'
		verbose_name = 'Session user'
		ordering = ['-updated_at']



class Session_client(models.Model):
	client = models.ForeignKey(Client, on_delete = models.CASCADE, related_name = 'client_sessions', verbose_name = 'Client')
	device = models.CharField(max_length = 150, verbose_name = 'Device')

	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')


	def __str__(self):
		return f'user: {self.client} | device: {self.device}'


	class Meta:
		unique_together = ('client', 'device')
		db_table = 'Session_client'
		verbose_name_plural = 'Sessions clients'
		verbose_name = 'Session client'
		ordering = ['-updated_at']
		