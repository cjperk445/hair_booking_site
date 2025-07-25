from django.shortcuts import render
from .models import User

# Create your views here.


def index(request):
    return render(request, 'index.html')


def stylists(request):
    return render(request, 'stylists.html')

def profile_page(request, pk):
    user = User.objects.get(id=pk)
    context = {'user': user}
    return render(request, 'profile.html', context)