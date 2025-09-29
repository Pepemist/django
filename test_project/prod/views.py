from django.shortcuts import render
from prod.models import ProdCategory, Product

def index(request):
    context = {
        'title': 'Test Title',
        'is_promotion': False,
    }
    return render(request, 'index.html', context)

def products(request):
    context = {
        'title': 'Products page',
        'products': Product.objects.all(),
        'categories': ProdCategory.objects.all()
    }
    return render(request, 'prod.html', context)
