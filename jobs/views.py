from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from jobs.models import Vacancy, Specialty, Company


# TODO error 404, 500
class MainView(View):
    def get(self, request):
        context = {
            'companies': Company.objects.all(),
            'specialties': Specialty.objects.all(),
        }
        return render(request, 'index.html', context)


class ListVacancyView(ListView):
    model = Vacancy

    def get_queryset(self):
        return Vacancy.objects.all()


class DetailVacancyView(DetailView):
    model = Vacancy


class ListSpecialtyView(DetailView):
    model = Specialty


class DetailCompanyView(DetailView):
    model = Company
