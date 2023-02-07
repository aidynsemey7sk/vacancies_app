from django.forms import ModelForm
from django import forms
from ckeditor.widgets import CKEditorWidget

from vacancies.models import Vacancy, Group, VacancySettings, Time, TIME_CHOICES, Manager


class VacancySettingsForm(ModelForm):
    vacancy = forms.ModelChoiceField(queryset=Vacancy.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control',
                                                                "placeholder": "Выберите вакансию"}))
    group = forms.ModelChoiceField(queryset=Group.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control',
                                                              "placeholder": "Выберите группу"}))

    period = forms.ChoiceField(choices=TIME_CHOICES,
                               widget=forms.Select(attrs={'class': 'form-control', "placeholder": "Частота"}))

    manager = forms.ModelMultipleChoiceField(queryset=Manager.objects.all(),
                                             widget=forms.CheckboxSelectMultiple)

    from_time = forms.ModelChoiceField(queryset=Time.objects.all(),
                                       widget=forms.Select(attrs={'class': 'form-control',
                                                                  "placeholder": "Выберите вакансию"}))

    to_time = forms.ModelChoiceField(queryset=Time.objects.all(),
                                     widget=forms.Select(attrs={'class': 'form-control',
                                                                "placeholder": "Выберите вакансию"}))



    class Meta:
        model = VacancySettings
        fields = ("vacancy", "group", "period", "manager", "from_time", "to_time")


class UpdateTimeForm(ModelForm):
    time = forms.ModelMultipleChoiceField(queryset=Time.objects.all(),
                                          widget=forms.CheckboxSelectMultiple)

    period = forms.ChoiceField(choices=TIME_CHOICES,
                               widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = VacancySettings
        fields = ('time',)


class StartVacancyForm(ModelForm):
    enable = forms.BooleanField(required=False, label='Старт')

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date',
                                                         "placeholder": "дата"}))

    class Meta:
        model = Vacancy
        fields = ('enable', "date")


class VacancyForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': "form-control", "textarea"
                   "placeholder": "Введите название вакансии"}))

    # text = forms.CharField(
    #     widget=forms.Textarea())
    text = forms.CharField(
        widget=CKEditorWidget())

    class Meta:
        model = Vacancy
        fields = ("title", 'text')


class GroupForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",
               "placeholder": "Введите название группы"}))

    chat_id = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",
               "placeholder": "Введите ID группы"}))

    class Meta:
        model = Group
        fields = ("name", 'chat_id')


class ManagerForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",
               "placeholder": "Введите имя аккаунта"}))

    client_id = forms.CharField(widget=forms.TextInput(
        attrs={'class': "form-control",
               "placeholder": "Введите ID аккаунта"}))

    class Meta:
        model = Manager
        fields = ("name", 'client_id')
