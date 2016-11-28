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
    
    return render(request, template_name='random_test.html', context={'questions':test_questions})