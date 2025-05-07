from django.shortcuts import render
from .forms import OfferSearchForm
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, HttpResponse
from .models import FlightOffers

# Create your views here.

from django.views.generic.edit import CreateView, View, FormView

class OffersSearch(FormView):
    template_name = 'flights/search.html'
    form_class = OfferSearchForm
    success_url = ''

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('flights:home'))

    def form_invalid(self, form):
        return HttpResponse('Ошибка')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['test_data'] = self.request.POST
        context['requests'] = FlightOffers.objects.all()
        return context


def index(request):
    return render(request, 'flights/search.html')
