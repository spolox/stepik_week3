from django.urls import resolve


def get_title(request):
    #current_url = resolve(request.path_info).url_name
    #'Регистрация | Джуманджи' register
    #'Войти | Джуманджи' login
    #'Создать резюме | Джуманджи' myresume
    #'Вакансии компании | Джуманджи'
    #'Отклик отправлен | Джуманджи'
    #'Моя компания | Джуманджи' mycompany
    #'Создать карточку компании | Джуманджи'
    return {
        'title': 'Джуманджи'
    }