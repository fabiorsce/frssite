'''
Created on 24 de nov de 2016

@author: fabio
'''
import random
from .models import Question
from django.shortcuts import render
from qa.models import Alternative
from django.http import JsonResponse
import json
from django.contrib import messages

def random_test(request, number_of_questions=5):
    
    test_questions = []
    
    questions_in_db = Question.objects.all().count()
    if questions_in_db == 0:
        messages.error(request, 'There is no question in database. You must add questions to generate a test.' )
    if questions_in_db < number_of_questions:
        messages.warning(request, 'There are only ' + str(questions_in_db) + ' questions in database. The test will be limited to ' + str(questions_in_db) + ' question(s).' )
        number_of_questions = questions_in_db
    
    questions = Question.objects.all()    
    random_array = []
    while len(random_array) < number_of_questions:
        x = random.randrange(number_of_questions)
        if not x in random_array:
            random_array.append(x)
            test_questions.append(questions[x])
    
    return render(request, template_name='random_test.html', context={'number_of_questions':number_of_questions, 'questions':test_questions})

def correct_questions(request):
    
    
    if not request.method == 'POST':
        messages.error(request, 'Invalid request')
        return render(request, template_name='random_test.html', context={'number_of_questions':0, 'questions':[]})
    
    data = json.loads(request.body.decode('utf-8'))
    
    print (data)
    
    response_data = []
    
    for q in data:
        questionObj = Question.objects.get(id=int(q['question']))
        answerObj = Alternative.objects.filter(question=questionObj, is_answer=True)[0]
        response_data.append({'question': questionObj.id, 'user_answer':int(q['user_answer']), 'correct_answer':answerObj.id})
    
    print(response_data)
    
    return JsonResponse(response_data, safe=False)
