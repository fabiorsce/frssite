from django.shortcuts import render
from cron.business import ManagedCommands

from django.http import JsonResponse


def create_requests(request):
    mc = ManagedCommands()
    mc.create_requests()
    return JsonResponse({'result':'ok'})

def update_requests(request):
    mc = ManagedCommands()
    mc.update_requests()
    return JsonResponse({'result':'ok'})

def close_requests(request):
    mc = ManagedCommands()
    mc.close_requests()
    return JsonResponse({'result':'ok'})

def create_one_year_of_requests(request):
    mc = ManagedCommands()
    mc.create_one_year_of_requests()
    return JsonResponse({'result':'ok'})

def create_months_of_requests(request, pmonths):
    mc = ManagedCommands()
    mc.create_months_of_requests(pmonths)
    return JsonResponse({'result':'ok'})

    
