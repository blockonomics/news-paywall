import django.contrib.auth.views
from django.urls import path
from . import views
from .views import SignUpView, LoginView

app_name = 'authentication'

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('login', LoginView.as_view(), name='login'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('logout', django.contrib.auth.views.LogoutView.as_view(), name='logout'),
]
