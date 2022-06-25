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
from django.contrib.auth.decorators import login_required # validate identity

#@login_required
def template(request):
    #avatars = Avatar.objects.filter(user=request.user.id).first()
    #avatars = Avatar.objects.filter(user=request.user.id)

    return render(request, 'BookRecord/home.html' )
    #return render(request, 'BookRecord/home.html', {'url':avatars[0].image.url} )

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
    form = AuthenticationForm()
    return render(request, 'BookRecord/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,'BookRecord/home.html', {'message': f'Usuario {username} creado con éxito'})
        else:
            return render(request,'BookRecord/home.html', {'message':'Error - no se pudo crear el usuario (largo mínimo de la contraseña: 9 caracteres)'})
    else:
        form = UserRegisterForm()
        return render(request,'BookRecord/register.html',{'form':form})

@login_required
def edit_profile(request):
    username = request.user
    if request.method == 'POST':
        my_form = UserEditForm(request.POST)
        if my_form.is_valid():
            info = my_form.cleaned_data

            username.email = info['email']
            username.password1 = info['password1']
            username.password2 = info['password1']
            username.first_name = info['first_name']
            username.last_name = info['last_name']
            username.save()

            return render(request,'BookRecord/home.html', {'username':username, 'message': f'Datos actualizados con éxito para {username}'})
    else:
        my_form = UserEditForm(initial={'email':username.email})
    
    return render(request, 'BookRecord/edit_profile.html', {'my_form':my_form,'username':username})

# book model
class View_books(ListView):
    model = Book
    template_name = 'BookRecord/book_list.html'

class Detail_book(DetailView):
    model = Book
    template_name = 'BookRecord/book_detail.html'

class Create_book(LoginRequiredMixin, CreateView): # needs to be logged in
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
    # success_url = reverse_lazy('list_books')

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
