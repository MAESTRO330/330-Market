from django import forms
from django.forms import widgets
from .models import User, Product, ProductImage

class ProductForm(forms.Form):
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageForm(forms.Form):
    photos = forms.FileField(widget=widgets.FileInput(attrs={'multiple': True}))

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
