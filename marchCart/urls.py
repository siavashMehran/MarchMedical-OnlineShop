# from marchCart.views import add_user_order
from marchCart.views import cart_pop, cart_view, clear_cart
from django.urls import path

urlpatterns = [
    # path('cart', add_user_order)
    path('cart', cart_view, name='user_cart'),
    path('cart/clear/', clear_cart, name='clear_my_cart'),
    path('cart/pop/<int:order_detail_id>', cart_pop, name='pop_from_cart'),
]


