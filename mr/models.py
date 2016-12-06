'''
Created on 6 de dez de 2016

@author: fabio
'''

from django.db import models

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
    text = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    
    def __str__(self):
        return self.text

class Request(models.Model):
    
    QUEUE = 'queue'
    PREPARING = 'preparing'
    DONE = 'done'
    STATUS_CHOICES = ( (QUEUE, 'Queue'),
                       (PREPARING, 'Preparing'),
                       (DONE, 'Done'),
                    )
    
    name = models.CharField(max_length=50, null=False, blank=False)
    status = models.CharField(max_length=50, null=False, blank=False, choices=STATUS_CHOICES, default=QUEUE)
    created = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    
    def __str__(self):
        return self.product.text

    
class Item(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    request = models.ForeignKey(Request, null=False, blank=False)
    
    def __str__(self):
        return self.product.text
    
