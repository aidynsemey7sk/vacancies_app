from django.urls import path

from vacancies.views.vacancy_views import get_all_vacancies, vacancy_detail, delete_vacancy, create_vacancy, \
    update_vacancy,get_vacancies_for_today

from vacancies.views.group_views import create_group, get_all_groups, delete_group, update_group, remove_group

from vacancies.views.vacancy_settings_views import add_group, update_time

from vacancies.views.manager_views import create_manager, get_all_manager, delete_manager, update_manager


urlpatterns = [
    path('', get_all_vacancies, name="get_all_vacancies"),
    path('vacancy-for-today/', get_vacancies_for_today, name="get_vacancies_for_today"),
    path('update-time/<int:settings_id>/', update_time, name="update_time"),
    path('add-settings/<int:vacancy_id>/', add_group, name="add_group"),

    # Vacancy
    path('create-vacancy/', create_vacancy, name="create_vacancy"),
    path('delete-vacancy/<int:vacancy_id>/', delete_vacancy, name="delete_vacancy"),
    path('vacancy-detail/<int:vacancy_id>/', vacancy_detail, name="vacancy_detail"),
    path('update-vacancy/<int:vacancy_id>/', update_vacancy, name="update_vacancy"),

    # Group
    path('groups/', get_all_groups, name="get_all_groups"),
    path('create-group/', create_group, name="create_group"),
    path('delete-group/<int:group_id>/', delete_group, name="delete_group"),
    path('update-group/<int:group_id>/', update_group, name="update_group"),

    # Manager
    path('managers/', get_all_manager, name="get_all_manager"),
    path('delete-manager/<int:manager_id>/', delete_manager, name="delete_manager"),
    path('update-manager/<int:manager_id>/', update_manager, name="update_manager"),
    path('create-manager/', create_manager, name="create_manager"),
]