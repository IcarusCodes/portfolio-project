from django.shortcuts import render

from .models import Project


def project(request):
    project = Project.objects
    return render(request, 'projects/index.html', {'project_object': project})
