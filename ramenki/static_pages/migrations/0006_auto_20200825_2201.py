# Generated by Django 3.1 on 2020-08-25 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0005_auto_20200825_2200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutstaticpage',
            options={'ordering': ('-sorting',), 'verbose_name': 'Страница раздела "О клубе"', 'verbose_name_plural': 'Страницы раздела "О клубе"'},
        ),
        migrations.AlterModelOptions(
            name='taekwondostaticpage',
            options={'ordering': ('-sorting',), 'verbose_name': 'Страница раздела "Тхэквондо"', 'verbose_name_plural': 'Страницы раздела "Тхэквондо"'},
        ),
    ]