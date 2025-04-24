from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView, View, FormView
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


class SignView(FormView):
    template_name = 'user_management/signup.html'
    form_class = SignUpForm
    #success_url = reverse('user_management:signup')

    def form_valid(self, form):
        request = self.request
        if request.user.is_authenticated:
            messages.success(request, ("Вы не успешно зарегистрированы."))
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            f = form.save(commit=False)
            f.username = form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')
            f.save()
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password'))
            login(request, user)
            messages.success(request, ("Вы успешно зарегистрированы."))
            return redirect('/')


#class AuthView()


def index(request):
    return render(request, 'user_management/auth.html')



