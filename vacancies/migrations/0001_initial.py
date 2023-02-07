# Generated by Django 4.1.6 on 2023-02-06 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('chat_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('client_id', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='RandomTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('text', models.CharField(max_length=300)),
                ('enable', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='VacancySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(choices=[('2', 'Каждые два часа'), ('1', 'Каждый час'), ('3', 'Каждые три часа')], default='1', max_length=20)),
                ('from_time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='from_time', to='vacancies.time')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.group')),
                ('last_send_manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_send_manager', to='vacancies.manager')),
                ('manager', models.ManyToManyField(to='vacancies.manager')),
                ('random_time', models.ManyToManyField(to='vacancies.randomtime')),
                ('time', models.ManyToManyField(to='vacancies.time')),
                ('to_time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_time', to='vacancies.time')),
                ('vacancy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vacancies.vacancy')),
            ],
        ),
    ]