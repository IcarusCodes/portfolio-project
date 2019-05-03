from django.shortcuts import render

from .models import Ctfs


def all_ctfs(request):
    ctfs = Ctfs.objects
    return render(request, 'ctfs/index.html', {'ctfs': ctfs})
