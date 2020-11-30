from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag()
def get_variable(id_vacancy):
    context = {
        'id_modal': 'id_vacancy_delete',
        'modal_title': 'Удаление вакансии',
        'modal_message': 'Вы уверены, что хотите удалить вакансию? Потом его нельзя будет восстановить',
        'modal_url_action': reverse('mycompany-vacancy-delete', kwargs={'pk': id_vacancy}),
        'next_url': reverse('mycompany-vacancy-list'),
    }
    return context
