from django.db import models
from django.contrib.auth import get_user_model
from Organizations.models import Organization



class Client(models.Model):
	user = models.OneToOneField(get_user_model(), on_delete = models.CASCADE, related_name = 'user_client', verbose_name = 'Client')
	organization = models.ForeignKey(Organization, on_delete = models.CASCADE, related_name = 'user_client', verbose_name = 'Organization')

	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')
	updated_at = models.DateTimeField(auto_now = True, verbose_name = 'Updated_at')


	def __str__(self):
		return f"user: {self.user} | organization: {self.organization}"


	class Meta:
		db_table = 'Client'
		verbose_name_plural = 'Clients'
		verbose_name = 'Client'
		ordering = ['-updated_at']