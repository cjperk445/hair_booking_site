from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    
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


class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    stylist = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="customer_bookings")
    date = models.DateField()
    time = models.TimeField()
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer.first_name} {self.customer.last_name} booking with {self.stylist.first_name} {self.stylist.last_name}"
