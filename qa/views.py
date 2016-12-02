'''
Created on 24 de nov de 2016

@author: fabio
'''
import random
from .models import Question
from django.shortcuts import render
from qa.models import Alternative

def random_test(request, number_of_questions=5):

    test_questions = []
    selected_alternatives = []
    
    if request.method == 'POST':
        right_questions = 0
        i = 0
        while i < number_of_questions:
            i = i + 1
            parameter = ''.join(('question', i.__str__()))
            alternative_id = request.POST.get(parameter, '')
            if alternative_id:
                alternative = Alternative.objects.get(id=int(alternative_id))
                if alternative.is_answer:
                    right_questions = right_questions + 1
            test_questions.append(alternative.question)
            selected_alternatives.append(alternative.id)
                
        return render(request, template_name='random_test.html', context={'questions':test_questions, 'selected_alternatives': selected_alternatives})        
    else:
        questions = Question.objects.all()
        count = questions.count()
        i = number_of_questions
        while i > 0:
            test_questions.append(questions[random.randrange(count)])
            i = i - 1
    
    return render(request, template_name='random_test.html', context={'number_of_questions':number_of_questions, 'questions':test_questions})

from django.http import JsonResponse
import json

def correct_questions(request):
    
    data = json.loads(request.body.decode('utf-8'))
    
    print (data)
    
    response_data = []
    
    for q in data:
        questionObj = Question.objects.filter(id=int(q['question']))
        answerObj = Alternative.objects.filter(question=questionObj, is_answer=True)
        response_data.append({'question': questionObj.id, 'user_answer':data['user_answer'], 'correct_answer':answerObj.id})
    
    return JsonResponse(response_data, safe=False)
