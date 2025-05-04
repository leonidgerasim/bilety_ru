from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView, View, FormView
from django.contrib.auth.models import User
from .forms import SignUpForm, SignInForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


class SignUpView(FormView):
    template_name = 'user_management/signup.html'
    form_class = SignUpForm
    success_url = 'user_management/signup'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        request = self.request
        f = form.save(commit=False)
        username = form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')
        f.username = username
        f.save()
        user = authenticate(username=username,
                            password=form.cleaned_data.get('password1'))
        login(request, user)
        return HttpResponseRedirect(reverse('user_management:index'))

    def form_invalid(self, form):
        return super().form_invalid(form)


class SignInView(FormView):
    template_name = 'user_management/auth.html'
    form_class = SignInForm
    success_url = 'user_management/'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['first_name'] + ' ' + form.cleaned_data['last_name']
        user = authenticate(username=username,
                            password=form.cleaned_data.get('password'))
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(reverse('user_management:index'))
        else:
            return HttpResponse('user')

    def form_invalid(self, form):
        return redirect('/')


class LogOutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('user_management:index'))


def index(request):
    context = {'users': User.objects.all(),
               'user': request.user}
    return render(request, 'user_management/auth.html', context)



