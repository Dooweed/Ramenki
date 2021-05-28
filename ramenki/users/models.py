from django.db import models
from ramenki.static_vars import POSITIONS, KINDS_OF_SPORTS, DANS, QUALIFICATION_TYPES
from other.models import Branch
from image_cropping import ImageRatioField
from multiselectfield import MultiSelectField
from django.utils import timezone
from django.shortcuts import reverse
from ramenki.utils import get_ending, paired_range, make_link, link_tag
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import SafeString
from django.db.models import signals


# Create your models here.


class Staff(models.Model):
    name = models.CharField("Имя", max_length=150)
    position = MultiSelectField("Должности", max_length=300, choices=POSITIONS, null=True, blank=True)
    short_description = models.CharField("Короткое описание", max_length=500, default="", null=True, blank=True)
    active = models.BooleanField("Активен", help_text="Неактивные члены руководства не будут отображаться на сайте", default=True)
    sports_kind = MultiSelectField("Виды спорта", max_length=20, choices=KINDS_OF_SPORTS)
    birth_date = models.DateField("Дата рождения", help_text="Оставьте все три поля пустыми, если дата рождения неизвестна", null=True, blank=True)
    qualification = models.IntegerField("Квалификация (дан)", choices=DANS, null=True, blank=True)
    started_trainings = models.IntegerField("Год начала занятий", null=True, blank=True)
    weight = models.FloatField("Вес", null=True, blank=True)
    additional_information = models.TextField("Дополнительная информация", null=True, blank=True)
    branch = models.ManyToManyField(verbose_name="Филиал", to=Branch, blank=True)
    photo = models.ImageField("Фото", upload_to='staff', help_text="Возможность обрезки появится после сохранения", null=True, blank=True)
    photo_profile = ImageRatioField(verbose_name="Обрезка фото для профиля", image_field='photo', size="5000x5000", free_crop=True)
    photo_avatar = ImageRatioField(verbose_name="Обрезка фото для аватара", image_field='photo', size="80x80")
    veteran = models.BooleanField("Ветеран (Да/Нет)", default=False)
    merits = models.TextField("Заслуги", null=True, blank=True)
    sorting = models.CharField("Сортировка", max_length=5, help_text="Подразделы будут появляться в списке раздела, согласно данной сортировке (по алфавиту, в порядке убывания)",
                               default="zz")

    def __str__(self):
        return self.name

    def verbose_position(self):
        return self.get_position_display()

    verbose_position.short_description = "Должность"

    def verbose_sports_kinds(self):
        return self.get_sports_kind_display()

    verbose_sports_kinds.short_description = "Виды спорта"

    def age(self):
        if not self.birth_date:
            return None
        today = timezone.now()
        if today.month > self.birth_date.month:
            age = str(today.year - self.birth_date.year)
        elif today.month == self.birth_date.month and today.day >= self.birth_date.day:
            age = str(today.year - self.birth_date.year)
        else:
            age = str(today.year - self.birth_date.year - 1)
        return get_ending(age, ("год", "года", "лет"))

    def years_in_sports(self):
        if self.started_trainings:
            return f"{get_ending(str(timezone.now().year - self.started_trainings), ('год', 'года', 'лет'))} занимается {self.get_sports_kind_display()}"
        else:
            return ""

    def has_photo(self):
        return bool(self.photo)

    has_photo.short_description = "Есть фото"
    has_photo.boolean = bool(photo)

    class Meta:
        verbose_name = "Член руководства"
        verbose_name_plural = "Члены руководства"


class CustomManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        Profile.objects.create(user=user)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    forename = models.CharField("Имя", max_length=150)
    surname = models.CharField("Фамилия", max_length=150, blank=True, null=True)
    email = models.EmailField("Email", unique=True)
    phone = models.CharField("Телефон", max_length=100, null=True, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False, help_text=_('Designates whether the user can log into this admin site.'), )
    objects = CustomManager()

    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'), )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['forename', 'surname']

    def __str__(self):
        return self.email if self.email else self.id

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"


class Profile(models.Model):
    user = models.OneToOneField(verbose_name="Пользователь", to=CustomUser, on_delete=models.CASCADE)
    patronymic = models.CharField("Отчество", max_length=150, null=True, blank=True)
    birth_date = models.DateField("Дата рождения", null=True, blank=True)
    coach = models.ForeignKey(verbose_name="Тренер", to=Staff, on_delete=models.DO_NOTHING, limit_choices_to={"position__contains": "single-coach"}, null=True, blank=True)
    budo_pass = models.CharField("Номер будо пасспорта", max_length=200, null=True, blank=True)
    qualification_type = models.CharField("Тип квалификации", choices=QUALIFICATION_TYPES, max_length=20, null=True, blank=True)
    qualification_number = models.IntegerField("Дан/Кю", choices=paired_range(1, 11), null=True, blank=True)
    photo = models.ImageField("Фото", upload_to="personal-area/", help_text="Возможность обрезки появится после сохранения", default='personal-area/default-user.png', null=True,
                              blank=True)
    avatar_cut = ImageRatioField(verbose_name="Обрезка фото для профиля", image_field='photo', size="44x44")
    use_social_photo = models.BooleanField("Использовать фото из соц. сети", default=False)
    social_photo = models.TextField("URL фото из соц. сети", help_text="Заполняется автоматически", null=True, blank=True)
    social_avatar = models.TextField("URL аватара из соц. сети", help_text="Заполняется автоматически", null=True, blank=True)

    odnoklassniki = models.CharField("Одноклассники", max_length=200, null=True, blank=True)
    facebook = models.CharField("Фейсбук", max_length=200, null=True, blank=True)
    instagram = models.CharField("Инстаграм", max_length=200, null=True, blank=True)
    vkontakte = models.CharField("Вконтакте", max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{f'{self.user.surname} ' if self.user.surname else ''}{self.user.forename}{f'{self.patronymic} ' if self.patronymic else ''}"

    def full_name(self):
        return f"{f'{self.user.surname} ' if self.user.surname else ''} {self.user.forename}{f'{self.patronymic} ' if self.patronymic else ''}"
    full_name.short_description = "Полное имя"

    def edit_user(self):
        url = reverse('admin:%s_%s_change' % (self.user._meta.app_label, self.user._meta.model_name), args=[self.user.id])
        return SafeString(f"Вы можете изменить параметры аккаунта {link_tag(url, name='перейдя по этой ссылке')}")

    edit_user.short_description = "Аккаунт"

    def name(self):
        return f"{self.user.forename}{f' {self.user.surname}' if self.user.surname else ''}"

    def has_photo(self):
        return bool(self.photo)

    def qualification(self):
        return f"{self.qualification_number} {self.get_qualification_type_display()}" if self.qualification_type and self.qualification_number else ""
    qualification.short_description = "Квалификация"

    def verbose_birth_date(self):
        print(bool(self.birth_date))
        return self.birth_date.strftime("%d.%m.%Y") if self.birth_date else ""

    def odnoklassniki_link(self):
        if not self.odnoklassniki:
            return ""
        return make_link(self.odnoklassniki)

    def facebook_link(self):
        if not self.facebook:
            return ""
        return make_link(self.facebook)

    def instagram_link(self):
        if not self.instagram:
            return ""
        return make_link(self.instagram)

    def vkontakte_link(self):
        if not self.vkontakte:
            return ""
        return make_link(self.vkontakte)

    def age(self):
        if not self.birth_date:
            return ""
        today = timezone.now()
        if today.month > self.birth_date.month:
            age = str(today.year - self.birth_date.year)
        elif today.month == self.birth_date.month and today.day >= self.birth_date.day:
            age = str(today.year - self.birth_date.year)
        else:
            age = str(today.year - self.birth_date.year - 1)
        return get_ending(age, ("год", "года", "лет"))

    def age_and_date(self):
        return f"{self.age()} ({self.verbose_birth_date()})" if self.birth_date else "-"
    age_and_date.short_description = "Дата рождения"

    has_photo.short_description = "Есть фото"
    has_photo.boolean = bool(photo)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"


def create_profile(sender, instance, created, **kwargs):
    """Create Profile for every new CustomUser."""
    if created:
        Profile.objects.create(user=instance)


signals.post_save.connect(create_profile, sender=CustomUser, weak=False, dispatch_uid='models.create_profile')
