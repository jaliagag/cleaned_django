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

# login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

def template(self):
    myTemplate=loader.get_template('BookRecord/template.html')
    document = myTemplate.render()
    return HttpResponse(document)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')

            user = authenticate(username=name,password=passw)

            if user is not None:
                login(request, user)
                return render(request,'BookRecord/template.html', {'message':f'Bienvenido {name}'})
            else:
                return render(request,'BookRecord/template.html', {'message':f'Error: datos incorrectos'})
        else:
            return render(request,'BookRecord/template.html', {'message':f'Error: formulario erróneo'})

    form = AuthenticationForm()
    return render(request, 'BookRecord/login.html', {'form': form})

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

