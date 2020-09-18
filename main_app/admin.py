from django.contrib import admin

from .models import Dino, Sighting, Pet

# Register your models here.
admin.site.register(Dino)
admin.site.register(Sighting)
admin.site.register(Pet)