from django.shortcuts import render
from .models import Product, WeeklyTreat

def home(request):
    return render(request, 'bakery/home.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'bakery/products.html', {'products': products})

def weekly_treats(request):
    weekly_treats = WeeklyTreat.objects.all()
    return render(request, 'bakery/weekly_treats.html', {'weekly_treats': weekly_treats})
