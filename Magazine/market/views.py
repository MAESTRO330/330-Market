from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ProductForm, ProductImageForm

# Create your views here.

class NewProduct(View):
    def get(self, request):
        form = ProductForm()
        form_img = ProductImageForm()
        return render(request, 'new_product.html', context={'form':form, 'form_img':form_img})
    
    def post(self, request):
        form = ProductForm(request.POST)
        form_img = ProductImageForm(request.POST, request.FILES, request=request)
        if form.is_valid() and form_img.is_valid():
            product = form.save()
            form_img.save_for(product)
            return HttpResponse('<p>Товар добавлен</p><br><a href="../">На главную</a>')
        return render(request, 'new_product.html', context={'form':form, 'form_img':form_img})