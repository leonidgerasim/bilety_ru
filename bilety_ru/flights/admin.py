from django.contrib import admin
from .models import FlightOffer, FlightRequest

# Register your models here.

admin.site.register(FlightOffer)
admin.site.register(FlightRequest)
