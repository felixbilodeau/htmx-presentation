from uuid import uuid4

from django.db import models


class Post(models.Model):
    id = models.UUIDField('ID', primary_key=True, default=uuid4)
    created = models.DateTimeField('Created', auto_now_add=True)
    content = models.CharField('Content', max_length=255)
    edited = models.BooleanField('Edited', default=False)
