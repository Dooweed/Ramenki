# Generated by Django 3.1 on 2020-08-24 19:59

import autoslug.fields
from django.db import migrations, models
import image_cropping.fields
import ramenki.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название категории')),
                ('url', autoslug.fields.AutoSlugField(editable=True, populate_from='name', unique=True, validators=[ramenki.utils.category_url_validator], verbose_name='URL категории')),
                ('active', models.BooleanField(default=True, help_text='Неактивные категории не будут отображаться в списке категорий', verbose_name='Активно')),
            ],
            options={
                'verbose_name': 'Категория статей',
                'verbose_name_plural': 'Категории статей',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок статьи')),
                ('text', models.TextField(verbose_name='Текст статьи')),
                ('status', models.CharField(choices=[('editing', 'Редактирование'), ('pending', 'Ожидание'), ('published', 'Опубликовано')], default='editing', help_text='Отображаться будут только статьи с состоянием "Выпущено"', max_length=30, verbose_name='Состояние статьи')),
                ('short_text', models.CharField(blank=True, help_text='Информация для превью статьи (необязательно)', max_length=500, null=True, verbose_name='Краткая информация о статье')),
                ('image', models.ImageField(blank=True, help_text='Возможность обрезки появится после сохранения', null=True, upload_to='articles/', verbose_name='Изображение статьи')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('thumbnail_size', image_cropping.fields.ImageRatioField('image', '288x276', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='Обрезка изображения для превью')),
                ('article_size', image_cropping.fields.ImageRatioField('image', '0x0', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='Обрезка изображения для статьи')),
                ('associations', models.ManyToManyField(blank=True, help_text='(необязательно)', to='news.ArticleCategory', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
