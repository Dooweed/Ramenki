# Generated by Django 3.1 on 2020-09-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediacontent', '0009_auto_20200916_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediacategory',
            name='meta_description',
            field=models.CharField(blank=True, help_text='Оставьте поле пустым, чтобы использовать информацию из шаблона news.html', max_length=1000, null=True, verbose_name='Описание (мета-тег)'),
        ),
    ]
