from django.contrib import admin
from django import forms
from django.contrib import messages
from django.utils.translation import ngettext
from image_cropping import ImageCroppingMixin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *

# Register your models here.

class ArticleForm(forms.ModelForm):
    class Meta:
        fields = ("title", "url", "short_text", "meta_description", "status", "associations", "date", "text", "image", "thumbnail_size", "article_size")
        widgets = {
            'title': forms.Textarea(attrs={"style": "width: 400px; height: 34px;"}),
            'short_text': forms.Textarea(attrs={"style": "width: 400px; height: 68px;"}),
            'text': CKEditorUploadingWidget(),
            "meta_description": forms.Textarea(attrs={"style": "width: 400px; height: 68px;"}),
        }
        model = Article


class ArticleAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("title", "status", "url", "has_image", "date", "short_text", "categories")
    search_fields = ("title", "status", "short_text")
    list_editable = ("status",)
    actions = ("make_published", 'make_pending', 'make_editing')
    prepopulated_fields = {'url': ('title',), }
    form = ArticleForm

    def make_published(self, request, queryset):
        updated = queryset.update(status='published')
        self.message_user(request, ngettext(
            '%d статья была успешно опубликована.',
            '%d статей были успешно опубликованы.',
            updated,
        ) % updated, messages.SUCCESS)
    make_published.short_description = "Опубликовать"

    def make_pending(self, request, queryset):
        updated = queryset.update(status='pending')
        self.message_user(request, ngettext(
            '%d статья была успешно переведена в режим ожидания.',
            '%d статей были успешно переведены в режим ожидания.',
            updated,
        ) % updated, messages.SUCCESS)
    make_pending.short_description = "Перевести в режим ожидания"

    def make_editing(self, request, queryset):
        updated = queryset.update(status='editing')
        self.message_user(request, ngettext(
            '%d статья была успешно переведена в режим редактирования.',
            '%d статей были успешно переведены в режим редактирования.',
            updated,
        ) % updated, messages.SUCCESS)
    make_editing.short_description = "Перевести в режим редактирования"

class ArticleCategoryForm(forms.ModelForm):
    class Meta:
        fields = ("name", "url", "active", "meta_description")
        widgets = {
            "meta_description": forms.Textarea(attrs={"style": "width: 400px; height: 68px;"}),
        }

class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "active")
    search_fields = ("name", "url")
    prepopulated_fields = {'url': ('name',), }
    list_editable = ("active", )
    form = ArticleCategoryForm


admin.site.register(ArticleCategory, ArticleCategoryAdmin)
admin.site.register(Article, ArticleAdmin)
