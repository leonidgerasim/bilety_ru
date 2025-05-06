from django.contrib import admin
from django.urls import path, include
from .views import index

app_name = 'flights'

urlpatterns = [
    path('', index, name='index'),
]