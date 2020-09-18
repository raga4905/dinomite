from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('dinos/', views.dinos_index, name='index'),
    path('dinos/<int:dino_id>/', views.dinos_detail, name='detail'),
    path('dinos/create/', views.DinoCreate.as_view(), name='dinos_create'),
    path('dinos/<int:pk>/update/', views.DinoUpdate.as_view(), name='dinos_update'), 
    path('dinos/<int:pk>/delete/', views.DinoDelete.as_view(), name='dinos_delete'),
    path('dinos/<int:dino_id>/add_sighting/', views.add_sighting, name='add_sighting'),
    path('dinos/<int:dino_id>/assoc_pet/<int:pet_id>/', views.assoc_pet, name='assoc_pet'),
    path('pets/', views.PetList.as_view(), name='pets_index'),
    path('pets/<int:pk>/', views.PetDetail.as_view(), name='pets_detail'),
    path('pets/create/', views.PetCreate.as_view(), name='pets_create'),
    path('pets/<int:pk>/update/', views.PetUpdate.as_view(), name='pets_update'),
    path('pets/<int:pk>/delete/', views.PetDelete.as_view(), name='pets_delete'),
]
