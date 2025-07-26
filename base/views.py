from django.shortcuts import render
from django.views import generic
from .models import User
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, 'index.html',)


def profile_page(request, pk):
    user = User.objects.get(username__iexact=pk)
    context = {'user': user}
    return render(request, 'profile.html', context)


class UserList(generic.ListView):
    model = User
