from marchPRODUCTS.models import Product
from marchCATEGORIES.models import Category
from django.shortcuts import render , redirect
import itertools


def grouper(n, iterable, nullValue=None):
        args = [iter(iterable)] * n
        return ([e for e in t if e !=None] for t in itertools.zip_longest(*args))


def home(request):

    mostViewd = Product.objects.order_by('-views').filter(active=True)[:4]
    

    content = {
        'mostViewd' : mostViewd
    }

    return render(request, 'index.html', content)


def sidebar_partial(request):

    categories = Category.objects.all()
    context = {
        'cat' : categories
    }
    return render(request, 'shit/shop_sidebar.html', context)