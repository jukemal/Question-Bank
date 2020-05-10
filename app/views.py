from django.shortcuts import render
from .models import Question

def index(request):
    questions = Question.objects.all()

    context = {
        'questions': questions
    }

    return render(request, 'index.html',context)