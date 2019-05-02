from django.urls import path

from ctfs import views

urlpatterns = [
    path('', views.all_ctfs, name='ctfs'),
]
