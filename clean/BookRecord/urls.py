#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from BookRecord import views


urlpatterns = [
    path('',views.template, name='home'),
    #path('book/add/', views.Create_book.as_view(), name='create'),
    path('book/add/', views.testform, name='create_book'),
    path('book/list/', views.View_books.as_view(), name='list_books'),

]
