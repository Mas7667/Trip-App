from django.db import models
from .evenement import EvenementSportif

class Voyage(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_depart = models.DateField()
    duree = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    places_disponibles = models.PositiveIntegerField()
    evenements = models.ManyToManyField(EvenementSportif, related_name='voyages')

    def __str__(self):
        return self.titre