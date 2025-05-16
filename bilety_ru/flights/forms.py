from django import forms
from .models import FlightRequest


class OfferSearchForm(forms.ModelForm):
    CURRENCY_CODES = [('EUR', '€'), ('RUB', '₽'), ('USD', '$')]

    currencyCode = forms.ChoiceField(choices=CURRENCY_CODES, initial='EUR', label='Валюта')
    # returnDate = forms.DateField(required=False)

    class Meta:
        model = FlightRequest
        fields = ('currencyCode',
                  'originLocationCode',
                  'destinationLocationCode',
                  'departureDate',
                  'returnDate',
                  'adults')
        labels = {
            'currencyCode': "Валюта",
            'originLocationCode': 'Аэропорт отправления',
            'destinationLocationCode': 'Аэропорт прибытия',
            'departureDate': 'Дата отправления',
            'returnDate': 'Дата возвращения',
            'adults': 'Число взрослых пассажиров',
        }
        widgets = {
            #'currencyCode': forms.Select(),
            'departureDate': forms.SelectDateWidget(),
            'returnDate': forms.SelectDateWidget(),
        }


# class OfferSearchForm(forms.Form):
#     CURRENCY_CODES = [('EUR', '€'), ('RUB', '₽'), ('USD', '$')]
#
#     currencyCode = forms.ChoiceField(choices=CURRENCY_CODES, label='Валюта', initial='EUR', widget=forms.Select())
#     originLocationCode = forms.CharField(max_length=100)
#     # originLC = forms.ChoiceField(choices=[], label='Выбирете аэропорт отправления')
#     destinationLocationCode = forms.CharField(max_length=100)
#     # destinationLC = forms.ChoiceField(choices=[], label='Выбирете аэропорт прибытия')
#     departureDate = forms.DateField(label='Дата отправления', widget=forms.SelectDateWidget())
#     returnDate = forms.DateField(label='Дата возвращения', widget=forms.SelectDateWidget(), required=False)
#     adults = forms.IntegerField(label='Количество взрослых пассажиров')

