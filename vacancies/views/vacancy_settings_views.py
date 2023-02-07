from vacancies.models import Group, Vacancy, VacancySettings, Time, RandomTime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from vacancies.forms import VacancySettingsForm, UpdateTimeForm
import random
import datetime


def add_group(request, vacancy_id):
    if request.method == "POST":
        form = VacancySettingsForm(request.POST)
        if form.is_valid():
            form.save()
            obj = form.instance
            for i in range(obj.from_time_id, obj.to_time_id + 1, int(obj.period)):
                time = Time.objects.get(id=i).time
                minute = str(random.randint(0, 60))
                tt = datetime.time(hour=int(time[:2]), minute=int(minute), second=0)
                random_time = RandomTime.objects.create(time=tt)
                print(random_time)
                obj.random_time.add(random_time)

            return HttpResponseRedirect(f'/vacancies/vacancy-detail/{vacancy_id}')
    else:
        form = VacancySettingsForm({"vacancy": vacancy_id})
    return render(request, "vacancy_settings/add_settings.html", {"form": form})


def update_time(request, settings_id):
    instance = VacancySettings.objects.get(id=settings_id)
    if request.method == "POST":
        form = UpdateTimeForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/vacancies/vacancy-detail/{instance.vacancy_id}')
    else:
        form = UpdateTimeForm(instance=instance)
    return render(request, "times/update_time.html", {"form": form})
