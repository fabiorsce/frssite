'''
Created on 24 de nov de 2016

@author: fabio
'''

from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'$^', views.random_test, name='random_test'),
    url(r'^random_test/', views.random_test, name='random_test'),
    url(r'^correct_questions/', views.correct_questions, name='correct_questions'),
]
