# Generated by Django 3.1 on 2020-09-10 12:34

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0006_auto_20200825_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutstaticpage',
            name='url',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='title', unique=True, verbose_name='URL подраздела'),
        ),
        migrations.AlterField(
            model_name='karatestaticpage',
            name='url',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='title', unique=True, verbose_name='URL подраздела'),
        ),
        migrations.AlterField(
            model_name='taekwondostaticpage',
            name='url',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='title', unique=True, verbose_name='URL подраздела'),
        ),
    ]