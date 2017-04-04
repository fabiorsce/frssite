from django.shortcuts import render

from django.views.generic.list import ListView
from django.utils import timezone

from df.models import Employee

class EmployeeListView(ListView):

    model = Employee

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context