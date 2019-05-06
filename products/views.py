from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def products_view(request, *args, **kwargs):
    print(request.headers)
    print(request.user)
    print(request.method)
    return HttpResponse('<h1>Products View</h1>')