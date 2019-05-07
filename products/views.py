from django.shortcuts import render
from .models import Product
from .forms import ProductForm

# Create your views here.
def prod_display_view(request, *args, **kwargs):

    data = Product.objects.all()

    context = {'title':'View Products',
               'data':data}

    return render(request, 'products-display.html', context)

def prod_create_view(request, *args, **kwargs):

    form = ProductForm(request.POST or None)

    if form.is_valid():
        form.save()

    context = {'title':'Create a product',
    'form':form}

    return render(request, 'products-create.html', context)

