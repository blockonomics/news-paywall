from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from .forms import UserLoginForm, UserRegistrationForm


class LoginView(auth_views.LoginView):
    form_class = UserLoginForm
    redirect_authenticated_user = True
    template_name = 'auth/login_page.html'


class SignUpView(generic.CreateView):
    form_class = UserRegistrationForm
    template_name = 'auth/signup_page.html'
    success_url = reverse_lazy('authentication:login')

