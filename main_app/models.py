from django.db import models
from django.urls import reverse
from datetime import date


# Create your models here.
LOCATIONS = (
    ('H', 'Horizon'), 
    ('B', 'Backyard'), 
    ('P', 'From a Plane')
)


class Pet(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('pets_detail', kwargs={'pk': self.id})

class Dino(models.Model):
    name = models.CharField(max_length=100)
    fun_pun = models.TextField(max_length=350)
    description = models.TextField(max_length=250)
    pets = models.ManyToManyField(Pet)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'dino_id': self.id})

    def seen_recently(self):
        return self.sighting_set.filter(date=date.today()).count() >= len(LOCATIONS)

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

    class Meta:
        ordering = ['-date']
