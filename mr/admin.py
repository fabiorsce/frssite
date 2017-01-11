'''
Created on 19 de ago de 2016

@author: fabio
'''

from django.contrib import admin
from .models import Product, Request


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id', 'photo','title', 'text', 'price' ]
    

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'status', 'total', 'created', 'paid' ]
