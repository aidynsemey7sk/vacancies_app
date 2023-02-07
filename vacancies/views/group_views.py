from vacancies.models import Group, Vacancy, VacancySettings
from django.shortcuts import render
from django.http import HttpResponseRedirect
from vacancies.forms import GroupForm, StartVacancyForm


def get_all_vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'vacancies/all_vacancies.html', {"vacancies": vacancies})


def create_group(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vacancies/groups')
    else:
        form = GroupForm()

    return render(request, "groups/create_group.html", {"form": form})


def get_all_groups(request):
    groups = Group.objects.all()
    return render(request, 'groups/all_groups.html', {"groups": groups})


def delete_group(request, group_id):
    group = Group.objects.get(id=group_id)
    group.delete()
    groups = Group.objects.all()
    return render(request, 'groups/all_groups.html', {"groups": groups})


def update_group(request, group_id):
    group = Group.objects.get(id=group_id)
    if request.method == "POST":
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vacancies/groups')
    else:
        form = GroupForm(instance=group)

    return render(request, "groups/update_group.html", {"form": form})


# Todo Продумать логику
def remove_group(request, setting_id):
    sett = VacancySettings.objects.get(id=setting_id)
    vacancy_id = sett.vacancy_id
    sett.delete()
    vacancy = Vacancy.objects.get(id=vacancy_id)

    settings = VacancySettings.objects.filter(vacancy_id=vacancy_id)
    if request.method == "POST":
        form = StartVacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/vacancies')
    else:
        form = StartVacancyForm(instance=vacancy)

    return render(request, 'vacancies/vacancy_detail.html', {"vacancy": vacancy, "settings": settings, "form": form})
