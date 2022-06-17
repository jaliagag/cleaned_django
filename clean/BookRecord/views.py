from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home(request):
  return HttpResponse('Hola django-coder')

def template(self):
    myTemplate=loader.get_template('template.html')
    document = myTemplate.render()
    return HttpResponse(document)
