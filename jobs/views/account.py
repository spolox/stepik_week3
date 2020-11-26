import os

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView

from jobs.forms.account import UserLoginForm


class MyRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = os.path.join('jobs', 'account', 'register.html')
    success_url = 'login'


class MyLoginView(LoginView):
    form_class = UserLoginForm
    redirect_authenticated_user = True
    template_name = os.path.join('jobs', 'account', 'login.html')
