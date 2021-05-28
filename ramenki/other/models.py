from django.db import models
from image_cropping import ImageRatioField
from django.db.models.functions import Length, Left


# Create your models here.

class SliderItem(models.Model):
    header = models.CharField("Заголовок слайда", max_length=400)
    body = models.CharField("Текст слайда", max_length=4000, null=True, blank=True)
    image = models.ImageField("Картинка слайда", upload_to="slider/", help_text="Возможность обрезки появится после сохранения")
    active = models.BooleanField("Активен", default=True, help_text="Неактивные слайды не будут отображаться на главной странице")
    crop_mobile = ImageRatioField(verbose_name="Обрезка изображения (Мобильные)", image_field='image', size="320x594")
    crop_tablet = ImageRatioField(verbose_name="Обрезка изображения (Планшет)", image_field='image', size="756x504")
    crop_index = ImageRatioField(verbose_name="Обрезка изображения (Обычный)", image_field='image', size="687x458")
    crop_wide = ImageRatioField(verbose_name="Обрезка изображения (Широкий)", image_field='image', size="1105x628")
    sorting = models.PositiveIntegerField("Сортировка", help_text="Слайды будут расположены согласно данной сортировке", default=0)

    def __str__(self):
        return self.header

    class Meta:
        ordering = ('-sorting',)
        verbose_name = "Слайд"
        verbose_name_plural = "Слайды"


class MiniSliderItem(models.Model):
    quote = models.TextField("Цитата", max_length=1000)
    author = models.CharField("Автор цитаты", max_length=100, null=True, blank=True)
    description = models.CharField("Краткая информация об авторе цитаты", max_length=400, null=True, blank=True)
    image = models.ImageField("Фото автора цитаты", upload_to="slider-mini/", help_text="Возможность обрезки появится после сохранения", null=True, blank=True)
    active = models.BooleanField("Активен", default=True, help_text="Неактивные цитаты не будут отображаться на главной странице")
    crop_normal = ImageRatioField(verbose_name="Обрезка изображения (большие экраны)", image_field='image', size="200x223")
    crop_mini = ImageRatioField(verbose_name="Обрезка изображения (маленькие экраны)", image_field='image', size="106x118")
    sorting = models.PositiveIntegerField("Сортировка", help_text="Цитаты будут расположены согласно данной сортировке", default=0)

    def __str__(self):
        return self.author if self.author else self.quote

    class Meta:
        ordering = ('-sorting',)
        verbose_name = "Цитата"
        verbose_name_plural = "Цитаты"


class MetroStation(models.Model):
    line_color = models.CharField("Цвет ветки (hexadecimal)", max_length=20)
    line_name = models.CharField("Название ветки", max_length=100)
    position_in_line = models.IntegerField("Позиция на линии")
    station_name = models.CharField("Название станции", max_length=100)

    def __str__(self):
        return f"{self.station_name} — {self.line_name}"

    class Meta:
        verbose_name = "Станция метро"
        verbose_name_plural = "Станции метро"


class Settings(models.Model):
    name = models.CharField("Название", max_length=200)
    description = models.CharField("Описание", max_length=1000)
    key = models.CharField("Ключ", max_length=200)
    value = models.TextField("Значение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

class CeoSettings(models.Model):
    template_name = models.CharField("Название шаблона", max_length=200, unique=True)
    title = models.CharField("Заголовок", help_text="Оставьте поле пустым, чтобы использовать информацию из шаблона base.html", max_length=200, default="", blank=True)
    title_postfix = models.BooleanField("Включить постфикс (дополнение к заголовку с конца)", default=True)
    meta_description = models.CharField("Описание (мета-тег)", help_text="Оставьте поле пустым, чтобы использовать информацию из шаблона base.html",
                                        max_length=1000, null=True, blank=True)
    meta_keywords = models.CharField("Ключевые слова (мета-тег)", help_text="Оставьте поле пустым, чтобы использовать информацию из шаблона base.html",
                                     max_length=500, null=True, blank=True)
    meta_robots = models.CharField("Robots (мета-тег)", help_text="Оставьте поле пустым, чтобы использовать информацию из шаблона base.html",
                                   max_length=500, null=True, blank=True)
    has_custom_title = models.BooleanField("Имеет динамический (создаётся согласно контенту) заголовок", default=False)

    def __str__(self):
        return self.template_name

    def admin_title(self):
        return self.title if self.title else self.template_name
    admin_title.short_description = "Название"

    def admin_postfix(self):
        return self.title_postfix
    admin_postfix.boolean = title_postfix
    admin_postfix.short_description = "Включить постфикс"

    def has_meta_description(self):
        return bool(self.meta_description)
    has_meta_description.short_description = "мета тег \"Описание\""
    has_meta_description.boolean = bool(meta_description)

    def has_meta_keywords(self):
        return bool(self.meta_keywords)
    has_meta_keywords.short_description = "мета тег \"Ключевые слова\""
    has_meta_keywords.boolean = bool(meta_keywords)

    def has_meta_robots(self):
        return bool(self.meta_robots)
    has_meta_robots.short_description = "мета тег \"Robots\""
    has_meta_robots.boolean = bool(meta_robots)

    class Meta:
        verbose_name = "CEO настройки страницы"
        verbose_name_plural = "CEO настройки страниц"


class City(models.Model):
    name = models.CharField("Название города", max_length=200)
    youtube_link = models.CharField("Ссылка на ютуб канал (для данного города)", help_text="Оставьте поле пустым, чтобы использовать общие ссылки", max_length=100, null=True,
                                    blank=True)
    facebook_link = models.CharField("Ссылка на страницу Фейсбука", help_text="Оставьте поле пустым, чтобы использовать общие ссылки", max_length=100, null=True, blank=True)
    instagram_link = models.CharField("Ссылка на Инстаграм профиль", help_text="Оставьте поле пустым, чтобы использовать общие ссылки", max_length=100, null=True, blank=True)
    vk_link = models.CharField("Ссылка на страницу Вконтакте", help_text="Оставьте поле пустым, чтобы использовать общие ссылки", max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def filled_id(self):
        return str(self.id).zfill(2)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Branch(models.Model):
    name = models.CharField("Название филиала", max_length=200)
    moscow_metro_station = models.ForeignKey(verbose_name="Метро (список, только для Москвы)", to=MetroStation, on_delete=models.DO_NOTHING, null=True, blank=True)
    custom_metro_station = models.CharField(verbose_name="Метро (ручной ввод)", max_length=400, null=True, blank=True,
                                            help_text="Оставьте поле пустым, чтобы отображать выбранную из списка станцию метро")
    city = models.ForeignKey(verbose_name="Город", to=City, on_delete=models.DO_NOTHING)
    description = models.CharField("Описание", max_length=4000, null=True, blank=True)
    address = models.CharField("Адрес", max_length=400)
    website = models.CharField("Сайт филиала", max_length=300, null=True, blank=True)
    email = models.EmailField("Email филиала", max_length=200, null=True, blank=True)
    phone = models.CharField("Телефон", max_length=50, null=True, blank=True)
    geocode_lat = models.FloatField("Гео-код (Широта)")
    geocode_lon = models.FloatField("Гео-код (Долгота)")

    def __str__(self):
        return f"{self.name} — {self.address}"

    def title(self):
        return self.name

    def instructors(self):
        return self.staff_set.filter(position__contains="single-coach")

    def filled_id(self):
        return str(self.id).zfill(2)

    def metro(self):
        return self.custom_metro_station if self.custom_metro_station else self.moscow_metro_station if self.moscow_metro_station else None

    def trainers(self):
        return self.staff_set[:3]

    def website_link(self):
        if not self.website:
            return ""
        return self.website if self.website.startswith("http") else f"http://{self.website}"

    class Meta:
        ordering = [Left('name', 1), Length('name'), 'name']
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"
