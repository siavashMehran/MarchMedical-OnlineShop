from django.contrib import admin

from .models import Product, ProductGallery
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', '__str__', 'price', 'caption','pic' , 'active']
    class Meta:
        model = Product


class galleryAdmin (admin.ModelAdmin):

    list_display = ['id', '__str__', 'product']
    class Meta:
        model = ProductGallery

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery, galleryAdmin)