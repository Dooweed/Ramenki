# Generated by Django 3.1 on 2020-08-25 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0004_auto_20200825_2129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='karatestaticpage',
            options={'ordering': ('-sorting',), 'verbose_name': 'Страница раздела "Карате"', 'verbose_name_plural': 'Страницы раздела "Карате"'},
        ),
    ]