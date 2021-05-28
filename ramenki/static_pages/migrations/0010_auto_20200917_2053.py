# Generated by Django 3.1 on 2020-09-17 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0009_auto_20200917_1959'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutstaticpage',
            name='meta_robots_tag',
            field=models.CharField(blank=True, help_text='Оставьте поле пустым, чтобы использовать метатег robots базового шаблона', max_length=500, null=True, verbose_name='Содержимое тега <meta name="robots">'),
        ),
        migrations.AddField(
            model_name='karatestaticpage',
            name='meta_robots_tag',
            field=models.CharField(blank=True, help_text='Оставьте поле пустым, чтобы использовать метатег robots базового шаблона', max_length=500, null=True, verbose_name='Содержимое тега <meta name="robots">'),
        ),
        migrations.AddField(
            model_name='taekwondostaticpage',
            name='meta_robots_tag',
            field=models.CharField(blank=True, help_text='Оставьте поле пустым, чтобы использовать метатег robots базового шаблона', max_length=500, null=True, verbose_name='Содержимое тега <meta name="robots">'),
        ),
        migrations.AlterField(
            model_name='aboutstaticpage',
            name='meta_keywords_tag',
            field=models.CharField(blank=True, help_text='Оставьте поле пустым, чтобы использовать метатег keywords базового шаблона', max_length=500, null=True, verbose_name='Содержимое тега <meta name="keywords">'),
        ),
        migrations.AlterField(
            model_name='karatestaticpage',
            name='meta_keywords_tag',
            field=models.CharField(blank=True, help_text='Оставьте поле пустым, чтобы использовать метатег keywords базового шаблона', max_length=500, null=True, verbose_name='Содержимое тега <meta name="keywords">'),
        ),
        migrations.AlterField(
            model_name='taekwondostaticpage',
            name='meta_keywords_tag',
            field=models.CharField(blank=True, help_text='Оставьте поле пустым, чтобы использовать метатег keywords базового шаблона', max_length=500, null=True, verbose_name='Содержимое тега <meta name="keywords">'),
        ),
    ]