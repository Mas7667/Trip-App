from django.db import models
from django.contrib.auth.models import User

class Voyage(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    date_depart = models.DateField()
    duree = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    places_disponibles = models.PositiveIntegerField()
    evenements = models.ManyToManyField("EvenementSportif", related_name="voyages_evenements", blank=True)
    def __str__(self):
        return self.titre

class EvenementSportif(models.Model):
    SPORTS = [
        ('hockey', 'Hockey'),
        ('football', 'Football'),
        ('soccer', 'Soccer'),
        ('baseball', 'Baseball'),
        ('basketball', 'Basketball'),
    ]

    nom = models.CharField(max_length=100)
    sport = models.CharField(max_length=20, choices=SPORTS)
    description = models.TextField()
    date = models.DateField()
    lieu = models.CharField(max_length=100)
    ligue = models.CharField(max_length=50)
    voyages = models.ManyToManyField(Voyage, related_name="evenments_voyages", blank=True)

    def __str__(self):
        return f"{self.nom} - {self.ligue}"

class Reservation(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    nb_personnes = models.PositiveIntegerField()
    date_reservation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} → {self.voyage.titre}"
