from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Product
from .forms import ProductForm, RawProductForm

# Home Page
def prod_home_view(request, *args, **kwargs):

    context = {'title':'Home Page'}

    return render(request, 'products-home.html', context)

# Display all products view
def prod_display_view(request, *args, **kwargs):

    data = Product.objects.all()

    context = {'title':'View Products',
               'data':data}

    return render(request, 'products-display.html', context)


# Create a product view
def prod_create_view(request, *args, **kwargs):

    """ USING RawProductForm Class (has validators) """
    form = RawProductForm(request.GET)

    if request.method == 'POST':
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Product.objects.create(**form.cleaned_data)
            return HttpResponse('<code>You have successfully added a new product to the database.</code>')
        else:
            print(my_form.errors)

    context = {
        'form':form
    }

    url = reverse('products-view')
    print(url)
    
    return render(request, 'products-create.html', context)


    """ USING ProductForm Class from forms.py """
    # form = ProductForm(request.POST or None)

    # if form.is_valid():
    #     form.save()

    # context = {'title':'Create a product',
    # 'form':form}

    # return render(request, 'products-create.html', context)

