from django.db import models
from image_cropping import ImageRatioField
from ramenki.utils import category_url_validator, get_ending
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.utils.html import mark_safe

# Create your models here.

class MediaCategory(models.Model):
    name = models.CharField("Название категории", max_length=50, unique=True)
    url = AutoSlugField(verbose_name="URL категории", unique=True, populate_from="name", editable=True, validators=(category_url_validator, ))
    active = models.BooleanField("Активно", help_text="Неактивные категории не будут отображаться в списке категорий", default=True)
    meta_description = models.CharField("Описание (мета-тег)", help_text="Оставьте поле пустым, чтобы использовать информацию из шаблона news.html",
                                        max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name

    def has_photo_galleries(self):
        return bool(self.photogallery_set)

    class Meta:
        verbose_name = "Категория медиа"
        verbose_name_plural = "Категории медиа"

class Photo(models.Model):
    name = models.CharField("Название фото", max_length=500, null=True, blank=True)
    image = models.ImageField("Фото", upload_to="photos/")
    gallery = models.ForeignKey(verbose_name="Галерея", to="PhotoGallery", on_delete=models.CASCADE)
    date = models.DateTimeField("Дата добавления", auto_now_add=True)

    def __str__(self):
        return self.name if self.name else self.image.name

    def get_name(self):
        if self.name:
            name = self.name
        else:
            name = self.image.name.split("/")[-1]
            name = name[:name.rfind(".")]
        return name

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

class PhotoGallery(models.Model):
    name = models.CharField("Название галереи", max_length=500)
    thumbnail = models.ImageField("Обложка галереи", upload_to=f'photo-galleries/{slugify(name)}', help_text="Возможность обрезки появится после сохранения")
    use_raw_thumbnail = models.BooleanField("Использовать оригинальное фото обложки (без обрезки)", default=True)
    crop = ImageRatioField(verbose_name="Обрезка изображения для обложки", image_field='thumbnail', size="448x276")
    category = models.ForeignKey(verbose_name="Категории", to=MediaCategory, on_delete=models.DO_NOTHING, null=True, blank=True)
    date = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.name

    def length(self):
        return get_ending(Photo.objects.filter(gallery=self).count(), ("фотография", "фотографии", "фотографий"))
    length.short_description = "Размер галереи"

    def has_thumbnail(self):
        return bool(self.thumbnail)
    has_thumbnail.short_description = "Имеет обложку"
    has_thumbnail.boolean = bool(thumbnail)

    class Meta:
        verbose_name = "Фото-галерея"
        verbose_name_plural = "Фото-галереи"

class Video(models.Model):
    name = models.CharField("Название видео", max_length=500)
    description = models.CharField("Описание видео", max_length=5000, help_text="Необязательно", null=True, blank=True)
    category = models.ForeignKey(verbose_name="Категории", to=MediaCategory, on_delete=models.DO_NOTHING, null=True, blank=True)
    link = models.CharField("Ссылка на видео", max_length=200, help_text="Ссылку можно получить нажав \"Поделиться\" под видео")
    thumbnail = models.ImageField("Обложка видео", upload_to=f'video-thumbnails/', help_text="Возможность обрезки появится после сохранения", blank=True, null=True)
    use_raw_thumbnail = models.BooleanField("Использовать оригинальное фото обложки (без обрезки)", default=True)
    crop = ImageRatioField(verbose_name="Обрезка изображения для обложки", image_field='thumbnail', size="448x276")
    date = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.name

    def has_description(self):
        return bool(self.description)
    has_description.short_description = "Имеет описание"
    has_description.boolean = bool(description)

    def clickable_link(self):
        return mark_safe(f'<a href="{self.link}">{self.link}</a>')
    clickable_link.short_description = "Ссылка на видео"

    def youtube_thumbnail(self):
        return f"""https://img.youtube.com/vi/{self.link.split("/")[-1]}/hqdefault.jpg"""

    def has_thumbnail(self):
        return bool(self.thumbnail)
    has_thumbnail.short_description = "Имеет обложку"
    has_thumbnail.boolean = bool(thumbnail)

    def embed_tag(self):
        return f'<iframe width="560" height="315" src="https://www.youtube.com/embed/{self.link.split("/")[-1]}" frameborder="0" allow="accelerometer; autoplay; ' \
               f'encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'

    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Видео"
