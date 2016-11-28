'''
Created on 19 de ago de 2016

@author: fabio
'''

from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':100}))
    '''
    class Meta:
        model = Question
    '''
    
class AlternativeInlineForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'cols':100}))
    
