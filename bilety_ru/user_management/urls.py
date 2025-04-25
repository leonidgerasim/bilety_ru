from django.urls import path, include
from .views import index, SignUpView, SignInView, LogOutView

app_name = 'user_management'

urlpatterns = [
    path('f/', index, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', SignInView.as_view(), name='signin'),
    path('logout/', LogOutView.as_view(), name='logout'),
]
