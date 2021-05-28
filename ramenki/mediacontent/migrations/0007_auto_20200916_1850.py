# Generated by Django 3.1 on 2020-09-16 13:50

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mediacontent', '0006_auto_20200916_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photogallery',
            name='crop',
            field=image_cropping.fields.ImageRatioField('thumbnail', '448x276', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='Обрезка изображения для обложки'),
        ),
        migrations.AlterField(
            model_name='video',
            name='crop',
            field=image_cropping.fields.ImageRatioField('thumbnail', '448x276', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='Обрезка изображения для обложки'),
        ),
    ]
