import os

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from jobs.forms.application import ApplicationForm
from jobs.models import Vacancy, Specialty, Company


def custom_handler404(request, exception):
    return HttpResponseNotFound('Извините, страница не найдена.')


def custom_handler500(request):
    return HttpResponseNotFound('Внутреняя ошибка сервака. Приносим свои извинения, повторите попытку позже')


class MainView(View):
    def get(self, request):
        context = {
            'companies': Company.objects.all(),
            'specialties': Specialty.objects.all(),
        }
        return render(request, os.path.join('jobs', 'public', 'index.html'), context)


class ListVacancyView(ListView):
    model = Vacancy
    template_name = os.path.join('jobs', 'public', 'vacancy_list.html')


class DetailVacancyView(DetailView):
    model = Vacancy
    template_name = os.path.join('jobs', 'public', 'vacancy_detail.html')

    def get_context_data(self, **kwargs):
        context = super(DetailVacancyView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['form'] = ApplicationForm(self.kwargs['pk'])
        return context


class ListSpecialtyView(DetailView):
    model = Specialty
    template_name = os.path.join('jobs', 'public', 'specialty_detail.html')


class DetailCompanyView(DetailView):
    model = Company
    template_name = os.path.join('jobs', 'public', 'company_detail.html')


class SendFeedBackView(View):
    def post(self, request, pk):
        application_form = ApplicationForm(pk, request.POST)
        vacancy = Vacancy.objects.filter(id=pk).first()
        if application_form.is_valid():
            application_instance = application_form.save(commit=False)
            application_instance.user = request.user
            application_instance.vacancy = vacancy
            application_instance.save()
        else:
            return render(request, os.path.join('jobs', 'public', 'vacancy_detail.html'),
                          {'form': application_form, 'pk': pk, 'vacancy': vacancy})
        return render(request, os.path.join('jobs', 'public', 'sent.html'), {'pk': pk})
