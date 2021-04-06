from django.db import models
import os
# Create your models here.


def get_name_ext(filepath):
    fullName      = os.path.basename(filepath)
    filename, ext = os.path.splitext(fullName)
    return filename, ext

def media_upload_path(instance, filepath):
    
    filename, ext = get_name_ext(filepath)

    final = f"id={instance.id}//{filename}{ext}"
    return f"logo/{final}"



class SiteInfoModel (models.Model):



    adress      = models.CharField(verbose_name='ادرس', max_length=200, blank=False)
    phone       = models.CharField(verbose_name='شماره تماس', max_length=25, blank=False, )
    email       = models.EmailField(verbose_name='ایمیل', blank=False, )
    companyName = models.CharField(verbose_name='نام شرکت', max_length=100, blank=False, )
    companyLogo = models.FileField(verbose_name='لوگو (320 x 350)', upload_to=media_upload_path, blank=False, )
    aboutUsTxt  = models.TextField(verbose_name='متن درباره ما', blank=False, )

    def __str__(self):
        return 'Site information'



class ContactUsFormModel (models.Model):

    title   = models.CharField(verbose_name='عنوان', blank=False, max_length=100)
    email   = models.CharField(blank=True, null=True, verbose_name='ایمیل', max_length=100)
    sender  = models.CharField("نام", max_length=50, blank=False)
    message = models.TextField('پیام', blank=False, max_length=500)
    
    def __str__(self):
        return f"{self.title} - {self.email}"