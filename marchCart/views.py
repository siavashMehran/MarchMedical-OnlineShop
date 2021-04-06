







from marchCart.models import Cart, OrderDetails
from django.shortcuts import redirect, render


def cart_view(request):
    user_has_cart = True
    if not request.user.is_authenticated:

        return redirect('/login')


    userId = request.user.id

    user_cart = Cart.objects.filter(owner_id=userId, is_paid=False).first()
    try:
        order_details = user_cart.orderdetails_set.all()
    except:
        order_details = None

    if (user_cart is None) or ( not order_details):
        user_has_cart = False
        

    
    

    context = {
        'has_cart'     : user_has_cart,
        'cart_details' : order_details,


    }

    return render(request, 'cart.html', context)




def clear_cart(request):
    if not request.user.is_authenticated:
    
        return redirect('/login')

    userId = request.user.id

    user_cart = Cart.objects.filter(owner_id=userId, is_paid=False).first()
    

    if user_cart is None:
        return redirect(request.META.get('HTTP_REFERER'))

    user_cart.delete()

    return redirect(request.META.get('HTTP_REFERER'))





def cart_pop (request, order_detail_id):

    popThisDetail = OrderDetails.objects.get(pk=order_detail_id)
    popThisDetail.delete()
    return redirect(request.META.get('HTTP_REFERER'))