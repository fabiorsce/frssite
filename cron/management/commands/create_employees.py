'''
Created on 31/12/2014

@author: fabio
'''

from django.core.management.base import BaseCommand, CommandError
from datetime import timedelta, datetime, date
from dateutil.relativedelta import relativedelta
from df.models import Employee
import random
import decimal



class Command(BaseCommand):
    
    help = 'Create new employees in database'

    def handle(self, *args, **options):
        
        names = ["Gaylord","Rochell","Jolyn","Janine","Laurence","Tenesha","Honey","Norma","Gretchen","Yvone","Reggie",
                 "Wilfred","Camie","Sheldon","Tesha","Leoma","Loris","Ellie","Ha","Karen","Angle","Vernie","Cortez",
                 "Yuonne","Stacey","Jenae","Layla","Amiee","Vinnie","Millard","Susana","Marth","Tona","Shawnna",
                 "Rosendo","Isabella","Judy","Yahaira","Yessenia","Lori","Milissa","Belinda","Ernestina","Waldo",
                 "Deirdre","Adrianna","Dolly","Jannet","Deanne", "Fabio"]

        for i in range(1,100):
            new_employee = Employee()
            new_employee.first_name = names[random.randint(0,49)]
            new_employee.last_name = names[random.randint(0,49)]
            new_employee.birth_date = date(1970,1,1) + timedelta(days=random.randint(1,10000))
            new_employee.role = Employee.ROLE_CHOICES[random.randint(0,2)][0]
            new_employee.salary = decimal.Decimal(random.randrange(1000000))/100
            new_employee.ssn = ssn = '-'.join( (str(random.randint(0,999)).rjust(3,'0'), str(random.randint(0,99)).rjust(2,'0'), str(random.randint(0,9999)).rjust(4,'0')))

            new_employee.save()


        

        
                
