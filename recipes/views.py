from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'recipes/home.html')

def contato(request):
    return HttpResponse('contanto!')
  
def sobre(request):
    return HttpResponse('sobre!')
