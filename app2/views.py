from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def python(request):
    return HttpResponse('python is easy to learn')
    
