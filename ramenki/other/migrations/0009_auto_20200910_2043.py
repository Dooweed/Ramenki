# Generated by Django 3.1 on 2020-09-10 15:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('other', '0008_auto_20200910_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='moscow_metro_station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='other.metrostation', verbose_name='Метро (список, только для Москвы)'),
        ),
    ]