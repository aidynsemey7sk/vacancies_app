from django.contrib import admin
from vacancies.models import Vacancy, Time, Group, VacancySettings, Manager

admin.site.register(Vacancy)
admin.site.register(Time)
admin.site.register(Group)
admin.site.register(VacancySettings)
admin.site.register(Manager)
