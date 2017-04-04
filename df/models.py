from django.db import models

# Create your models here.

class Employee(models.Model):

    PROJECT_MANAGER = 'Project Manager'
    DEVELOPER = 'Developer'
    DESIGNER = 'Designer'

    ROLE_CHOICES = ( 
                          (PROJECT_MANAGER, PROJECT_MANAGER),
                          (DEVELOPER, DEVELOPER),
                          (DESIGNER, DESIGNER),
                        )

    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    #ssn example = 987-65-4329
    ssn = models.CharField(max_length=10, null=False, blank=False)
    birth_date = models.DateField(null=False, blank=False)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default=DEVELOPER, null=False, blank=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return ', '.join((self.last_name, self.first_name))