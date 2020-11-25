import os

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from jobs.models import Vacancy


class SendFeedBackView(View):
    def get(self, request):
        return render(request, os.path.join('jobs', 'my_company', 'sent.html'), {})


class MyCompanyView(View):
    def get(self, request):
        return render(request, os.path.join('jobs', 'my_company', 'company.html'), {})


class ListMyCompanyVacancyView(ListView):
    model = Vacancy
    template_name = os.path.join('jobs', 'my_company', 'company_vacancy_list.html')

    def get_queryset(self):
        return Vacancy.objects.all()


class DetailMyCompanyVacancyView(DetailView):
    model = Vacancy
    template_name = os.path.join('jobs', 'my_company', 'company_vacancy_list.html')
