from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginRequiredMixinOverride(LoginRequiredMixin):
    login_url = 'login'
    redirect_field_name = 'next'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Вы не авторизированы. Пожалуйта авторизируйтесь")
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)