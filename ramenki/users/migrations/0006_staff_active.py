# Generated by Django 3.1 on 2020-09-16 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200911_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='active',
            field=models.BooleanField(default=True, help_text='Неактивные члены руководства не будут отображаться на сайте', verbose_name='Активен'),
        ),
    ]
