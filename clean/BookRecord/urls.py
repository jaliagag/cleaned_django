#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from BookRecord import views


urlpatterns = [
    path('',views.template, name='home'),
    path('dev/',views.dev, name='dev'),
    #path('book/add/', views.Create_book.as_view(), name='create'),
    path('add/', views.testform, name='create'),
    path('book/list/', views.View_books.as_view(), name='list'),
]
