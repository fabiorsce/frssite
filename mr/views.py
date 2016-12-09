'''
Created on 24 de nov de 2016

@author: fabio
'''
import random
from django.shortcuts import render
from django.http import JsonResponse
import json
from django.contrib import messages
from .models import Request

def food_request(request):
    
    food_requests = Request.objects.filter()
    
    return render(request, template_name='food_request.html', context={'food_requests':food_requests})


def make_request(request):
    
    
    
    return render(request, template_name='make_request.html', context=locals())