from django.db import models
from autoslug import AutoSlugField


# Create your models here.

class AboutStaticPage(models.Model):
    title = models.CharField("Название подраздела", max_length=200)
    url = AutoSlugField(verbose_name="URL подраздела", populate_from='title', unique=True, editable=True, blank=True)
    active = models.BooleanField("Страница активна", default=True, help_text="Неактивные страницы не будут отображаться в списке подразделов")
    custom_database_query = models.BooleanField("Имеет уникальный запрос в базу данных", default=False,
                                                help_text="Крайне не рекомендуется удалять страницы с уникальным запросом в базу данных")
    title_tag = models.CharField("Содержимое тега <title>", help_text="Оставьте поле пустым, чтобы использовать название подраздела как заголовок страницы", max_length=300, null=True, blank=True)
    meta_tag = models.CharField("Содержимое тега <meta name=\"description\">", help_text="Оставьте поле пустым, чтобы использовать метатег description базового шаблона", max_length=2000, null=True, blank=True)
    meta_keywords_tag = models.CharField("Содержимое тега <meta name=\"keywords\">", help_text="Оставьте поле пустым, чтобы использовать метатег keywords базового шаблона", max_length=500, null=True, blank=True)
    meta_robots_tag = models.CharField("Содержимое тега <meta name=\"robots\">", help_text="Оставьте поле пустым, чтобы использовать метатег robots базового шаблона", max_length=500, null=True, blank=True)
    image = models.ImageField("Изображение статьи", help_text="Возможность обрезки появится после сохранения", upload_to="static-pages/about/")
    content = models.TextField("Контент страницы", help_text="Перетащите изображение в редактор, чтобы загрузить его на сервер", null=True, blank=True)
    additional_content_left = models.TextField("Дополнительный контент страницы (левая часть)", null=True, blank=True,
                                               help_text="Дополнительный контент расположен под списком подразделов (слева)")
    additional_content_right = models.TextField("Дополнительный контент страницы (правая часть)", null=True, blank=True,
                                                help_text="Дополнительный контент расположен прямо под основным контентом (справа)")
    sorting = models.PositiveIntegerField("Сортировка", help_text="Подразделы будут появляться в списке раздела согласно данной сортировке", default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-sorting', )
        verbose_name = "Страница раздела \"О клубе\""
        verbose_name_plural = "Страницы раздела \"О клубе\""


class KarateStaticPage(models.Model):
    title = models.CharField("Название подраздела", max_length=200)
    url = AutoSlugField(verbose_name="URL подраздела", populate_from='title', unique=True, editable=True, blank=True)
    active = models.BooleanField("Страница активна", default=True, help_text="Неактивные страницы не будут отображаться в списке подразделов")
    custom_database_query = models.BooleanField("Имеет уникальный запрос в базу данных", default=False,
                                                help_text="Крайне не рекомендуется удалять страницы с уникальным запросом в базу данных")
    title_tag = models.CharField("Содержимое тега <title>", help_text="Оставьте поле пустым, чтобы использовать название подраздела как заголовок страницы", max_length=300, null=True, blank=True)
    meta_tag = models.CharField("Содержимое тега <meta name=\"description\">", help_text="Оставьте поле пустым, чтобы использовать метатег description базового шаблона", max_length=4000, null=True, blank=True)
    meta_keywords_tag = models.CharField("Содержимое тега <meta name=\"keywords\">", help_text="Оставьте поле пустым, чтобы использовать метатег keywords базового шаблона", max_length=500, null=True, blank=True)
    meta_robots_tag = models.CharField("Содержимое тега <meta name=\"robots\">", help_text="Оставьте поле пустым, чтобы использовать метатег robots базового шаблона", max_length=500, null=True, blank=True)
    image = models.ImageField("Изображение статьи", help_text="Возможность обрезки появится после сохранения", upload_to="static-pages/karate/", null=True, blank=True)
    content = models.TextField("Контент страницы", help_text="Перетащите изображение в редактор, чтобы загрузить его на сервер")
    sorting = models.PositiveIntegerField("Сортировка", help_text="Подразделы будут появляться в списке раздела согласно данной сортировке", default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-sorting', )
        verbose_name = "Страница раздела \"Карате\""
        verbose_name_plural = "Страницы раздела \"Карате\""


class TaekwondoStaticPage(models.Model):
    title = models.CharField("Название подраздела", max_length=200)
    url = AutoSlugField(verbose_name="URL подраздела", populate_from='title', unique=True, editable=True, blank=True)
    active = models.BooleanField("Страница активна", default=True, help_text="Неактивные страницы не будут отображаться в списке подразделов")
    custom_database_query = models.BooleanField("Имеет уникальный запрос в базу данных", default=False,
                                                help_text="Крайне не рекомендуется удалять страницы с уникальным запросом в базу данных")
    title_tag = models.CharField("Содержимое тега <title>", help_text="Оставьте поле пустым, чтобы использовать название подраздела как заголовок страницы", max_length=300, null=True, blank=True)
    meta_tag = models.CharField("Контент тега <meta name=\"description\">", help_text="Оставьте поле пустым, чтобы использовать метатег description базового шаблона", max_length=4000, null=True, blank=True)
    meta_keywords_tag = models.CharField("Содержимое тега <meta name=\"keywords\">", help_text="Оставьте поле пустым, чтобы использовать метатег keywords базового шаблона", max_length=500, null=True, blank=True)
    meta_robots_tag = models.CharField("Содержимое тега <meta name=\"robots\">", help_text="Оставьте поле пустым, чтобы использовать метатег robots базового шаблона", max_length=500, null=True, blank=True)
    image = models.ImageField("Изображение статьи", help_text="Возможность обрезки появится после сохранения", upload_to="static-pages/taekwondo/", null=True, blank=True)
    content = models.TextField("Контент страницы", help_text="Перетащите изображение в редактор, чтобы загрузить его на сервер")
    sorting = models.PositiveIntegerField("Сортировка", help_text="Подразделы будут появляться в списке раздела согласно данной сортировке", default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-sorting', )
        verbose_name = "Страница раздела \"Тхэквондо\""
        verbose_name_plural = "Страницы раздела \"Тхэквондо\""
