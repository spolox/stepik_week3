import os

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import View
from django.urls import reverse

from jobs.models import Vacancy, Company
from jobs.forms.mycompany import CompanyForm
from jobs.views.override import LoginRequiredMixinOverride


class SendFeedBackView(View):
    def get(self, request):
        return render(request, os.path.join('jobs', 'my_company', 'sent.html'), {})


class MyCompanyView(LoginRequiredMixinOverride, View):
    def get(self, request):
        user = request.user
        user_company = Company.objects.filter(owner=user).first()
        user_company_form = None
        context = {}
        if user_company is None and request.GET.get('create'):
            user_company_form = CompanyForm(None)
        elif user_company is not None:
            user_company_form = CompanyForm(instance=user_company)
            context['is_exists'] = True
        context['form'] = user_company_form
        return render(request, os.path.join('jobs', 'my_company', 'company.html'), context)

    def post(self, request):
        user = request.user
        user_company = Company.objects.filter(owner=user).first()
        user_company_form = CompanyForm(request.POST, request.FILES, instance=user_company)
        if user_company_form.is_valid():
            if user_company:
                user_company_form.save()
                messages.info(request, "Информация о компании обновлена")
            else:
                user_company_instance = user_company_form.save(commit=False)
                user_company_instance.owner = user
                user_company_instance.save()
                messages.info(request, "Компания была создана")
        else:
            messages.error(request, "Проверьте правильность введенной информации!")
            return render(request, os.path.join('jobs', 'my_company', 'company.html'), {'form': user_company_form})
        return redirect(reverse('mycompany'))


class MyCompanyCreateView(LoginRequiredMixinOverride, View):
    def get(self, request):
        pass


class MyCompanyDeleteView(LoginRequiredMixinOverride, View):
    def post(self, request):
        user = request.user
        print(Company.objects.filter(owner=user).delete())
        messages.warning(request, "Компания была удалена")
        return redirect(self.request.GET.get('next'))


class ListMyCompanyVacancyView(LoginRequiredMixinOverride, ListView):
    model = Vacancy
    template_name = os.path.join('jobs', 'my_company', 'company_vacancy_list.html')

    def get_queryset(self):
        queryset = Vacancy.objects.filter(company__owner=self.request.user)
        if queryset.count() == 0:
            messages.info(self.request, 'У вас пока нет вакансий, но вы можете создать первую!')
        return queryset


class DetailMyCompanyVacancyView(LoginRequiredMixinOverride, DetailView):
    model = Vacancy
    template_name = os.path.join('jobs', 'my_company', 'company_vacancy_list.html')
