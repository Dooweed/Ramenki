from django.contrib import admin
from image_cropping import ImageCroppingMixin
from adminsortable2.admin import SortableAdminMixin
from django import forms
from .models import *
from django.db.models.functions import Length

# Register your models here.

admin.site.site_header = "Спортклуб Раменки"


class MetroStationAdmin(admin.ModelAdmin):
    ordering = ("station_name", "line_name")
    search_fields = ("station_name", "line_name")
    list_display = ("station_name", "line_name")

class CityAdmin(admin.ModelAdmin):
    list_display = ("name", )
    fieldsets = (
        (None, {'fields': ('name', )}),
        ('Социальные сети', {'fields': ('youtube_link', 'facebook_link', 'instagram_link', 'vk_link')}),
    )

class BranchForm(forms.ModelForm):
    class Meta:
        fields = ("name", "no", "moscow_metro_station", "custom_metro_station", "city", "description", "address", "website", "email", "phone", "geocode_lat", "geocode_lon")
        widgets = {
            "description": forms.Textarea(),
        }

class BranchAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "website", "city", "address", "email", "phone")
    autocomplete_fields = ("moscow_metro_station",)
    fieldsets = (
        (None, {'fields': ("name", "city", "moscow_metro_station", "custom_metro_station", "description", "address", "website")}),
        ('Геокод (геопозиция)', {'fields': ('geocode_lat', 'geocode_lon'), 'description': 'Используется для определения центра карты этого города'}),
        ('Контактные данные', {'fields': ("email", "phone")}),
    )

    form = BranchForm

class SliderItemForm(forms.ModelForm):
    class Meta:
        fields = ("header", "body", "image", "crop_mobile", "crop_tablet", "crop_index", "crop_wide")
        widgets = {
            'header': forms.Textarea(attrs={"style": "width: 400px; height: 34px;"}),
            'body': forms.Textarea(attrs={"style": "width: 400px; height: 68px;"}),
        }
        model = SliderItem


class SliderItemAdmin(ImageCroppingMixin, SortableAdminMixin, admin.ModelAdmin):
    list_display = ["header", "body", "active", "sorting"]
    form = SliderItemForm

class MiniSliderItemAdmin(ImageCroppingMixin, SortableAdminMixin, admin.ModelAdmin):
    list_display = ["author", "description", "quote", "active", "sorting"]

class SettingsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)
        self.fields['value'].strip = False

    class Meta:
        fields = "__all__"

class SettingsAdmin(admin.ModelAdmin):
    list_display = ("name", "key", "value")
    readonly_fields = ("key", "name", "description")

    form = SettingsForm

    def render_change_form(self, request, context, *args, **kwargs):
        self.change_form_template = 'admin/static_pages/change_form_help_text.html'
        extra = {'help_text': "<b>Внимание!</b> Удаление настроек может привести к потере части фукнционала, крайне не рекомендуется УДАЛЯТЬ настройки.", }
        context.update(extra)
        return super(SettingsAdmin, self).render_change_form(request, context, *args, **kwargs)

class CeoSettingsForm(forms.ModelForm):
    class Meta:
        fields = ("template_name", "title", "title_postfix", "meta_description", "meta_keywords")
        widgets = {
            'title': forms.Textarea(attrs={"style": "width: 400px; height: 34px;"}),
            'meta_keywords': forms.Textarea(attrs={"style": "width: 400px; height: 34px;"}),
            'meta_robots': forms.Textarea(attrs={"style": "width: 400px; height: 34px;"}),
            'meta_description': forms.Textarea(attrs={"style": "width: 400px; height: 68px;"}),
        }

class CeoSettingsAdmin(admin.ModelAdmin):
    list_display = ("admin_title", "template_name", "admin_postfix", "has_meta_description", "has_meta_keywords", "has_meta_robots")
    fieldsets = (
        (None, {"fields": ("template_name", )}),
        ("Заголовок", {"fields": ("title", "title_postfix")}),
        ("Мега-теги", {"fields": ("meta_robots", "meta_keywords", "meta_description")})
    )
    form = CeoSettingsForm

    def render_change_form(self, request, context, *args, **kwargs):
        self.change_form_template = 'admin/static_pages/change_form_help_text.html'
        obj = context.get("original")
        if obj and obj.has_custom_title:
            extra = {'help_text': "<b>Внимание!</b> Эта запись имеет динамический заголовок (заголовок создаётся согласно контенту). Заполните поле \"Заголовок\" чтобы "
                                  "переопределить значение динамического заголовка.",
                     'color_main': 'rgb(255,193,7)',
                     'color_back': 'rgba(255,193,7, 0.5)',
                     'color_font': '#343A40'}
            context.update(extra)
        return super(CeoSettingsAdmin, self).render_change_form(request, context, *args, **kwargs)


admin.site.register(CeoSettings, CeoSettingsAdmin)
admin.site.register(Settings, SettingsAdmin)
admin.site.register(MiniSliderItem, MiniSliderItemAdmin)
admin.site.register(SliderItem, SliderItemAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(MetroStation, MetroStationAdmin)
admin.site.register(Branch, BranchAdmin)
