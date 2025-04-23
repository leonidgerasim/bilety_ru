from django.contrib import admin
from django.urls import path, include
from .views import index, SignUpView

app_name = 'user_management'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    #path('', )
]
