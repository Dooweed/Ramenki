from django import forms
from .models import PhotoGallery, Photo
from django.core.validators import validate_image_file_extension
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import io
from transliterate import translit

class PhotoGalleryAdminForm(forms.ModelForm):
    class Meta:
        model = PhotoGallery
        exclude = ("photos", )

    class Media:
        js = ('js/select_all_button.js', )

    images = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label="Добавить сразу несколько изображений",
        required=False,
    )
    size_restriction = forms.IntegerField(
        label="Ограничение по размеру",
        help_text="Ограничение по размеру применяется к наибольшей стороне изображения. Оставьте поле пустым чтобы оставить изображения в исходном размере",
        min_value=0,
        required=False)

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("images"):
            validate_image_file_extension(upload)

    def save_photos(self, gallery):
        """Process each uploaded image."""
        if 'size_restriction' in self.cleaned_data:
            size_restriction = self.cleaned_data['size_restriction']
        else:
            size_restriction = None
        for upload in self.files.getlist("images"):
            upload.name = translit(upload.name, 'ru', reversed=True)
            if size_restriction:
                image = Image.open(upload)
                w, h = image.size
                if w > size_restriction or h > size_restriction:
                    if w > h:
                        image = image.resize((size_restriction, int(size_restriction*(h/w))), Image.ANTIALIAS)
                    else:
                        image = image.resize((int(size_restriction*(w/h)), size_restriction), Image.ANTIALIAS)
                    output = io.BytesIO()
                    image.save(output, format=upload.content_type.split("/")[-1])
                    output.seek(0)
                    upload = InMemoryUploadedFile(output, None, upload.name, upload.content_type,
                                                  output.tell(), upload.charset, upload.content_type_extra)
            image_obj = Photo(gallery=gallery, image=upload)
            image_obj.save()
