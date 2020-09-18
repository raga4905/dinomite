from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Dino, Pet
from .forms import SightingForm


class DinoCreate(CreateView):
    model = Dino
    fields = ['name', 'fun_pun', 'description']


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

def assoc_pet(request, dino_id, pet_id):
  Dino.objects.get(id=dino_id).pets.add(pet_id)
  return redirect('detail', dino_id=dino_id)


def dinos_detail(request, dino_id):
  dino = Dino.objects.get(id=dino_id)
  pets_dino_doesnt_have = Pet.objects.exclude(id__in = dino.pets.all().values_list('id'))
  sighting_form = SightingForm()
  return render(request, 'dinos/detail.html', {
      'dino': dino, 'sighting_form': sighting_form, 'pets': pets_dino_doesnt_have
  })


def add_sighting(request, dino_id):
  form = SightingForm(request.POST)
  if form.is_valid():
    new_sighting = form.save(commit=False)
    new_sighting.dino_id = dino_id
    new_sighting.save()
  return redirect('detail', dino_id=dino_id)


class PetList(ListView):
  model = Pet


class PetDetail(DetailView):
  model = Pet


class PetCreate(CreateView):
  model = Pet
  fields = '__all__'


class PetUpdate(UpdateView):
  model = Pet
  fields = ['name']


class PetDelete(DeleteView):
  model = Pet
  success_url = '/pets/'
