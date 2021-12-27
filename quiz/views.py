from django.shortcuts import render

# Create your views here.

def quiz(request):
    return render(request, 'quiz/home.html')

def create(request):
    return render(request, 'quiz/create.html')

def join(request):
    return render(request, 'quiz/join.html')    