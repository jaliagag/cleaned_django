#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class User_form(forms.Form):
    name = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    shelf = forms.CharField()

class Book_form(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    author = forms.CharField()
    date = forms.DateField()
    pages = forms.IntegerField()
    rating = forms.IntegerField()
    comments = forms.CharField()
    genre = forms.CharField()

class Author_form(forms.Form):
    name = forms.CharField()
    lastname = forms.CharField()
    book = forms.CharField()
    wiki = forms.CharField()
    genre = forms.CharField()

class Shelf_form(forms.Form):
    title = forms.CharField()
    owner = forms.CharField()
    books = forms.CharField()

#class

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:'' for k in fields}
