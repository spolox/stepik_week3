"""stepik_hh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from jobs.views import MainView, ListVacancyView, DetailVacancyView, ListSpecialtyView, DetailCompanyView
from jobs.views import custom_handler404, custom_handler500


handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('companies/<int:pk>', DetailCompanyView.as_view(), name='company-detail'),
    path('vacancies/', ListVacancyView.as_view(), name='vacancy-list'),
    path('vacancies/<int:pk>', DetailVacancyView.as_view(), name='vacancy-detail'),
    path('vacancies/cat/<str:pk>', ListSpecialtyView.as_view(), name='specialty-list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
