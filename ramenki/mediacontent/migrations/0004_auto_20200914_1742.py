# Generated by Django 3.1 on 2020-09-14 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mediacontent', '0003_auto_20200910_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photogallery',
            name='photos',
        ),
        migrations.AddField(
            model_name='photo',
            name='gallery',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='mediacontent.photogallery', verbose_name='Галерея'),
            preserve_default=False,
        ),
    ]