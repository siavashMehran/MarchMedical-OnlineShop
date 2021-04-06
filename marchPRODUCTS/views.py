
import itertools

from django.http.response import JsonResponse
from marchCOMMENTS.forms import CommentModelForm
from marchCart.models import Cart, OrderDetails
from marchCart.forms import OrderForm
from django.http import Http404
from django.core.paginator import Paginator
from marchPRODUCTS.models import Product, ProductGallery
from django.shortcuts import redirect, render

class MyPaginator(Paginator): pass;


def shop(request):
    products = Product.objects.getActive().order_by('timestamp')
    
    paginator = MyPaginator(products, 9)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    
    
    context = {
        'products'    : products,
        'paginator'   : paginator,
        'page_obj' : page_obj,
        'GETpage'     : page
        
    }

    return render(request, 'shop.html', context)



def product_detail_view(request, id=None, title=None):

    
        
        

    # slice list into smaller lists with length of (n)
    def grouper(n, iterable, nullValue=None):
        args = [iter(iterable)] * n
        return ([e for e in t if e !=None] for t in itertools.zip_longest(*args))



    # getting the objects
    item = Product.objects.getActiveById(id=id, title=title)
    galleryPics = ProductGallery.objects.filter(product_id=id)
    categories = item.category.all()


    # products validation for existing or being active
    if item != None :
        tags = item.tag_set.all()  
    else :
        raise Http404('not active or sumting')

    
    

    # galery section
    #innitialization for detail view (product gallery) arrows
    gallery_is_none = True 

    if (galleryPics.first() is not None) and (len(galleryPics) > 3)  :
        gallery_is_none = False
    gallery_sliced = list(grouper(3, galleryPics))



    # ordering section
    #ordering form instance
    order_form_instance = OrderForm(request.POST or None, initial={'product_id':id, 'product_price':item.price })
    
    if (request.method == "POST") and ('order_count' in request.POST):
        print('>'*100)
        print(request.user)
        print(request.user.is_authenticated)
        print('<'*100)

        if request.user.is_authenticated:


            # USER Cart related
            UserActiveCart = Cart.objects.filter(owner_id=request.user.id, is_paid=False).first()
            if UserActiveCart == None:
                UserActiveCart = Cart.objects.create(owner_id=request.user.id, is_paid=False)
            
            if order_form_instance.is_valid():

                order_count = order_form_instance.cleaned_data.get('order_count')
                orderd_item = order_form_instance.cleaned_data.get('product_id')
                item_price  = order_form_instance.cleaned_data.get('product_price')

                #making sure count is positive
                if order_count < 0: order_count = 1;

                OrderDetails.objects.create(
                    relative_cart_id    = UserActiveCart.id,
                    orderd_item_id      = orderd_item,
                    orderd_item_count   = order_count,
                    orderd_item_price   = item_price,
                    )

                print('0'*100)
                print(order_count)
                print(orderd_item)
                print('0'*100)

                order_form_instance = OrderForm(request.POST or None, initial={'product_id':id, 'product_price':item.price })
                return redirect('user_cart')

            else:raise Http404('form not valid');
            
        else: return redirect('/login');

    

    # comments section ========================
    comments = item.comment_set.all()

    #  commenting for authenticated users only initialisation
    if request.user.is_authenticated:
        commentsInitialData = {'product':item, 'user':request.user.username, 'user_email':request.user.email}
    else:
        commentsInitialData = {}


    commentform = CommentModelForm(initial=commentsInitialData)
    

    if (request.method == 'POST') and ('comment_text' in request.POST):
        commentform = CommentModelForm(request.POST)
        if commentform.is_valid:
            commentform.save()

        order_form_instance = OrderForm()
        commentform = CommentModelForm()
        return redirect(request.META.get('HTTP_REFERER'))

    if request:
        item.views += 1
        item.save()
        

    context = {
        'product'        : item,
        'tags'           : tags,
        'categories'     : categories,
        'gallery_sliced' : gallery_sliced,
        'gallery_is_none': gallery_is_none,
        'form'           : order_form_instance,
        'comments'       : comments,
        'commentform'       : commentform
        
    }

    return render(request, 'product_detail_view.html', context)



# class SerachProducts(ListView):

#     template_name = 'search_page.html'
    
#     page_object = Paginator.page
#     paginate_by = 9

#     def get_queryset(self):
#         request = self.request
#         serach = request.GET.get('q')
#         print(serach)
#         return Product.objects.filter(title__icontains=serach) 

def search(request, *args, **kwargs):

    querry   = request.GET.get('q')
    products = Product.objects.search(querry).order_by('title')
    products.reverse()

    searchCount = products.count()
    print(*args)
    print(**kwargs)
    context = {
        'page_obj' : products,
        'count' : searchCount,
    }
    return render(request, 'search_page.html', context)
        

