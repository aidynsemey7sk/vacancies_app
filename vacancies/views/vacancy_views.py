from vacancies.models import Group, Vacancy, VacancySettings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from vacancies.forms import StartVacancyForm, VacancyForm
import datetime

today = datetime.datetime.today()


def get_all_vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies/all_vacancies.html', {"vacancies": vacancies})


def get_vacancies_for_today(request):
    print(today)
    vacancies = Vacancy.objects.filter(date=today)
    return render(request, 'vacancies/vacancy_for_today.html', {"vacancies": vacancies})



def vacancy_detail(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    settings = VacancySettings.objects.filter(vacancy_id=vacancy_id)

    for sett in settings:
        sett.get_time()

    if request.method == "POST":
        form = StartVacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/vacancies')
    else:
        form = StartVacancyForm(instance=vacancy)

    return render(request, 'vacancies/vacancy_detail.html', {"vacancy": vacancy, "settings": settings, "form": form})


def delete_vacancy(request, vacancy_id):
    vacancy = Vacancy.objects.get(id=vacancy_id)
    settings = VacancySettings.objects.filter(vacancy=vacancy)
    settings.delete()
    vacancy.delete()
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies/all_vacancies.html', {"vacancies": vacancies})


def create_vacancy(request):
    if request.method == "POST":
        form = VacancyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/vacancies/vacancy-detail/{form.instance.id}/')
    else:
        form = VacancyForm()
    return render(request, "vacancies/create_vacancy.html", {"form": form})


def update_vacancy(request, vacancy_id):
    manager = Vacancy.objects.get(id=vacancy_id)
    if request.method == "POST":
        form = VacancyForm(request.POST, instance=manager)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/vacancies/vacancy-detail/{vacancy_id}/')
    else:
        form = VacancyForm(instance=manager)

    return render(request, "vacancies/update_vacancy.html", {"form": form})


