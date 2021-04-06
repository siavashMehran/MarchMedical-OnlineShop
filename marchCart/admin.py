from marchCart.models import Cart, OrderDetails
from django.contrib import admin

# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ['__str__','owner', 'is_paid', 'pay_date']
    list_filter  = ['is_paid', 'pay_date']
    
    
    class Meta:
        model = Cart


class OrderDetailsAdmin (admin.ModelAdmin):

    list_display = ['__str__', 'orderd_item', 'orderd_item_count', 'orderd_item_price']
    list_filter = ['relative_cart__id']
    
    class Meta:
        model = OrderDetails


admin.site.register(Cart, CartAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)