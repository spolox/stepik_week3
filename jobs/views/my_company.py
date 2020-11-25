import os

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from jobs.models import Vacancy, Specialty, Company


class MyCompanyView(View):
    def get(request):
        return render(request, os.path.join('jobs', 'my_company', 'company.html'), {})


class MyCompany