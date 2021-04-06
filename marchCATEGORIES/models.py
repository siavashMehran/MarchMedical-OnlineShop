from django.db import models
from django.db.models.signals import pre_save

# Create your models here.


class Category(models.Model):


    title = models.CharField(max_length=60)
    slug  = models.CharField(max_length=60, blank=True)

    class Meta:
            verbose_name = 'دسته'
            verbose_name_plural = 'دسته بندی ها'
            
    def __str__(self):
        return self.title

    def getCatAbsouluteUrl(self):
        # noFordslash = self.title.replace('/', '-')
        # noBackslash = noFordslash.replace('\\', '-')
        # final = noBackslash.replace(' ', '-')

        final = self.slug
        
        return f"/categories/{final}"



def pre_save_reciever(sender, instance, *args, **kwargs):

    if not instance.slug :
        slug = instance.title.replace(' ', '-')

        instance.slug = f"{slug}"

pre_save.connect(receiver=pre_save_reciever, sender=Category)