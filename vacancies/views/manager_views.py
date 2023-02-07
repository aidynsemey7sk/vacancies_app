from vacancies.models import Manager
from django.shortcuts import render
from django.http import HttpResponseRedirect
from vacancies.forms import ManagerForm


def create_manager(request):
    if request.method == "POST":
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vacancies/managers')
    else:
        form = ManagerForm()

    return render(request, "managers/create_manager.html", {"form": form})


def get_all_manager(request):
    managers = Manager.objects.all()
    return render(request, 'managers/all_managers.html', {"managers": managers})


def delete_manager(request, manager_id):
    manager = Manager.objects.get(id=manager_id)
    manager.delete()
    managers = Manager.objects.all()
    return render(request, 'managers/all_managers.html', {"managers": managers})


def update_manager(request, manager_id):
    manager = Manager.objects.get(id=manager_id)
    if request.method == "POST":
        form = ManagerForm(request.POST, instance=manager)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/vacancies/managers')
    else:
        form = ManagerForm(instance=manager)

    return render(request, "managers/update_manager.html", {"form": form})
