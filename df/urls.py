from django.conf.urls import include, url
from django.contrib import admin
from . import views



urlpatterns = [
    url(r'^$', views.EmployeeListView.as_view(), name='employee-list'),
]
