from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class FlightRequest(models.Model):
    currencyCode = models.CharField(max_length=3)
    originLC = models.CharField(max_length=3)
    destinationLC = models.CharField(max_length=3)
    departureDate = models.DateField()
    departureTime = models.TimeField(default=datetime.time(10, 10, 10))
    returnDate = models.DateField(null=True, blank=True)
    adults = models.IntegerField()
    children = models.IntegerField(null=True, blank=True)
    infants = models.IntegerField(null=True, blank=True)
    cabin = models.CharField(max_length=20, null=True, blank=True)
    includedAirlines = models.CharField(max_length=200, null=True, blank=True)
    excludedAirlines = models.CharField(max_length=200, null=True, blank=True)
    travalClass = models.CharField(max_length=50, null=True, blank=True)
    nonStop = models.BooleanField(default=False)
    maxPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)


class FlightOffers(models.Model):
    flightRequest = models.ForeignKey(FlightRequest, on_delete=models.CASCADE)
    #instantTicketingRequired = models.BooleanField()
    #nonHomogeneous = models.BooleanField()
    #oneWay = models.BooleanField()
    #lastTicketingDate = models.DateField()
    numberSeats = models.IntegerField()
    dep_duration = models.TimeField()
    arr_duration = models.TimeField(default=None)
    currencyCode = models.CharField(max_length=3)
    totalPrice = models.DecimalField(max_digits=10, decimal_places=2)


class FlightSegments(models.Model):
    offer = models.ForeignKey(FlightOffers, on_delete=models.CASCADE)
    there_seg = models.BooleanField()
    dep_iataCode = models.CharField(max_length=3)
    dep_terminal = models.CharField(max_length=2)
    dep_dateTime = models.DateTimeField()
    arr_iataCode = models.CharField(max_length=3)
    arr_terminal = models.CharField(max_length=2)
    arr_dateTime = models.DateTimeField()
    carrierCode = models.CharField(max_length=2)
    number = models.CharField(max_length=4)
    aircraftCode = models.CharField(max_length=4)
    operating = models.CharField(max_length=2)
    duration = models.TimeField()
    id_seg = models.CharField(max_length=2)


