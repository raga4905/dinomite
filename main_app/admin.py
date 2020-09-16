from django.contrib import admin

from .models import Dino, Sighting

# Register your models here.
admin.site.register(Dino)
admin.site.register(Sighting)