from django import forms
from django.forms import widgets
from .models import User, Product, ProductImage

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result

class ProductForm(forms.Form):
    title = forms.CharField(label='Название')
    description = forms.CharField(widget=forms.Textarea, label='Описание')
    category = forms.ChoiceField(choices=Product.category_choices, label='Категория')
    count = forms.IntegerField(label='Количество')
    price = forms.FloatField(label='Цена')

class ProductImageForm(forms.Form):
    photos = MultipleFileField()

    def clean_photos(self):
        # Остаются только картинки
        photos = [photo for photo in self.request.FILES.getlist('photos') if 'image' in photo.content_type]
        # Если среди загруженных файлов картинок нет, то исключение
        if len(photos) == 0:
            raise forms.ValidationError(u'Not found uploaded photos.')
        return photos

    def save_for(self, product):
        for photo in self.cleaned_data['photos']:
            ProductImage(photo=photo, product=product).save()
