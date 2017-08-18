from django.db import models
from decimal import Decimal
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

class Material(models.Model):

    serial_number = models.CharField(max_length=20, null=False, blank=False, unique=True)
    description = models.CharField(max_length=200, null=False, blank=False)
    photo = models.ImageField(null=False, blank=False, upload_to='material_images')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    lat = models.DecimalField(_('Latitude'), max_digits=10, decimal_places=8)
    lng = models.DecimalField(_('Longitude'), max_digits=10, decimal_places=8)
    address = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.serial_number

class ReviewStatus(models.Model):
    description = models.CharField(max_length=20, null=False, blank=False, unique=True)

    def __str__(self):
        return self.description

class Review(models.Model):

    user = models.ForeignKey(User, null=False)
    material = models.ForeignKey(Material, null=False)
    message = models.CharField(max_length=200, null=False, blank=False)
    created = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    lat = models.DecimalField(_('Latitude'), max_digits=10, decimal_places=8)
    lng = models.DecimalField(_('Longitude'), max_digits=10, decimal_places=8)
    address = models.CharField(max_length=500, null=True, blank=True)
    status = models.ForeignKey(ReviewStatus, null=False)

