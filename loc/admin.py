'''
Created on 24 de mai de 2017

@author: fabio
'''

from django.contrib import admin
from .models import Material, Review


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display=['serial_number', 'description', 'photo', 'price', 'lat', 'lng' ]
    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=['material', 'user', 'message', 'created', 'status' ]