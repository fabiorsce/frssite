# Create your views here.


'''
Created on 25 de may de 2015

@author: fabio
'''

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def get_location(request):
    return render(request, template_name='get_location.html')