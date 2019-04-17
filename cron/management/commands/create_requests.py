'''
Created on 31/12/2014

@author: fabio
'''

from django.core.management.base import BaseCommand, CommandError
from cron.business import ManagedCommands


class Command(BaseCommand):
    
    help = 'Create new requests in database'

    def handle(self, *args, **options):

        mc = ManagedCommands()
        mc.create_requests()
