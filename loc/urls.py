'''
Created on 24 de nov de 2016

@author: fabio
'''

from django.conf.urls import include, url
from django.contrib import admin
from . import views
from tastypie.api import Api
from .api.resources import MaterialResource

v1_api = Api(api_name='v1')
v1_api.register(MaterialResource())

urlpatterns = [
    url(r'^get_location/', views.get_location, name='get_location'),
    url(r'^api/', include(v1_api.urls)),
]



