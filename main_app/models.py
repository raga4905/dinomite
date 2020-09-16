from django.db import models

# Create your models here.

class Dino(models.Model):
    name = models.CharField(max_length=100)
    fun_pun = models.TextField(max_length=350)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name


# class Dino:
#     def __init__(self, name, fun_pun, description):
#         self.name = name
#         self.fun_pun = fun_pun
#         self.description = description


# dinos = [
#     Dino('Pterodactyl', 'What is the scariest type of dinosaur? A Terror-dactyl.',
#          'winged lizard, pointy head'),
#     Dino('Tyrannosaurus', 'What do you call it when a dinossaur has a car accident? A tyrannosaurus wreck!',
#          'Big head, little arms')
# ]
