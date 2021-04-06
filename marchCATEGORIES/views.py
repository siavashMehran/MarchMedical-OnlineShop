from django.core.paginator import Paginator
from marchPRODUCTS.models import Product
from django.http.response import Http404
from marchCATEGORIES.models import Category
from django.shortcuts import render

# Create your views here.

class MyPaginator(Paginator): pass;

def category_page(request, categorySlug, *args, **kwargs):

    slug = categorySlug.replace('-', ' ')
    slug2 = categorySlug

    try:
        category = Category.objects.get(slug__iexact=slug)
        a = category.title
        items = Product.objects.filter(active=True, category=category.id)
        print('1111111 try 1111111'*15)
        print(items)
        print('1111111 try 1111111'*15)

    except: #if slug was incorrect
        try :
            category = Category.objects.get(slug__iexact=slug2)
            a = category.title
            items = Product.objects.filter(active=True, category=category.id)
            print('222222 try 22222'*15)
            print(items)
            print('222222 try 22222'*15)
        except: raise Http404('ridi ostad')
            
    paginator = MyPaginator(items, 1)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    print(' $$$$$ try outside$$$$ '*15)
    print(items)
    print(' $$$$$ try outside$$$$'*15)

    context = {
        'a' : a,
        'products'    : items,
        'paginator'   : paginator,
        'page_obj' : page_obj,
        'GETpage'     : page,
        'count'       : items.count
    }

    return render(request, 'category_page.html', context)