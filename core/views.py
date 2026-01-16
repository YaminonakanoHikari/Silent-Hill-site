from django.shortcuts import render
from .models import Artifact 

def index(request):
    artifacts = Artifact.objects.all() 
    return render(request, 'core/index.html', {'artifacts': artifacts})