from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

from jobs.models import Company


class LoginRequiredMixinOverride(LoginRequiredMixin):
    login_url = 'login'
    redirect_field_name = 'next'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Вы не авторизированы. Пожалуйта авторизируйтесь")
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class HasCompanyRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if Company.objects.filter(owner=self.request.user).first() is None:
            messages.error(self.request, 'У вас компании нету, создайте его для добавления новых вакансий')
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def handle_no_permission(self):
        return redirect(reverse_lazy('mycompany'))
