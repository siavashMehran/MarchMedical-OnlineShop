from django.http.response import Http404
from marchCATEGORIES.models import Category
import os
from django.db import models
from django.db.models import Q

def get_name_ext(filepath):
    fullName      = os.path.basename(filepath)
    filename, ext = os.path.splitext(fullName)
    return filename, ext

def media_upload_path(instance, filepath):
    
    filename, ext = get_name_ext(filepath)

    final = f"id={instance.id}//{filename}{ext}"
    return f"products/{instance.title}--{final}"

def media_gallery_upload_path(instance, filepath):

    filename, ext = get_name_ext(filepath)

    final = f"id={instance.id}//{filename}{ext}"
    return f"gallery/{instance.title}--{final}"


class ProductsManager(models.Manager):
    
    def getById(self, id):
        item = self.get_queryset().filter(id=id)
        return item.first()

    def getActiveById(self, id, title):
        nonSlug = title.replace('-', ' ')
        item = self.get_queryset().filter(id=id, active=True, title=nonSlug)
        
        return item.first()

    def getActive(self):
        return self.get_queryset().filter(active=True)


    def search(self, querry):

        condition =  Q(title__icontains=str(querry)) |  Q(caption=str(querry)) | Q(tag__title__iexact=str(querry)) | Q(category__title__icontains=str(querry)) ;

        return self.get_queryset().filter(condition, active=True).distinct()

    
    

class Product(models.Model):

    title       = models.CharField(blank=False, max_length=50, default='عنوان یا اسم محصول', verbose_name='عنوان')
    price       = models.PositiveIntegerField(blank=False, default=0,verbose_name='قیمت',)
    caption     = models.CharField(blank=False, max_length=160, verbose_name='توضیحات کوتاه و مختصر')
    pic         = models.ImageField(upload_to=media_upload_path, null=True, blank=False,verbose_name='عکس')    
    description = models.TextField(blank=False, max_length=800, verbose_name=' توضیح کامل')
    brand       = models.CharField(blank=True, null=True, max_length=40,verbose_name='برند')
    active      = models.BooleanField(default=True,verbose_name='فعال')
    timestamp   = models.DateTimeField("تاریخ و ساعت", auto_now_add=True)
    category    = models.ManyToManyField(Category, verbose_name='دسته', blank=True)

    views       = models.IntegerField(blank=True, default=0, null=False)


    objects = ProductsManager()

    class Meta:
        verbose_name = 'عنوان'
        verbose_name_plural = 'محصول'

    def __str__(self):
        return f"{self.title}"

    def getAbsoluteUrl(self):
        return f"/shop/{self.id}/{self.title.replace(' ', '-')}"



class ProductGallery(models.Model):

    title   = models.CharField(max_length=50)
    pic     = models.ImageField(upload_to=media_gallery_upload_path, null=True, blank=False,verbose_name='عکس')    
    product = models.ForeignKey(Product, models.CASCADE, )


    def __str__(self):
        return self.title