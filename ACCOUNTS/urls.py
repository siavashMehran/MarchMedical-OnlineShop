from django.urls import path

from .views import log_ou, login_page, register_page

urlpatterns = [
    path('login', login_page),
    path('register', register_page),
    path('logout', log_ou),

]
