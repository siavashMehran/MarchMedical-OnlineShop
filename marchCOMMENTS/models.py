from marchPRODUCTS.models import Product
from django.contrib.auth.models import User
from django.db import models
# Create your models here.



class Comment(models.Model):



    product      = models.ForeignKey(Product, on_delete=models.CASCADE)

    user         = models.CharField(max_length=50, blank=False, )
    user_email   = models.EmailField(blank=True)
    comment_text = models.TextField(max_length=300, blank=False, null=False)

    likes        = models.PositiveIntegerField(null=False, blank=True, default=0)
    users_liked  = models.ManyToManyField(User, blank=True)
    timeStamp    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.title






class BadWords(models.Model):

    word = models.CharField(max_length=20)

    def __str__(self):
        return self.word