from django.db import models
from ramenki.static_vars import CONDITIONS, MONTHS, ARTICLE_DESCRIPTION_LENGTH
from image_cropping import ImageRatioField
from django.utils import timezone
from datetime import timedelta
from ramenki.utils import category_url_validator, get_ending
from autoslug import AutoSlugField
from django.utils.html import strip_tags

# Create your models here.

class ArticleCategory(models.Model):
    name = models.CharField("Название категории", max_length=50, unique=True)
    url = AutoSlugField(verbose_name="URL категории", unique=True, populate_from='name', editable=True, validators=(category_url_validator, ))
    active = models.BooleanField("Активно", help_text="Неактивные категории не будут отображаться в списке категорий", default=True)
    meta_description = models.CharField("Описание (мета-тег)", help_text="Оставьте поле пустым, чтобы использовать информацию из шаблона news.html",
                                        max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория статей"
        verbose_name_plural = "Категории статей"

class Article(models.Model):
    title = models.CharField("Заголовок статьи", max_length=500)
    url = AutoSlugField(verbose_name="URL статьи", unique=True, populate_from='title', editable=True)
    text = models.TextField("Текст статьи")
    status = models.CharField("Состояние статьи", help_text="Отображаться будут только статьи с состоянием \"Выпущено\"", default="editing", max_length=30, choices=CONDITIONS)
    short_text = models.CharField("Краткая информация о статье", help_text="Информация для превью статьи (необязательно)", max_length=500, null=True, blank=True)
    image = models.ImageField("Изображение статьи", help_text="Возможность обрезки появится после сохранения", upload_to="articles/", null=True, blank=True)
    associations = models.ManyToManyField(verbose_name="Категории", to=ArticleCategory, blank=True)
    date = models.DateTimeField("Дата создания")
    meta_description = models.CharField("Описание (мета-тег)", help_text="Оставьте поле пустым, чтобы использовать первые 250 знаков статьи",
                                        max_length=1000, null=True, blank=True)

    thumbnail_size = ImageRatioField(verbose_name="Обрезка изображения для превью", image_field='image', size="288x276")
    article_size = ImageRatioField(verbose_name="Обрезка изображения для статьи", image_field='image', free_crop=True)

    def __str__(self):
        return self.title

    def get_meta_description(self):
        return self.meta_description if self.meta_description else strip_tags(self.text[:500])[:250]

    def description(self, length=ARTICLE_DESCRIPTION_LENGTH):
        if self.short_text:
            return strip_tags(self.short_text)
        else:
            short_text = strip_tags(self.text[:length*2])[:length]
            index = short_text.rfind(" ")
            if index == -1:
                return f"{short_text}..."
            else:
                return f"{short_text[:index]}..."

    def has_image(self):
        return bool(self.image)
    has_image.short_description = "Наличие изображения"
    has_image.boolean = bool(image)

    def categories(self):
        associations = self.associations.all()
        categories_string = f"({associations.count()}) "
        for category in associations:
            categories_string = f"{categories_string}, {category.name}"

    def active(self):
        return self.status == "active"

    def date_string(self):
        if timezone.now().year == self.date.year:
            if self.date > timezone.now() - timedelta(days=1):
                hours = round((timezone.now() - self.date).seconds/3600)
                if hours == 0:
                    return "Менее часа назад"
                else:
                    return f"{get_ending(hours, ('час', 'часа', 'часов'))} назад"
            else:
                date_string = self.date.strftime("%d {}")
                return date_string.format(MONTHS[self.date.month])
        else:
            date_string = self.date.strftime("%d {} %Y")
            return date_string.format(MONTHS[self.date.month])

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
