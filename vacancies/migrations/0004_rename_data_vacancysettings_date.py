# Generated by Django 4.1.6 on 2023-02-07 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_vacancysettings_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacancysettings',
            old_name='data',
            new_name='date',
        ),
    ]
