from django.shortcuts import render
from .forms import OfferSearchForm
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, HttpResponse
from .models import FlightOffers
from django.views.generic.edit import CreateView, View, FormView
# from rest_framework.views import APIView, status
# from rest_framework.response import Response
from django.contrib import messages
import amadeus
from django.http import JsonResponse
import datetime
from .flight import Flight


c = amadeus.Client(client_id='1otgEUauKpjxxGPcPxSQvvsRz7o3fxv1',
                   client_secret='VgqvL5c92wzXcPgV')


class OffersSearch(FormView):
    template_name = 'flights/search.html'
    form_class = OfferSearchForm
    success_url = ''

    def form_valid(self, form):
        func = lambda date: date if date is not None else None
        form_data = {
            'currencyCode': form.cleaned_data['currencyCode'],
            'originCity': self.request.POST['originCity'],
            'destinationCity': self.request.POST['destinationCity'],
            'departureDate': (form.cleaned_data['departureDate'].year,
                              form.cleaned_data['departureDate'].month,
                              form.cleaned_data['departureDate'].day),
            'adults': form.cleaned_data['adults'],
        }
        if 'returnDate' in form.cleaned_data:
            form_data['returnDate'] = (form.cleaned_data['returnDate'].year,
                                       form.cleaned_data['returnDate'].month,
                                       form.cleaned_data['returnDate'].day)
        self.request.session['form_data'] = form_data
        return HttpResponseRedirect(reverse('flights:home'))

    def form_invalid(self, form):
        return HttpResponse('Ошибка')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form_data' in self.request.session:
            form_data = self.request.session['form_data']
            kwargs = {
                'currencyCode': form_data['currencyCode'],
                'originLocationCode': form_data['originCity'][0:3],
                'destinationLocationCode': form_data['destinationCity'][0:3],
                'departureDate': datetime.date(int(form_data['departureDate'][0]),
                                               int(form_data['departureDate'][1]),
                                               int(form_data['departureDate'][2])),
                'adults': int(form_data['adults']),
                'max': 3,
            }
            if form_data['returnDate']:
                kwargs['returnDate'] = datetime.date(int(form_data['returnDate'][0]),
                                                int(form_data['returnDate'][1]),
                                                int(form_data['returnDate'][2])),
            context['form'] = OfferSearchForm(initial=f)
            context['form_data'] = f
            #context['response'] = offer_search_api(self.request, **kwargs)
        return context


def get_cities(request):
    query = request.GET.get("query", None)  # Получаем введённый текст
    try:
        data = c.reference_data.locations.get(keyword=query, subType=amadeus.Location.ANY).data
    except amadeus.ResponseError as error:
        messages.add_message(request, messages.ERROR, error)
    data = c.reference_data.locations.get(keyword=query, subType=amadeus.Location.ANY).data
    result = []
    for i, val in enumerate(data):
        result.append(data[i]['iataCode']+', '+data[i]['name'])
    return JsonResponse(result, safe=False)


def offer_search_api(request, **kwargs):
    try:
        search_flights = c.shopping.flight_offers_search.get(**kwargs)
    except amadeus.ResponseError as error:
        messages.add_message(
            request, messages.ERROR, error.response.result["errors"][0]["detail"]
        )
    search_flights_returned = []
    search_flights = c.shopping.flight_offers_search.get(**kwargs)
    response = ""
    for flight in search_flights.data:
        offer = Flight(flight).construct_flights()
        search_flights_returned.append(offer)
        response = zip(search_flights_returned, search_flights.data)

    return response

