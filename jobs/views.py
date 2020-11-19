from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from jobs.models import Vacancy, Specialty, Company


class MainView(View):
    def get(self, request):
        return render(request, 'index.html')


class ListVacancyView(ListView):
    model = Vacancy

    def get_queryset(self):
        return Vacancy.objects.all()


class DetailVacancyView(DetailView):
    model = Vacancy


class ListSpecialtyView(ListView):
    model = Specialty

    def get_queryset(self):
        return Vacancy


class DetailCompanyView(DetailView):
    model = Company




