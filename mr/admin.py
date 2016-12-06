'''
Created on 19 de ago de 2016

@author: fabio
'''

from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['photo', 'text', 'price' ]
    
