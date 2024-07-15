from django.shortcuts import render
from products.models import Product, ProductCategory

# Create your views here.
# функции = контроллеры = вьюхи

def index(request):
    context = {
        'title': 'Test title',
        'is_promoution': 1,
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Catalog',
        'products': Product.objects.all(),
        'category': ProductCategory.objects.all()
    }
    return render(request, 'products/products.html', context)
