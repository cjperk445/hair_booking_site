from django.shortcuts import render
from .models import User
from datetime import datetime

# Create your views here.


def index(request):

    # Current year for copyright
    # today = datetime.now()
    # this_year = today.year

    return render(request, 'index.html', {
        # "year": year,
        # "this_year": this_year,
    })


def stylists(request):
    return render(request, 'stylists.html')


def profile_page(request, pk):
    user = User.objects.get(username=pk)
    context = {'user': user}
    return render(request, 'profile.html', context)
