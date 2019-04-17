'''
Created on 21 de nov de 2016

@author: fabio
'''

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cgrtbilling(request):
    return render(request, 'cgrtbilling.html')

def estatbio(request):
    return render(request, 'estatbio.html')