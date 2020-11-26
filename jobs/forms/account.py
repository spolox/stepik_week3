from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML
from crispy_forms.bootstrap import Field, FormActions, Div

from django import forms


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput)
    password = forms.CharField(label='', widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.form_class = 'form-signin pt-5'

        self.helper.layout = Layout(
            Div(
                HTML('<p class="text-muted">Логин</p>'),
                Field('username'),
            ),
            Div(
                HTML('<p class="text-muted"> Пароль</p>'),
                Field('password'),
            ),
            FormActions(Submit('submit', 'Войти', css_class='btn btn-primary btn-lg btn-block mt-5')),
        )


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='', widget=forms.TextInput)
    first_name = forms.CharField(label='', widget=forms.TextInput)
    last_name = forms.CharField(label='', widget=forms.TextInput)
    password = forms.CharField(label='', widget=forms.PasswordInput)


    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.form_class = 'form-signin pt-5'

        self.helper.layout = Layout(
            Div(
                HTML('<p class="text-muted">Логин</p>'),
                Field('username'),
            ),
            Div(
                HTML('<p class="text-muted">Имя</p>'),
                Field('first_name'),
            ),
            Div(
                HTML('<p class="text-muted">Фамилия</p>'),
                Field('last_name'),
            ),
            Div(
                HTML('<p class="text-muted"> Пароль</p>'),
                Field('password'),
            ),
            FormActions(Submit('submit', 'Войти', css_class='btn btn-primary btn-lg btn-block mt-5')),
        )