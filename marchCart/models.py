from django.db import models
from django.contrib.auth.models import User
from marchPRODUCTS.models import Product
from django.contrib.auth.models import User
# Create your models here.





class Cart (models.Model):
    
    owner    = models.ForeignKey(User, models.CASCADE)
    is_paid  = models.BooleanField(default=False, verbose_name='پرداخت شده')
    pay_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید کاربران'

    def __str__(self):
        username = self.owner.username
        user_id  = self.owner.id

        return f"#{self.id}  (@{username}"


class OrderDetails(models.Model):
    
    relative_cart     = models.ForeignKey(Cart, models.CASCADE)
    orderd_item       = models.ForeignKey(Product, models.CASCADE)
    orderd_item_count = models.PositiveIntegerField(verbose_name='تعداد سفارش', )
    orderd_item_price = models.PositiveIntegerField(verbose_name='قیمت', )
    

    class Meta:
        verbose_name = 'جزییات سبد'
        verbose_name_plural = 'جزییات سبد ها'

    def order_details_sum(self):
        sum = self.orderd_item_count * self.orderd_item_price
        return sum

    

    def __str__(self):
        return f"#{self.relative_cart.id} (@{self.relative_cart.owner.username})"
    


    