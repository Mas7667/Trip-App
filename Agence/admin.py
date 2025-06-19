from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Voyage, EvenementSportif, Reservation

admin.site.register(Voyage)
admin.site.register(EvenementSportif)
admin.site.register(Reservation)
