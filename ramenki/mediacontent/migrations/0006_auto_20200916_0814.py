# Generated by Django 3.1 on 2020-09-16 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mediacontent', '0005_auto_20200915_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='gallery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mediacontent.photogallery', verbose_name='Галерея'),
        ),
    ]
