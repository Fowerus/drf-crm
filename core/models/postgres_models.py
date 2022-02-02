from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    comment = models.TextField(null=True, blank=True, default=None)

    def __str__(self):
        return self.title
