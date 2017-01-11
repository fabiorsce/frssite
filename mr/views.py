'''
Created on 24 de nov de 2016

@author: fabio
'''
import random
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json
from django.contrib import messages
from .models import Request
from mr.models import Product, Item

def food_request(request):
    
    food_requests = Request.objects.filter()
    
    return render(request, template_name='food_request.html', context={'food_requests':food_requests})


def make_request(request):
    
    dishes = Product.objects.filter(category=Product.DISH)
    beverages = Product.objects.filter(category=Product.BEVERAGE)
    desserts =  Product.objects.filter(category=Product.DESSERT)
    
    products = Product.objects.all()
    
    return render(request, template_name='make_request.html', context=locals())

def add_request(request):
    
    if request.is_ajax():
        if request.method == 'POST':
            json_data = json.loads(request.body.decode("utf-8"))
            reqObj=Request()
            reqObj.name = json_data['name']
            reqObj.status = Request.WAITING
            reqObj.save()
            for i in json_data['items']:
                itemObj = Item()
                itemObj.product_id = int(i['id'])
                itemObj.quantity = int(i['quantity'])
                itemObj.request = reqObj
                itemObj.save()
                
            
            print (json_data)   
    return HttpResponse("OK")