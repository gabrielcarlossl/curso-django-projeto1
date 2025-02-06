from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Home!')

def contato(request):
    return HttpResponse('contanto!')
  
def sobre(request):
    return HttpResponse('sobre!')
