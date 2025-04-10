from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView

# Create your views here.


class AuthView:
    pass


def index(request):
    return render(request, 'main/auth.html')
