from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    #profilepic = models.ImageField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

#class Service(models.Model):
    #name = models.CharField(max_length=200)
    #description = 

    # def __str__(self)
    #     return self.name
