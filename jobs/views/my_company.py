import os

from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.urls import reverse

from jobs.models import Vacancy, Company
from jobs.forms.mycompany import CompanyForm, CompanyNoneLogoForm





class SendFeedBackView(View):
    def get(self, request):
        return render(request, os.path.join('jobs', 'my_company', 'sent.html'), {})


class MyCompanyView(View):
    def get(self, request):
        user = request.user
        if user.is_authenticated and user.is_active:
            mycompany = Company.objects.filter(owner=user).first()
            if mycompany is None:
                return render(request, os.path.join('jobs', 'my_company', 'company-create.html'), {})
            else:
                mycompany_form = CompanyForm(instance=mycompany)
                return render(request, os.path.join('jobs', 'my_company', 'company.html'), {'form': mycompany_form})
        else:
            if not user.is_authenticated:
                messages.error(request, "Вы не авторизированы. Пожалуйта авторизируйтесь")
            elif not user.is_active:
                messages.error(request, "Ваша учетная запись неактивна. "
                                        "Пожалуйста авторизируйтесь под другой учётной записью")
            return redirect(reverse('login'))

    def post(self, request):
        user = request.user
        mycompany = Company.objects.filter(owner=user).first()
        old_logo_path = mycompany.logo.path
        filepath = request.FILES.get('logo', False)
        if filepath:
            mycompany_form = CompanyForm(request.POST, request.FILES, instance=mycompany)
            if mycompany_form.is_valid():
                if os.path.exists(old_logo_path):
                    os.remove(old_logo_path)
                mycompany_form.save()
                messages.info(request, "Информация о компании обновлена")
        else:
            mycompany_none_logo_form = CompanyNoneLogoForm(request.POST, instance=mycompany)
            if mycompany_none_logo_form.is_valid():
                mycompany_none_logo_form.save()
                messages.info(request, "Информация о компании обновлена")
        return redirect(reverse('mycompany'))


class ListMyCompanyVacancyView(ListView):
    model = Vacancy
    template_name = os.path.join('jobs', 'my_company', 'company_vacancy_list.html')


class DetailMyCompanyVacancyView(DetailView):
    model = Vacancy
    template_name = os.path.join('jobs', 'my_company', 'company_vacancy_list.html')
