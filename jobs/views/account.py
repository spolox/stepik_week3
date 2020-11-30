import os

from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, View


from jobs.forms.account import UserLoginForm, UserRegisterForm


class MyRegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegisterForm
    template_name = os.path.join('jobs', 'account', 'register.html')
    success_url = 'login'
    success_message = 'Вы успешно зарегистировались!'


class MyLoginView(LoginView):
    form_class = UserLoginForm
    redirect_authenticated_user = True
    template_name = os.path.join('jobs', 'account', 'login.html')


class MyProfileView(View):
    def get(self, request):
        return redirect(reverse('login'))
