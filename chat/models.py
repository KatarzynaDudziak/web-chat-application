from django.db import models
from django.contrib.auth.models import User


class MessageModel(models.Model):
    content = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
