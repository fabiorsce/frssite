'''
Created on 24 de nov de 2016

@author: fabio
'''
import random
from .models import Question
from django.shortcuts import render

def random_test(request, number_of_questions=5):
    questions = Question.objects.all()
    count = questions.count()
    test_questions = []
    i = number_of_questions
    while i > 0:
        test_questions.append(questions[random.randrange(count)])
        i = i - 1
    
    return render(request, template_name='random_test.html', context={'questions':test_questions})