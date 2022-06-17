from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.PasswordField(max_length=40)
    shelf = models.CharField(max_length=40)

class Book(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=400)
    author = models.CharField(max_length=40)
    date = models.DateField(max_length=40)
    pages = models.IntegerField()
    rating = models.RealField()
    comments = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)

class Author(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    book = models.CharField(max_length=40)
    wiki = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)

class Shelf(models.Model):
    title = models.CharField(max_length=40)
    owner = models.CharField(max_length=40)
    books = models.CharField(max_length=40)

#class

