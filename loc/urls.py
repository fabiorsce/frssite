'''
Created on 24 de nov de 2016

@author: fabio
'''

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^get_location/', views.get_location, name='get_location'),
]
