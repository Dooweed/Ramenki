from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget
from image_cropping import ImageCroppingMixin
from django import forms
from .forms import PhotoGalleryAdminForm

# Register your models here.

class VideoForm(forms.ModelForm):
    class Meta:
        fields = ("name", "description", "category", "link", "thumbnail", "crop")
        widgets = {
            'description': CKEditorWidget(),
        }
        model = Video

class VideoAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("name", "clickable_link", "has_description", "has_thumbnail", "category")
    search_fields = ("name", "description")
    form = VideoForm

class PhotoInlineAdmin(admin.StackedInline):
    model = Photo
    extra = 0
    fields = (("image", "name"),)

class PhotoGalleryAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("name", "has_thumbnail", "length", "category")
    search_fields = ("name", )
    fieldsets = (
        (None, {'fields': ("name", "category")}),
        ('Обложка', {'fields': ('thumbnail', 'use_raw_thumbnail', 'crop')}),
        ('Мультизагрузка изображений', {'fields': ('images', 'size_restriction')})
    )
    inlines = [PhotoInlineAdmin]
    form = PhotoGalleryAdminForm
    save_on_top = True

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)

class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "url", "active")
    search_fields = ("name", "url")
    prepopulated_fields = {'url': ('name',), }
    list_editable = ("active", )


admin.site.register(Photo)
admin.site.register(MediaCategory, MediaCategoryAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(Video, VideoAdmin)
