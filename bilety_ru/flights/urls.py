from django.urls import path, include
from .views import OffersSearch, get_cities

app_name = 'flights'

urlpatterns = [
    path('', OffersSearch.as_view(), name='home'),
    path('api_airport_search/', get_cities, name='api_airport_search'),
]