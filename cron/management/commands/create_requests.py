'''
Created on 31/12/2014

@author: fabio
'''

from django.core.management.base import BaseCommand, CommandError
from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta
from mr.models import Request, Product, Item
import random



class Command(BaseCommand):
    
    help = 'Create new requests in database'

    def handle(self, *args, **options):
        
        number_of_new_requests = random.randrange(0,20)
        i = 0
        names = ["Gaylord","Rochell","Jolyn","Janine","Laurence","Tenesha","Honey","Norma","Gretchen","Yvone","Reggie",
                 "Wilfred","Camie","Sheldon","Tesha","Leoma","Loris","Ellie","Ha","Karen","Angle","Vernie","Cortez",
                 "Yuonne","Stacey","Jenae","Layla","Amiee","Vinnie","Millard","Susana","Marth","Tona","Shawnna",
                 "Rosendo","Isabella","Judy","Yahaira","Yessenia","Lori","Milissa","Belinda","Ernestina","Waldo",
                 "Deirdre","Adrianna","Dolly","Jannet","Deanne", "Fabio"]
        produts = Product.objects.all()
        
        requests_to_update = Request.objects.filter(status__in=[Request.WAITING, Request.PAID, Request.PREPARING])
        for r in requests_to_update:
            if r.status != Request.PAID:
                r.paid = datetime.utcnow() + relativedelta(minutes=random.randint(1,30))
            r.status = Request.DONE
            r.save()
        
        
        while i < number_of_new_requests:
            i = i + 1
            new_request = Request()
            new_request.name = names[random.randint(0,49)]
            new_request.status = Request.STATUS_CHOICES[random.randint(0,3)][0]
            new_request.total = 0
            if new_request.status != '1waiting':
                new_request.paid = datetime.utcnow() + relativedelta(minutes=random.randint(-120,120))
            new_request.save()
             
            items = random.sample(range(6), k=random.randint(1,6))
            for j in items:
                new_item = Item()
                new_item.request = new_request
                new_item.product = produts[j]
                new_item.quantity = random.randint(1,6)
                new_item.save()
                
            new_request.total = new_request.getTotalValue()
            new_request.save()
        
                
