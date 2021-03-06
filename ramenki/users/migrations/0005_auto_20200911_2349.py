# Generated by Django 3.1 on 2020-09-11 18:49

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0012_auto_20200911_2349'),
        ('users', '0004_auto_20200911_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='birth_date',
            field=models.DateField(blank=True, help_text='Оставьте все три поля пустыми, если дата рождения неизвестна', null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='branch',
            field=models.ManyToManyField(blank=True, to='other.Branch', verbose_name='Филиал'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('head-president', 'Президент клуба'), ('vice-president', 'Вице-президент клуба'), ('judiciary', 'Судейский корпус'), ('single-coach', 'Инструктор'), ('coach-committee', 'Тренерский комитет'), ('methodical-certification-committee', 'Методический и аттестационный комитет'), ('physical-mass-committee', 'Физкультурно-массовый комитет'), ('administration', 'Администрация'), ('parental-committee', 'Родительский комитет')], max_length=300, null=True, verbose_name='Должности'),
        ),
    ]
