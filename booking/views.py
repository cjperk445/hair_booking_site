from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_booking_system(request):
    return HttpResponse("This is the booking app")
