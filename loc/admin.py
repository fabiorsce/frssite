'''
Created on 24 de mai de 2017

@author: fabio
'''

from django.contrib import admin
from .models import Material, Review, ReviewStatus
from django.contrib import messages



def accept_new_location(modeladmin, request, queryset):
    objClosedStatus = ReviewStatus.objects.get(description='closed')

    for r in queryset:
        r.material.lat = r.lat
        r.material.lng = r.lng
        r.material.address = r.address
        r.material.save()
        r.status = objClosedStatus
        r.save()
    messages.success(request,'The locations of the materials were updated.')
accept_new_location.short_description = "Accept new location"

def ingnore_review(modeladmin, request, queryset):
    objClosedStatus = ReviewStatus.objects.get(description='closed')
    queryset.update(status=objClosedStatus)
    messages.success(request,'The review requests were ignored.')
ingnore_review.short_description = "Ignore review"

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display=['serial_number', 'description', 'photo', 'price', 'lat', 'lng', 'address' ]
    

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display=['material', 'user', 'message', 'lat', 'lng', 'address', 'created', 'status' ]
    actions = [accept_new_location, ingnore_review]
    list_filter = ('status', 'user')
    ordering = ('status','-created',)

@admin.register(ReviewStatus)
class ReviewStatusAdmin(admin.ModelAdmin):
    list_display=['id', 'description']



