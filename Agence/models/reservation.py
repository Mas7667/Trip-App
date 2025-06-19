from django.db import models
from django.contrib.auth.models import User
from .voyage import Voyage

class Reservation(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    nb_personnes = models.PositiveIntegerField()
    date_reservation = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.username} – {self.voyage.titre} ({self.nb_personnes} pers.)"
