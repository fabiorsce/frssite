'''
Created on 24 de nov de 2016

@author: fabio
'''

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
from django.contrib import messages
from mr.models import Product, Item, Request
from django.db.models import Sum
from django.db import connection
from datetime import timedelta, datetime
from django.db.models import Q

def food_request(request):
    food_requests = Request.objects.filter(Q(status__in=(Request.PAID, Request.PREPARING, Request.WAITING)) | Q(status=Request.DONE, paid__gte=datetime.now()-timedelta(days=1) )).order_by('status', '-paid')
    return render(request, template_name='food_request.html', context={'food_requests':food_requests})

def food_request_kitchen_view(request):
    food_requests = Request.objects.filter(status__in=(Request.PAID,Request.PREPARING)).order_by('status', '-paid')
    return render(request, template_name='food_request_kitchen_view.html', context={'food_requests':food_requests})

def food_request_cashier_view(request):
    food_requests = Request.objects.filter(status__in=(Request.WAITING, Request.PAID)).order_by('status', '-paid')
    return render(request, template_name='food_request_cashier_view.html', context={'food_requests':food_requests})



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
            reqObj.total = json_data['total']
            reqObj.save()
            for i in json_data['items']:
                itemObj = Item()
                itemObj.product_id = int(i['id'])
                itemObj.quantity = int(i['quantity'])
                itemObj.request = reqObj
                itemObj.save()
                
            
            print (json_data)   
    return HttpResponse("OK")

def change_to_done(request, food_request_id):
    r = Request.objects.get(id=int(food_request_id))
    r.status = Request.DONE
    r.save()
    return redirect('food_request_kitchen_view') 
 
def change_to_preparing(request, food_request_id):
    r = Request.objects.get(id=int(food_request_id))
    r.status = Request.PREPARING
    r.save()
    return redirect('food_request_kitchen_view') 

def change_to_paid(request, food_request_id):
    r = Request.objects.get(id=int(food_request_id))
    r.status = Request.PAID
    r.paid = datetime.now()
    r.save()
    return redirect('food_request_cashier_view') 

def cancel_food_request(request, food_request_id):
    Item.objects.filter(request_id=int(food_request_id)).delete()
    Request.objects.filter(id=int(food_request_id)).delete()
    return redirect('food_request_cashier_view') 


def get_requests_by_day(request):
    
    sql_str = '''
            SELECT 
                strftime('%Y-%m-%d', r.paid) as 'paid',
                sum(i.quantity) as 'quantity'
            FROM
                mr_request r 
                    join mr_item i on r.id = i.request_id
            WHERE
                r.paid is not NULL
            GROUP BY
                strftime('%Y-%m-%d', r.paid)
    '''
    
    with connection.cursor() as c:
        c.execute(sql_str)
        result = c.fetchall()
    
    #result.insert(0, ['Date', 'Quantity'])
        
    return JsonResponse(result, safe=False)


def get_sold_products(request):
    
    sold_products = Item.objects.filter(request__status=Request.DONE).values_list('product__title').annotate(qtt=Sum('quantity')).order_by('-qtt')
    sold_products = list(sold_products)
    sold_products.insert(0, ['Product', 'Qtt'])
    return JsonResponse(sold_products, safe=False)

def get_income_by_category(request):
    
    sql_str = ''' 
        SELECT 
            strftime('%Y-%m', r.paid) as 'month',
            COALESCE((select sum(i.quantity*p.price) 
                FROM 
                    mr_product p 
                join mr_item i on p.id = i.product_id
                join mr_request r2 on i.request_id = r2.id 
                WHERE p.category = 'beverage'
                    AND strftime('%Y-%m', r.paid) = strftime('%Y-%m', r2.paid)
            ),0) as 'beverage',
            COALESCE((select sum(i.quantity*p.price) 
                FROM 
                    mr_product p 
                join mr_item i on p.id = i.product_id
                join mr_request r2 on i.request_id = r2.id 
                WHERE p.category = 'dessert'
                    AND strftime('%Y-%m', r.paid) = strftime('%Y-%m', r2.paid)
            ),0) as 'dessert',
            COALESCE((select sum(i.quantity*p.price) 
                FROM 
                    mr_product p 
                join mr_item i on p.id = i.product_id
                join mr_request r2 on i.request_id = r2.id 
                WHERE p.category = 'dish'
                    AND strftime('%Y-%m', r.paid) = strftime('%Y-%m', r2.paid)
            ),0) as 'dish'
        FROM
            mr_request r 
        WHERE
            r.paid is not NULL
        GROUP BY
            strftime('%Y-%m', r.paid)
    '''
    
    with connection.cursor() as c:
        c.execute(sql_str)
        result = c.fetchall()
    
    result.insert(0, ['Month', 'Beverage', 'Dessert', 'Dish'])
        
    return JsonResponse(result, safe=False)

def sales_tracking(request):
   
    sold_products = Item.objects.filter(request__status=Request.DONE).values('product__title').annotate(qtt=Sum('quantity')).order_by('-qtt')
    
    #json_sold_products = serializers.serialize("json", sold_products)
    
    return render(request, template_name='sales_tracking.html', context={'sold_products':sold_products})

