# Generated by Django 3.1 on 2020-08-24 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import image_cropping.fields
import multiselectfield.db.fields
import users.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('other', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('forename', models.CharField(max_length=150, verbose_name='Имя')),
                ('surname', models.CharField(blank=True, max_length=150, null=True, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Телефон')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Аккаунт',
                'verbose_name_plural': 'Аккаунты',
            },
            managers=[
                ('objects', users.models.CustomManager()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('position', multiselectfield.db.fields.MultiSelectField(choices=[('head-president', 'Президент клуба'), ('vice-president', 'Вице-президент клуба'), ('judiciary', 'Судейский корпус'), ('single-coach', 'Инструктор'), ('coach-committee', 'Тренерский комитет'), ('methodical-certification-committee', 'Методический и аттестационный комитет'), ('physical-mass-committee', 'Физкультурно-массовый комитет'), ('administration', 'Администрация'), ('parental-committee', 'Родительский комитет')], max_length=300, verbose_name='Должности')),
                ('short_description', models.CharField(default='', max_length=500, verbose_name='Короткое описание')),
                ('sports_kind', multiselectfield.db.fields.MultiSelectField(choices=[('karate', 'Каратэ'), ('taekwondo', 'Тхэквондо')], max_length=20, verbose_name='Виды спорта')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('qualification', models.IntegerField(blank=True, choices=[(1, '1 дан'), (2, '2 дан'), (3, '3 дан'), (4, '4 дан'), (5, '5 дан'), (6, '6 дан'), (7, '7 дан'), (8, '8 дан'), (9, '9 дан'), (10, '10 дан')], null=True, verbose_name='Квалификация (дан)')),
                ('started_trainings', models.IntegerField(blank=True, null=True, verbose_name='Год начала занятий')),
                ('weight', models.FloatField(blank=True, null=True, verbose_name='Вес')),
                ('additional_information', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Дополнительная информация')),
                ('photo', models.ImageField(blank=True, help_text='Возможность обрезки появится после сохранения', null=True, upload_to='staff', verbose_name='Фото')),
                ('photo_profile', image_cropping.fields.ImageRatioField('photo', '5000x5000', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=False, verbose_name='Обрезка фото для профиля')),
                ('photo_avatar', image_cropping.fields.ImageRatioField('photo', '80x80', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='Обрезка фото для аватара')),
                ('veteran', models.BooleanField(default=False, verbose_name='Ветеран (Да/Нет)')),
                ('merits', models.CharField(blank=True, max_length=10000, null=True, verbose_name='Заслуги')),
                ('sorting', models.CharField(default='z', help_text='Подразделы будут появляться в списке раздела, согласно данной сортировке (по алфавиту, в порядке убывания)', max_length=5, verbose_name='Сортировка')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='other.branch', verbose_name='Филиал')),
            ],
            options={
                'verbose_name': 'Член руководства',
                'verbose_name_plural': 'Члены руководства',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patronymic', models.CharField(blank=True, max_length=150, null=True, verbose_name='Отчество')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('budo_pass', models.CharField(blank=True, max_length=200, null=True, verbose_name='Номер будо пасспорта')),
                ('qualification_type', models.CharField(blank=True, choices=[('KU', 'КЮ'), ('DAN', 'Дан')], max_length=20, null=True, verbose_name='Тип квалификации')),
                ('qualification_number', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], null=True, verbose_name='Дан/Кю')),
                ('photo', models.ImageField(blank=True, default='personal-area/default-user.png', help_text='Возможность обрезки появится после сохранения', null=True, upload_to='personal-area/', verbose_name='Фото')),
                ('avatar_cut', image_cropping.fields.ImageRatioField('photo', '44x44', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='Обрезка фото для профиля')),
                ('use_social_photo', models.BooleanField(default=False, verbose_name='Использовать фото из соц. сети')),
                ('social_photo', models.TextField(blank=True, help_text='Заполняется автоматически', null=True, verbose_name='URL фото из соц. сети')),
                ('social_avatar', models.TextField(blank=True, help_text='Заполняется автоматически', null=True, verbose_name='URL аватара из соц. сети')),
                ('odnoklassniki', models.CharField(blank=True, max_length=200, null=True, verbose_name='Одноклассники')),
                ('facebook', models.CharField(blank=True, max_length=200, null=True, verbose_name='Фейсбук')),
                ('instagram', models.CharField(blank=True, max_length=200, null=True, verbose_name='Инстаграм')),
                ('vkontakte', models.CharField(blank=True, max_length=200, null=True, verbose_name='Вконтакте')),
                ('coach', models.ForeignKey(blank=True, limit_choices_to={'position__contains': 'single-coach'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.staff', verbose_name='Тренер')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]