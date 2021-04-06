from marchCATEGORIES.models import Category
from django.contrib import admin

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id' , '__str__']

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)