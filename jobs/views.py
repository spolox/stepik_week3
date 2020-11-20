from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from jobs.models import Vacancy, Specialty, Company


def custom_handler404(request, exception):
    return HttpResponseNotFound('Извините, страница не найдена.')


def custom_handler500(request):
    return HttpResponseNotFound('Внутреняя ошибка сервака. Приносим свои извинения, повторите попытку позже')


class MainView(View):
    @staticmethod
    def get(request):
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
