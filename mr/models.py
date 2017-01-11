'''
Created on 6 de dez de 2016

@author: fabio
'''

from django.db import models
from decimal import Decimal

class Product(models.Model):
    
    BEVERAGE = 'beverage'
    DISH = 'dish'
    DESSERT = 'dessert'
    CATEGORY_CHOICES = ( 
                          (BEVERAGE, 'Beverage'),
                          (DISH, 'Dish'),
                          (DESSERT, 'Desert'),
                        )
    
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default=BEVERAGE, null=False, blank=False)
    photo = models.ImageField(null=False, blank=False, upload_to='product_images')
    title = models.CharField(max_length=40, null=False, blank=False)
    text = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    
    def __str__(self):
        return self.title

class Request(models.Model):
    
    WAITING = '1waiting'
    PAID = '2paid'
    PREPARING = '3preparing'
    DONE = '4done'
    STATUS_CHOICES = ( 
                       (WAITING, 'Waiting Payment'),
                       (PAID, 'Paid'),
                       (PREPARING, 'Preparing'),
                       (DONE, 'Done'),
                    )
    
    name = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=50, null=False, blank=False, choices=STATUS_CHOICES, default=WAITING)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    created = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    paid = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    def getTotalValue(self):
        
        total_value = Decimal.from_float(0.0)
        items = self.item_set.all()
        for i in items:
            total_value = total_value + (i.product.price * i.quantity) 
            
        return total_value
    
     
    def getStatusStyle(self):
        if self.status == self.WAITING:
            return 'danger'
        elif self.status == self.PAID:
            return 'info'
        elif self.status == self.PREPARING:
            return 'warning'
        elif self.status == self.DONE:
            return 'success'
        
        return 'danger'

    
class Item(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    request = models.ForeignKey(Request, null=False, blank=False)
    
    def __str__(self):
        return self.product.text
    
