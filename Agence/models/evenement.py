from django.db import models
from .voyage import Voyage  # ou "from agence.models.voyage import Voyage"

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

    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE, related_name="evenements", null=True)

    def __str__(self):
        return f"{self.nom} ({self.sport}) - {self.ligue}"
