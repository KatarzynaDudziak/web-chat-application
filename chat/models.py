from email import message
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


class MessageModel(models.Model):
    content = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='messagemodel_likes')
    
    def num_of_likes(self):
        return self.likes.count()
