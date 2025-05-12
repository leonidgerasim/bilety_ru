from django import forms
from .models import FlightRequest


# class OfferSearchForm(forms.ModelForm):
#     class Meta:
#         model = FlightRequest
#         fields = ('currencyCode', 'originLC', 'destinationLC', 'departureDate', 'returnDate', 'adults')


class OfferSearchForm(forms.Form):
    CURRENCY_CODES = [('EUR', '€'), ('RUB', '₽'), ('USD', '$')]

    currencyCode = forms.ChoiceField(choices=CURRENCY_CODES, label='Валюта', initial='EUR', widget=forms.Select())
    originCity = forms.CharField(max_length=100)
    # originLC = forms.ChoiceField(choices=[], label='Выбирете аэропорт отправления')
    destinationCity = forms.CharField(max_length=100)
    # destinationLC = forms.ChoiceField(choices=[], label='Выбирете аэропорт прибытия')
    departureDate = forms.DateField(label='Дата отправления', widget=forms.SelectDateWidget())
    returnDate = forms.DateField(label='Дата возвращения', widget=forms.SelectDateWidget(), required=False)
    adults = forms.IntegerField(label='Количество взрослых пассажиров')

