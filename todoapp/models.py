
from functools import cached_property
from logging import PlaceHolder
from django.db import models;
from django.contrib.auth.models import User;

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True);
    title = models.CharField(max_length=50,null=False,blank=False);
    description =models.TextField(null=False,blank=False);
    complete = models.BooleanField(default=False);
    create = models.DateTimeField(auto_now_add=True);

    def __str__(self):
        return self.title;

    class Meta:
        ordering =['complete'];
