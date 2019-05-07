from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def products_view(request, *args, **kwargs):
    print(request.headers)
    print(request.user)
    print(request.method)
    # return HttpResponse('<h1>Products View</h1>')

    data = Product.objects.all()

    context = {'title':'Product Page',
    		   'data':data}

    return render(request, 'products.html', context)