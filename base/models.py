from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    
    # profilepic = models.ImageField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Service(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    servicelength = models.DurationField(help_text="Duration in HH:MM:SS")
    is_available = models.BooleanField(default=True)
    # link this model to user model (stylist) - ManyToMany as
    # multiple stylists can offer the same thing
    stylist = models.ManyToManyField(
        User, related_name='services')
    
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.name} - £{self.price}"
