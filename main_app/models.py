from django.db import models
from django.urls import reverse

# Create your models here.
LOCATIONS = (
    ('H', 'Horizon'), 
    ('B', 'Backyard'), 
    ('P', 'From a Plane')
)

class Dino(models.Model):
    name = models.CharField(max_length=100)
    fun_pun = models.TextField(max_length=350)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dino_id': self.id})

class Sighting(models.Model):
    date = models.DateField('sighting date')
    location = models.CharField(
        max_length=1,
        choices=LOCATIONS, 
        default=LOCATIONS[0][0]
    )

    dino = models.ForeignKey(Dino, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_location_display()} on {self.date}"