from django import forms
from .models import FlightRequest


class OfferSearchForm(forms.ModelForm):
    class Meta:
        model = FlightRequest
        fields = ('currencyCode', 'originLC', 'destinationLC', 'departureDate', 'returnDate', 'adults')
