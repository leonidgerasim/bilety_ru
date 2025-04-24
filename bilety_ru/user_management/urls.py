from django.urls import path, include
from .views import index, SignView

app_name = 'user_management'

urlpatterns = [
    path('f/', index, name='index'),
    path('', SignView.as_view(), name='signup'),
]
