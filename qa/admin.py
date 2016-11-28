'''
Created on 19 de ago de 2016

@author: fabio
'''

from django.contrib import admin
from .models import Question, Alternative
from .forms import QuestionForm, AlternativeInlineForm


class AlternativeInline(admin.TabularInline):
    model = Alternative
    min_num = 5
    max_num = 5
    extra = 5
    can_delete = False
    can_add = False
    
    form = AlternativeInlineForm
    
    
    
    

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display=['text', ]
    inlines= [ AlternativeInline, ]
    form = QuestionForm
    
