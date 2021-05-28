from django.contrib import admin
from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget
from adminsortable2.admin import SortableAdminMixin


# Register your models here.

class StaticPageForm(forms.ModelForm):
    class Meta:
        fields = ("title", "url", "active", "title_tag", "meta_tag", "meta_keywords_tag", "image", "sorting", "content")
        widgets = {
            "content": CKEditorUploadingWidget()
        }


class AboutPageForm(forms.ModelForm):
    class Meta:
        fields = ("title", "url", "active", "title_tag", "meta_tag", "meta_keywords_tag", "image", "sorting", "content", "additional_content_left", "additional_content_right")
        widgets = {
            "content": CKEditorUploadingWidget(),
            "additional_content_left": CKEditorWidget(),
            "additional_content_right": CKEditorWidget(),
        }


class StaticPageAdmin(SortableAdminMixin, admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("title", "url", "active", "sorting")
    prepopulated_fields = {'url': ('title',), }
    form = StaticPageForm

    def render_change_form(self, request, context, *args, **kwargs):
        self.change_form_template = 'admin/static_pages/change_form_help_text.html'
        obj = context.get("original")
        if obj and obj.custom_database_query:
            extra = {'help_text': "<b>Внимание!</b> Этот подраздел имеет уникальный функционал. Крайне не рекомендуется удалять страницу или изменять её URL "
                                  "(изменение URL приведёт к потере доступа к уникальному функционалу в этом подразделе). Сохраняйте html структуру контента при редактировании "
                                  "подраздела.", }
            context.update(extra)
        return super(StaticPageAdmin, self).render_change_form(request, context, *args, **kwargs)


class KarateStaticPageAdmin(StaticPageAdmin):
    model = KarateStaticPage


class TaekwondoStaticPageAdmin(StaticPageAdmin):
    model = TaekwondoStaticPage


class AboutStaticPageAdmin(StaticPageAdmin):
    model = AboutStaticPage
    form = AboutPageForm


admin.site.register(KarateStaticPage, KarateStaticPageAdmin)
admin.site.register(TaekwondoStaticPage, TaekwondoStaticPageAdmin)
admin.site.register(AboutStaticPage, AboutStaticPageAdmin)
