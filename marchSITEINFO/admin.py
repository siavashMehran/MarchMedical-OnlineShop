from django.contrib import admin
from .models import SiteInfoModel, ContactUsFormModel
# Register your models here.

admin.site.register(SiteInfoModel)
admin.site.register(ContactUsFormModel)