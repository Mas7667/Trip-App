from django import forms
from .models import Reservation, Voyage, EvenementSportif


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['voyage', 'nb_personnes']

class VoyageForm(forms.ModelForm):
    class Meta:
        model = Voyage
        fields = ['titre', 'description', 'date_depart', 'duree', 'prix', 'places_disponibles', 'evenements']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom du voyage'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date_depart': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'duree': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de jours'}),
            'prix': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': 'Prix en $'}),
            'places_disponibles': forms.NumberInput(attrs={'class': 'form-control'}),
            'evenements': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

class EvenementSportifForm(forms.ModelForm):
    class Meta:
        model = EvenementSportif
        fields = ['nom', 'sport', 'description', 'date', 'lieu', 'ligue', 'voyages']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'sport': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'lieu': forms.TextInput(attrs={'class': 'form-control'}),
            'ligue': forms.TextInput(attrs={'class': 'form-control'}),
            'voyages': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }