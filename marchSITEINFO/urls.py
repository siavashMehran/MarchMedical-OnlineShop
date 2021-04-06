
from django.urls import path
from .views import aboutUsPage, contactUsPage


urlpatterns = [
    path('contact-us', contactUsPage),
    path('about-us', aboutUsPage),
]


