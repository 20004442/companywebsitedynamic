from django.shortcuts import render

from .models import People
from .models import Product

# Create your views here.

def home(request):
    context = {}
    return render(request, 'mywebsite/home.html', context)


def people(request):
    context = {}

    context["persons"] = People.objects.all()
     
    return render(request, 'mywebsite/people.html', context)

def contactus(request):
    context = {}
    return render(request, 'mywebsite/contactus.html', context)

def products(request):
    context = {}

    context["products"] = Product.objects.all()
     
    return render(request, 'mywebsite/products.html', context)