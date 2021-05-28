from django import forms
from users.models import CustomUser, Profile
from datetime import datetime

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("forename", "surname", "email", "phone", "password")
        widgets = {
            "forename": forms.TextInput(attrs={"class": "field-text__input"}),
            "surname": forms.TextInput(attrs={"class": "field-text__input"}),
            "email": forms.EmailInput(attrs={"class": "field-text__input"}),
            "phone": forms.TextInput(attrs={"class": "field-text__input"}),
            "password": forms.PasswordInput(attrs={"class": "field-text__input"}),
        }


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "field-text__input"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "field-text__input"}), max_length=100)

class EditCustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ("forename", "surname", "email", "phone")

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("patronymic", "birth_date", "coach", "budo_pass", "qualification_type", "qualification_number", "photo", "avatar_cut",
                  "odnoklassniki", "facebook", "instagram", "vkontakte", "use_social_photo")
        widgets = {
            "birth_date": forms.SelectDateWidget(years=range(1900, datetime.now().year + 1)),
            "photo": forms.FileInput(),
        }
