from django import forms
from . models import Reservation

# we will make forms from the reservation model
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation # choose a model
        fields = "__all__" # use all fields