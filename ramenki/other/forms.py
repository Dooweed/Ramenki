from django import forms

class CallbackForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "field-text__input", "placeholder": "имя"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "field-text__input", "placeholder": "email", "novalidate": ""}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class": "field-text__input", "placeholder": "Ваше сообщение", "rows": "5"}), max_length=4000)

    city_id = forms.IntegerField(widget=forms.HiddenInput)
    branch_id = forms.IntegerField(widget=forms.HiddenInput)
