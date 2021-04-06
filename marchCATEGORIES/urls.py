from marchCATEGORIES.views import category_page
from django.urls import path



urlpatterns = [
    path('categories/<str:categorySlug>', category_page),
]

