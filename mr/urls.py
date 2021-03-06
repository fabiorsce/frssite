'''
Created on 24 de nov de 2016

@author: fabio
'''

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'$^', views.food_request, name='food_request'),
    url(r'^food_request/', views.food_request, name='food_request'),
    url(r'^food_request_kitchen_view/', views.food_request_kitchen_view, name='food_request_kitchen_view'),
    url(r'^food_request_cashier_view/', views.food_request_cashier_view, name='food_request_cashier_view'),
    url(r'^make_request/', views.make_request, name='make_request'),
    url(r'^add_request/', views.add_request, name='add_request'),
    url(r'^change_to_preparing/(?P<food_request_id>\d+)/$', views.change_to_preparing, name='change_to_preparing'),
    url(r'^change_to_done/(?P<food_request_id>\d+)/$', views.change_to_done, name='change_to_done'),
    url(r'^change_to_paid/(?P<food_request_id>\d+)/$', views.change_to_paid, name='change_to_paid'),
    url(r'^cancel_food_request/(?P<food_request_id>\d+)/$', views.cancel_food_request, name='cancel_food_request'),
    url(r'^sales_tracking/', views.sales_tracking, name='sales_tracking'),
    url(r'^get_sold_products/(?P<months>\d+)/$', views.get_sold_products, name='get_sold_products'),
    url(r'^get_income_by_category/(?P<months>\d+)/$', views.get_income_by_category, name='get_income_by_category'),
    url(r'^get_requests_by_day/(?P<months>\d+)/$', views.get_requests_by_day, name='get_requests_by_day'),
]
