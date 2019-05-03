from django.shortcuts import render

from .models import Resume


def resume_home(request):
    resume_list = Resume.objects
    return render(request, 'resume/index.html', {'resume_object': resume_list})
