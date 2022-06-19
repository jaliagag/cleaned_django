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

def template(self):
    myTemplate=loader.get_template('BookRecord/template.html')
    document = myTemplate.render()
    return HttpResponse(document)

class View_books(ListView):
    model = Book
    template_name = 'BookRecord/book_list.html'

class Detail_book(DetailView):
    model = Book
    template_name = 'BookRecord/book_detail.html'

class Create_book(CreateView):
    model = Book
    success_url = '/BookRecord/book/list/'
    fields = ['title','description','author','date','pages','rating','comments','genre']

class Update_book(UpdateView):
    model = Book
    success_url = '/BookRecord/book/list/'
    fields = ['title','description','author','date','pages','rating','comments','genre']

class Delete_book(DeleteView):
    model = Book
    success_url = '/BookRecord/book/list/'

