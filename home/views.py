from django.shortcuts import render

from .models import Home


def home(request):
    jobs = Home.objects
    return render(request, 'home/index.html', {'home': jobs})
