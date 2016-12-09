'''
Created on 24 de nov de 2016

@author: fabio
'''

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^food_request/', views.food_request, name='food_request'),
    url(r'^make_request/', views.make_request, name='make_request'),
]
