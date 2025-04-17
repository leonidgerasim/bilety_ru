from django.contrib import admin
from django.urls import path, include
from .views import register

app_name = 'auth_management'

urlpatterns = [
    path('auth',),
    path('registration', )
]
