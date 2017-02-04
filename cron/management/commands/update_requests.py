'''
Created on 31/12/2014

@author: fabio
'''

from django.core.management.base import BaseCommand, CommandError
from datetime import timedelta
from mr.models import Request


class Command(BaseCommand):
    
    help = 'Update the requests in database'
    

    def handle(self, *args, **options):
        
        rs = Request.objects.filter(status=Request.DONE)
        for r in rs:
            r.paid = r.paid + timedelta(days=1)
            r.created = r.created + timedelta(days=1)
            r.save()
                
