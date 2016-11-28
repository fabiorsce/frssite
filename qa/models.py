'''
Created on 19 de ago de 2016

@author: fabio
'''

from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=500)
    
    def __str__(self):
        return self.text
    
class Alternative(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=200)
    is_answer = models.BooleanField(default=False)
    
class Test(models.Model):
    title = models.CharField(max_length=100)
    questions = models.ManyToManyField(Question, through='TestQuestion', through_fields=('test', 'question'),)

class TestQuestion(models.Model):
    test = models.ForeignKey(Test)
    question = models.ForeignKey(Question)
    
    class Meta:
        unique_together = ('test', 'question')
    
        