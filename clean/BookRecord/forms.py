#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

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

