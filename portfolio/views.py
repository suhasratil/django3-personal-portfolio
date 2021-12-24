from django.shortcuts import render
from .models import Project

# Create your views here.
def home(requests):
    projects=Project.objects.all()
    return render(requests, 'home.html', {'projects' : projects})