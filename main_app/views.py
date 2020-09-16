from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Dino


def home(request):
    return HttpResponse('<h1>Dinos are cool</h1>')


def about(request):
    return render(request, 'about.html')

def dinos_index(request):
    dinos = Dino.objects.all()
    return render(request, 'dinos/index.html', {'dinos': dinos})

def dinos_detail(request, dino_id):
    dino = Dino.objects.get(id=dino_id)
    return render(request, 'dinos/detail.html', {'dino': dino })