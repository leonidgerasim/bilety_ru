from django.shortcuts import render
import amadeus
from django.http import JsonResponse

# Create your views here.

c = amadeus.Client(client_id='1otgEUauKpjxxGPcPxSQvvsRz7o3fxv1',
                   client_secret='VgqvL5c92wzXcPgV')

def get_cities(request):
    query = request.GET.get("query", None)  # Получаем введённый текст
    data = c.reference_data.locations.get(keyword=query, subType=amadeus.Location.ANY).data
    result = []
    for i, val in enumerate(data):
        result.append(data[i]['iataCode']+', '+data[i]['name'])
    return JsonResponse(result, safe=False)


def offer_search_api(request, **kwargs):

    search_flights_returned = []
    search_flights = c.shopping.flight_offers_search.get(**kwargs)
    response = ""
    for flight in search_flights.data:
        # offer = Flight(flight).construct_flights()
        search_flights_returned.append(offer)
        response = zip(search_flights_returned, search_flights.data)
    return response

