from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    email = models.EmailField()
    password = models.CharField(max_length=40)
    shelf = models.CharField(max_length=40)
    def __str__(self):
        return f'name: {self.name} - \
                 lastname: {self.lastname} - \
                 email: {self.email} - \
                 password: {self.password} - \
                 shelf: {self.shelf}'

class Book(models.Model):
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    author = models.CharField(max_length=40)
    date = models.DateField(max_length=40)
    pages = models.IntegerField()
    rating = models.IntegerField()
    comments = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)

    def __str__(self):
        return f'title: {self.title} - \
                 description: {self.description} - \
                 author: {self.author} - \
                 date: {self.date} - \
                 pages: {self.pages} - \
                 rating: {self.rating} - \
                 comments: {self.comments} - \
                 genre: {self.genre}'

class Author(models.Model):
    name = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    book = models.CharField(max_length=40)
    wiki = models.CharField(max_length=40)
    genre = models.CharField(max_length=40)
    def __str__(self):
        return f'name: {self.name} - \
                 lastname: {self.lastname} - \
                 book: {self.book} - \
                 wiki: {self.wiki} - \
                 genre: {self.genre}'

class Shelf(models.Model):
    title = models.CharField(max_length=40)
    owner = models.CharField(max_length=40)
    books = models.CharField(max_length=40)
    def __str__(self):
        return f'title: {self.title} - \
                 owner: {self.owner} - \
                 books: {self.books}'

class Comment(models.Model):
    title = models.CharField(max_length=40)
    book = models.CharField(max_length=40)
    rating = models.IntegerField()
    comment = models.CharField(max_length=200)
    def __str__(self):
        return f'title: {self.title} - \
                 book: {self.book} - \
                 rating: {self.rating} - \
                 comment: {self.comment}'

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars', null=True, blank=True)
