from django.urls import path
from .views import(
    shop, 
    product_detail_view,
    search,
    # SerachProducts,

)
urlpatterns = [
    path('shop/', shop),
    path('shop/<id>/<title>', product_detail_view),
    # path('shop/search2', SerachProducts.as_view()),
    path('shop/search', search),
    

    

]
