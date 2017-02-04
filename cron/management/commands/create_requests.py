'''
Created on 31/12/2014

@author: fabio
'''

from django.core.management.base import BaseCommand, CommandError
from datetime import timedelta
from mr.models import Request


class Command(BaseCommand):
    
    help = 'Create new requests in database'
    
    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument(
            '--days',
            default=3,
            help='Update dates to date less x days',
        )

    def handle(self, *args, **options):
        
        rs = Request.objects.filter(status=Request.DONE)
        for r in rs:
            items = r.item_set.all()
            r.id = None
            r.paid = r.paid - timedelta(days=int(options['days']))
            r.created = r.created - timedelta(days=int(options['days']))
            r.save()
            for i in items:
                i.id = None
                i.request = r
                i.save()
                
