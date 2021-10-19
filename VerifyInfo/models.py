import uuid

from django.db import models
from Users.models import User 
from Clients.models import Client



class VerifyInfoUser(models.Model):
	choices_code = (
		(0, 'phone'),
		(1, 'email'),
		(2, 'reset')
	)

	user = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = 'User')
	code = models.IntegerField(unique = True)
	type_code = models.CharField(max_length = 10, choices = choices_code, verbose_name = 'Type_code')

	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')


	def __str__(self):
		return f'user: {self.user} | code: {self.code} | type_code: {self.type_code}'


	@property
	def raw_code(self):
		return self._code()


	def _code(self):
		self.code = int(str(uuid.uuid1().int)[:6])
		return self.code


	class Meta:
		unique_together = ('user', 'type_code')
		db_table = 'VerifyInfoUser'
		verbose_name_plural = 'VerifyInfoUsers'
		verbose_name = 'VerifyInfoUser'
		ordering = ['-created_at']



class VerifyInfoClient(models.Model):

	client = models.OneToOneField(Client, on_delete = models.CASCADE, verbose_name = 'Client')
	code = models.IntegerField(unique = True)

	created_at = models.DateTimeField(auto_now_add = True, verbose_name = 'Created_at')


	def __str__(self):
		return f'user: {self.client} | code: {self.code}'


	@property
	def raw_code(self):
		return self._code()


	def _code(self):
		self.code = int(str(uuid.uuid1().int)[:6])
		return self.code


	class Meta:
		db_table = 'VerifyInfoClient'
		verbose_name_plural = 'VerifyInfoClient'
		verbose_name = 'VerifyInfoClient'
		ordering = ['-created_at']
		