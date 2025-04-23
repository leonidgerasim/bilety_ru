from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic.edit import CreateView, View
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


class SignUpView(View):

    def get(self, request):
        if request.method == 'POST':
            form = SignUpForm(data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('first_name') + ' ' + form.cleaned_data.get('last_name')
                password = form.cleaned_data.get('password1')
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                email = form.cleaned_data.get('email')
                user = User(username=username, password=password, first_name=first_name,
                            last_name=last_name, email=email)
                user.save()
                login(request, user)
                messages.success(request, ("Вы успешно зарегистрированы."))
                return redirect('') #reverse('user_management:signup'))
            else:
                messages.success(request, ("Что то пошло не так, поробуйте ещё раз"))
                return HttpResponseRedirect(reverse('user_management:signup'))
        else:
            form = SignUpForm()
            context = {'title': 'Страница регистрации',
                       'form': form,
                       }
            return render(request, 'user_management/signup.html', context)



#class AuthView()


def index(request):
    return render(request, 'user_management/auth.html')



