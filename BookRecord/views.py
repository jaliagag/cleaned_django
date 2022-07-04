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
    if request.user.is_authenticated:
        if len(Avatar.objects.filter(user=request.user.id)) == 0:
            print(Avatar.objects.filter(user=request.user.id))
            message = 'no hay nada'
            return render(request, 'BookRecord/home.html', {'message': message })
        else:
            message = Avatar.objects.filter(user=request.user.id)
            return render(request, 'BookRecord/home.html', {'message': message })
    else:
        message = 'quien sos?'
        return render(request, 'BookRecord/home.html', {'message': message })
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

@login_required
def create_avatar(request):
    if request.method == 'POST':
        my_form = Avatar_form(request.POST, request.FILES)
        if my_form.is_valid():
            u = User.objects.get(username=request.user)
            i = my_form.cleaned_data['image']
            avatar = Avatar(user=u,image=i)
            avatar.save()
            message = 'Avatar subido con éxito'
            return render(request,'BookRecord/home.html', {'message': message})
    else:
        my_form = Avatar_form()

    return render(request,'BookRecord/create_avatar.html', {'my_form':my_form})

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

def search_book(request):
    return render(request, 'BookRecord/search_book.html')

def search_book_action(request):
    if request.GET['title']:
        title = request.GET['title']
        results = Book.objects.filter(title__icontains=title)
        return render(request,'BookRecord/search_book_results.html',{'results':results,'title':title})
    else:
        answer = 'No se enviaron datos'
    return HttpResponse(answer)

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

def search_author(request):
    return render(request, 'BookRecord/search_author.html')

def search_author_action(request):
    if request.GET['name']:
        name = request.GET['name']
        results = Author.objects.filter(name__icontains=name)
        #print(len(results))
        print(name)
        return render(request,'BookRecord/search_author_results.html',{'results':results,'name':name})
    else:
        answer = 'No se enviaron datos'
    return HttpResponse(answer)

# comment model
class View_comments(ListView):
    model = Comment
    template_name = 'BookRecord/comment_list.html'

class Detail_comment(DetailView):
    model = Comment
    template_name = 'BookRecord/comment_detail.html'

class Create_comment(LoginRequiredMixin, CreateView):
    model = Comment
    success_url = '/BookRecord/comment/list/'
    fields = ['title','book','rating','comment']

class Update_comment(LoginRequiredMixin, UpdateView):
    model = Comment
    success_url = '/BookRecord/comment/list/'
    fields = ['title','book','rating','comment']

class Delete_comment(LoginRequiredMixin, DeleteView):
    model = Comment
    success_url = '/BookRecord/comment/list/'

def search_comment(request):
    return render(request, 'BookRecord/search_comment.html')

def search_comment_action(request):

    if request.GET['title']:
        title = request.GET['title']
        results = Comment.objects.filter(title__icontains=title)
        return render(request,'BookRecord/search_comment_results.html',{'results':results,'title':title})
#    if request.GET['book']:
#        book = request.GET['book']
#        results = Comment.objects.filter(book__icontains=name)
#        return render(request,'BookRecord/search_comment_results.html',{'results':results,'book':book})
    else:
        answer = 'No se enviaron datos'
    return HttpResponse(answer)

# About

def aboutme(request):
    return render(request, 'BookRecord/about_me.html')
