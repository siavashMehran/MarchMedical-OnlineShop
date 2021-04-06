from django.db import models
from django.db.models.signals import pre_save
from marchPRODUCTS.models import Product

# Create your models here.


class TAG (models.Model):

    title    = models.CharField(blank=False, null=False, max_length=80)
    slug     = models.CharField(blank=True, max_length=80)
    active   = models.BooleanField(default=True)
    timestamp= models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, blank=True)


    def __str__(self):
        return self.title


    def getTagAbsouluteUrl(self):

        return f'/shop/search?q={self.title}'


def pre_save_reciever(sender, instance, *args, **kwargs):
    print('%'*20)
    if not instance.slug:
        instance.slug = instance.title.replace(' ', '-')


pre_save.connect(pre_save_reciever, sender=TAG)
