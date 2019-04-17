'''
Created on 24 de nov de 2016

@author: fabio
'''

from django.conf.urls import include, url
from django.contrib import admin
from loc import views
from tastypie.api import Api
from loc.api.resources import MaterialResource, UserResource, ReviewResource, ReviewStatusResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(MaterialResource())
v1_api.register(ReviewResource())
v1_api.register(ReviewStatusResource())

urlpatterns = [
    url(r'^get_location/', views.get_location, name='get_location'),
    url(r'^api/', include(v1_api.urls)),
]



