from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)

    #profilepic = models.ImageField

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []