import os

from django.shortcuts import render
from django.views.generic.base import View


class RegisterView(View):
    def get(self, request):
        return render(request, os.path.join('jobs', 'account', 'register.html'), {})


class LoginView(View):
    def get(self, request):
        return render(request, os.path.join('jobs', 'account', 'login.html'), {})