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

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.form_class = 'form-signin pt-5'
        self.helper.use_custom_control = True
        self.helper.layout = Layout(
            Row(
                Div(
                    Div(
                        Field('name'),
                        css_class='form-group pb-2'
                    ),
                    css_class='col-12 col-md-6',
                ),
                Div(
                    Div(
                        HTML('{{ form.logo.label_tag }}'
                             '{{ form.logo }}'
                             '<div class="text-danger list-inline-item"><strong>{{ form.logo.errors }}</strong></div>'),
                        css_class='form-group'
                    ),
                    css_class='col-12 col-md-6',
                ),
                Div(
                    Div(
                        Field('employee_count'),
                        css_class='form-group pb-2'
                    ),
                    css_class='col-12 col-md-6',
                ),
                Div(
                    Div(
                        Field('location'),
                        css_class='form-group pb-2'
                    ),
                    css_class='col-12 col-md-6',
                ),
                Div(
                    Div(
                        Field('description'),
                        css_class='form-group pb-2',
                    ),
                    css_class='col-12',
                ),
            ),
            FormActions(Submit('submit', 'Сохранить', css_class='btn btn-info')),
        )
