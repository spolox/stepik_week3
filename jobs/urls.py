from django.urls import re_path, path

from jobs.views import MainView, ListVacancyView, DetailVacancyView, ListSpecialtyView, DetailCompanyView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('companies/<int:pk>', DetailCompanyView.as_view(), name='company-detail'),
    path('vacancies/', ListVacancyView.as_view(), name='vacancy-list'),
    path('vacancies/<int:pk>', DetailVacancyView.as_view(), name='vacancy-detail'),
    path('vacancies/cat/<str:code>', ListSpecialtyView.as_view(), name='specialty-list'),
]
