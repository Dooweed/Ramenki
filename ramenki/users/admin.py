from django.contrib import admin
from django import forms
from datetime import datetime
from .models import Staff, CustomUser, Profile
from ckeditor.widgets import CKEditorWidget
from image_cropping import ImageCroppingMixin
from django.db.models import TextField
from social_django.models import UserSocialAuth, Nonce, Association
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(UserSocialAuth)
admin.site.unregister(Nonce)
admin.site.unregister(Association)


# Register your models here.

def get_years_choices():
    year = datetime.now().year
    choices = [(None, "Не указано")]
    for i in range(1950, year):
        choices.append((i, i))
    return choices


class StaffForm(forms.ModelForm):
    class Meta:
        fields = ("name", "position", "active", "short_description", "sports_kind", "branch", "birth_date", "qualification", "started_trainings", "weight", "veteran", "photo",
                  "photo_profile", "photo_avatar", "additional_information", "merits", "sorting")
        widgets = {
            "birth_date": forms.SelectDateWidget(years=range(1900, datetime.now().year + 1)),
            "started_trainings": forms.Select(choices=get_years_choices()),
            'short_description': forms.Textarea(attrs={"style": "width: 400px; height: 68px;"}),
            "additional_information": CKEditorWidget,
            "merits": CKEditorWidget,
        }
        help_texts = {
            'edit_user': "Имя, фамилия, телефон, Email и пароль хранятся в параметрах Аккаунта. Измените аккаунт чтобы изменить эти данные в профиле",
        }


class StaffAdmin(ImageCroppingMixin, admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ("name", "position", "active", "short_description", "branch", "birth_date")
        }),
        ("Спортивная информация", {
            'fields': ("sports_kind", "qualification", "started_trainings", "weight", "veteran")
        }),
        ("Изображение профиля", {
            'fields': ("photo", "photo_profile", "photo_avatar")
        }),
        ("Дополнительно", {
            'fields': ("additional_information", "merits", "sorting")
        }),
    )
    ordering = ("sorting", "position")
    search_fields = ("name", "position")
    list_display = ("name", "verbose_position", "verbose_sports_kinds", "sorting", "birth_date")
    list_editable = ("sorting",)
    form = StaffForm


class ProfileForm(forms.ModelForm):
    class Meta:
        fields = ("user", "patronymic", "birth_date", "coach", "budo_pass", "qualification_type", "qualification_number", "photo", "avatar_cut", "use_social_photo", "social_photo",
                  "social_avatar", "odnoklassniki", "facebook", "instagram", "vkontakte")
        widgets = {
            "birth_date": forms.SelectDateWidget(years=range(1900, datetime.now().year + 1)),
            "social_photo": forms.TextInput(attrs={"style": "width: 500px; max-width: 100%;"}),
            "social_avatar": forms.TextInput(attrs={"style": "width: 500px; max-width: 100%;"}),

        }


class ProfileInlineAdmin(admin.StackedInline):
    model = Profile
    formfield_overrides = {
        TextField: {'widget': forms.TextInput(attrs={"style": "width: 500px; max-width: 100%;"})},
    }
    form = ProfileForm
    fieldsets = (
        ("Личная информация", {
            'fields': ("patronymic", "birth_date")
        }),
        ("Спортивная информация", {
            'fields': ("coach", "budo_pass", "qualification_type", "qualification_number")
        }),
        ("Изображение профиля", {
            'fields': ("photo", "avatar_cut", "use_social_photo", "social_photo", "social_avatar")
        }),
        ("Социальные сети", {
            'fields': ("odnoklassniki", "facebook", "instagram", "vkontakte")
        }),
    )


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "forename", "surname", "phone", "is_staff", "is_active")
    fieldsets = (
        ("Общая информация", {
            'fields': ("email", "password", "forename", "surname", "phone"),
        }),
        ("Разрешения", {
            'fields': ("is_staff", "is_active", "is_superuser", "groups", "user_permissions"),
        }),
    )
    ordering = ("email", )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("forename", "surname", 'email', 'password1', 'password2'),
        }),
    )

    def get_inlines(self, request, obj):
        if not obj:
            return super().get_inlines(request, obj)
        else:
            return [ProfileInlineAdmin]


class ProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
    # inline_type = 'stacked'
    # inline_reverse = [('user', {'fields': ("email", "password", "forename", "surname", "phone", "is_staff", "is_active")}), ]
    list_display = ("full_name", "coach", "budo_pass", "qualification", "age_and_date", "has_photo")
    model = Profile
    form = ProfileForm
    readonly_fields = ("edit_user",)
    fieldsets = (
        ("Личная информация", {
            'fields': ("edit_user", "patronymic", "birth_date"),
        }),
        ("Спортивная информация", {
            'fields': ("coach", "budo_pass", "qualification_type", "qualification_number"),
        }),
        ("Изображение профиля", {
            'fields': ("photo", "avatar_cut", "use_social_photo", "social_photo", "social_avatar"),
        }),
        ("Социальные сети", {
            'fields': ("odnoklassniki", "facebook", "instagram", "vkontakte"),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Staff, StaffAdmin)
