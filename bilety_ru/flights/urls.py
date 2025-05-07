from django.urls import path, include
from .views import index, OffersSearch

app_name = 'flights'

urlpatterns = [
    path('', OffersSearch.as_view(), name='home'),
]