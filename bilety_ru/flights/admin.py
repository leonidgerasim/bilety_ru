from django.contrib import admin
from .models import FlightOffers, FlightRequest

# Register your models here.

admin.site.register(FlightOffers)
admin.site.register(FlightRequest)
