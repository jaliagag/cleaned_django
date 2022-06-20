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

from django.contrib.auth.mixins import LoginRequiredMixin # block view when not logged in

def template(self):
    myTemplate=loader.get_template('BookRecord/home.html')
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
                login(request, user) # user exists and logs them in
                return render(request,'BookRecord/home.html', {'message':f'Bienvenido {name}'})
            else:
                return render(request,'BookRecord/home.html', {'message':f'Error: datos incorrectos'})
        else:
            return render(request,'BookRecord/home.html', {'message':f'Error: formulario erróneo'})
    else:
        form = AuthenticationForm()
        return render(request, 'BookRecord/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,'BookRecord/home.html', {'message':'Usuario creado con éxito'})
        else:
            return render(request,'BookRecord/home.html', {'message':'Error en el formulario'})
    else:
        form = UserRegisterForm()
        return render(request,'BookRecord/register.html',{'form':form})

# book model
class View_books(ListView):
    model = Book
    template_name = 'BookRecord/book_list.html'

class Detail_book(DetailView):
    model = Book
    template_name = 'BookRecord/book_detail.html'

class Create_book(LoginRequiredMixin, CreateView):
    model = Book
    success_url = '/BookRecord/book/list/'
    fields = ['title','description','author','date','pages','rating','comments','genre']

class Update_book(LoginRequiredMixin, UpdateView):
    model = Book
    success_url = '/BookRecord/book/list/'
    fields = ['title','description','author','date','pages','rating','comments','genre']

class Delete_book(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/BookRecord/book/list/'

# author model
class View_authors(ListView):
    model = Author
    template_name = 'BookRecord/author_list.html'

class Detail_author(DetailView):
    model = Author
    template_name = 'BookRecord/author_detail.html'

class Create_author(LoginRequiredMixin, CreateView):
    model = Author
    success_url = '/BookRecord/author/list/'
    fields = ['name','lastname','book','wiki','genre']

class Update_author(LoginRequiredMixin, UpdateView):
    model = Author
    success_url = '/BookRecord/author/list/'
    fields = ['name','lastname','book','wiki','genre']

class Delete_author(LoginRequiredMixin, DeleteView):
    model = Author
    success_url = '/BookRecord/author/list/'
