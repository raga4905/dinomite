from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dino
from .forms import SightingForm


class DinoCreate(CreateView):
    model = Dino
    fields = '__all__'


class DinoUpdate(UpdateView):
    model = Dino
    fields = ['name', 'description']


class DinoDelete(DeleteView):
    model = Dino
    success_url = '/dinos/'


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def dinos_index(request):
  dinos = Dino.objects.all()
  return render(request, 'dinos/index.html', {'dinos': dinos})


def dinos_detail(request, dino_id):
  dino = Dino.objects.get(id=dino_id)
  # instantiate FeedingForm to be rendered in the template
  sighting_form = SightingForm()
  return render(request, 'dinos/detail.html', {
      # pass the cat and feeding_form as context
      'dino': dino, 'sighting_form': sighting_form
  })


def add_sighting(request, dino_id):
  form = SightingForm(request.POST)
  if form.is_valid():
    new_sighting = form.save(commit=False)
    new_sighting.dino_id = dino_id
    new_sighting.save()
  return redirect('detail', dino_id=dino_id)
