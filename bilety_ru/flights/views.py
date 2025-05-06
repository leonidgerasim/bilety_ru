from django.shortcuts import render

# Create your views here.

from django.views.generic.edit import CreateView, View, FormView

#class OffersSearch(FormView):

def index(request):
    return render(request, 'flights/search.html')
