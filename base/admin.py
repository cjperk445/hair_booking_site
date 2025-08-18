from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Service, Booking


admin.site.register(User)
admin.site.register(Service)
admin.site.register(Booking)