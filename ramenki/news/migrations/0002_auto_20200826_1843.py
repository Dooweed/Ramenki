# Generated by Django 3.1 on 2020-08-26 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateTimeField(verbose_name='Дата создания'),
        ),
    ]
