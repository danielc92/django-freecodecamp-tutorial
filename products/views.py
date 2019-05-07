from django.shortcuts import render
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
def prod_display_view(request, *args, **kwargs):

    data = Product.objects.all()

    context = {'title':'View Products',
               'data':data}

    return render(request, 'products-display.html', context)

def prod_create_view(request, *args, **kwargs):

    """ USING RawProductForm Class (has validators) """
    form = RawProductForm(request.GET)

    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
        else:
            print(my_form.errors)

    context = {
        'form':form
    }
    
    return render(request, 'products-create.html', context)


    """ USING ProductForm Class from forms.py """
    # form = ProductForm(request.POST or None)

    # if form.is_valid():
    #     form.save()

    # context = {'title':'Create a product',
    # 'form':form}

    # return render(request, 'products-create.html', context)

