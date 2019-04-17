'''
Created on 13 de out de 2017

@author: fabio
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create_requests/', views.create_requests, name='create_requests'),
    url(r'^update_requests/', views.update_requests, name='update_requests'),
    url(r'^close_requests/', views.close_requests, name='close_requests'),
    url(r'^create_one_year_of_requests/', views.create_one_year_of_requests, name='create_one_year_of_requests'),
    url(r'^create_months_requests/(?P<pmonths>\d+)/', views.create_months_of_requests, name='create_months_of_requests'),
]