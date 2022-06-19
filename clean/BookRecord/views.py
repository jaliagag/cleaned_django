from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from BookRecord.models import *
from BookRecord.forms import *

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

def home(request):
  return HttpResponse('Hola django-coder')

def template(self):
    myTemplate=loader.get_template('BookRecord/template.html')
    document = myTemplate.render()
    return HttpResponse(document)

class View_books(ListView):
    model = Book
    template_name = 'BookRecord/list_books.html'

class Create_book(CreateView):
    model = Book
    success_url = '/BookRecord/create_book.html'
    fields = ['title','description','author','date','pages','rating','comments','genre']

def testform(request):
    if request.method == 'POST':
        my_form = Book_form(request.POST)
        if my_form.is_valid():
            info = my_form.cleaned_data
            print(info)

            book = Book(title=info['title'],description=info['description'],author=info['author'],date=info['date'],pages=info['pages'],rating=info['rating'],comments=info['comments'],genre = info['genre'])
            book.save()

            return render(request, 'BookRecord/list_books.html')
    else:
        my_form=Book_form()

    return render(request, 'BookRecord/create_book.html', {'my_form': my_form})

