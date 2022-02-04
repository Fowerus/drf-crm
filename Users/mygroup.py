from django.contrib.auth.models import GroupManager, Permission
from django.db import models



class MyGroup(models.Model):

    name = models.CharField('name', max_length=150)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name='permissions',
        related_name="mygroup_permissions",
        blank=True,
    )
    organization = models.ForeignKey(
        'Organizations.Organization', on_delete=models.CASCADE, related_name='mygroup_organizations')
    service = models.ForeignKey(
        'Organizations.Service', blank=True, on_delete=models.CASCADE,  null=True, related_name='mygroup_services')

    objects = GroupManager()

    class Meta:
        unique_together = ('name', 'organization', 'service')
        db_table = 'group'
        verbose_name = 'group'
        verbose_name_plural = 'groups'
        permissions = [('change_user_group', 'Can change user group')]

    def __str__(self):
        return f'id: {self.id} | name {self.name} | {self.organization} | service {self.service}'

    def save(self, *args, **kwargs):
        if self.service == None:
            if self.__class__.objects.filter(~models.Q(id=self.id)).filter(name=self.name, organization=self.organization, service=None):
                raise setError(
                    f'The fields name, organization, service must make a unique set.', 400)

        self.name += f'_{self.organization.id}_{self.service.id}' if self.service else f'_{self.organization.id}'
        
        super().save(*args, **kwargs)

    def natural_key(self):
        return (self.name,)
    