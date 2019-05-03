from django.shortcuts import render

from .models import Home


def home(request):
    homeobjects = Home.objects
    return render(request, 'home/index.html', {'homeobjects': homeobjects})
