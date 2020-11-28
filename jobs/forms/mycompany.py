import os

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Row, Column
from crispy_forms.bootstrap import Field, FormActions, Div
from django import forms
from django.forms.widgets import ClearableFileInput
from django.conf import settings
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.conf import settings

from jobs.models import Company


class CustomClearableFileInput(ClearableFileInput):
    template_name = os.path.join('widgets', 'load_image.html')


class CompanyForm(forms.ModelForm):

    name = forms.CharField(label='Название компании', label_suffix='', max_length=100)
    name.widget.attrs.update({'class': 'form-control'})
    employee_count = forms.CharField(label='Количество человек в компании', label_suffix='', max_length=100)
    employee_count.widget.attrs.update({'class': 'form-control'})
    location = forms.CharField(label='География', label_suffix='', max_length=100)
    location.widget.attrs.update({'class': 'form-control'})
    description = forms.CharField(label='Информация о компании', label_suffix='', widget=forms.Textarea)
    description.widget.attrs.update({'class': 'form-control', 'rows': 5, 'cols': 10})
    logo = forms.ImageField(label='Логотип', label_suffix='', widget=CustomClearableFileInput)

    class Meta:
        model = Company
        fields = ['name', 'location', 'logo', 'description', 'employee_count']

class CompanyNoneLogoForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['name', 'location', 'description', 'employee_count']
