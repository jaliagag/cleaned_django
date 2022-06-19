#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from BookRecord import views


urlpatterns = [
    path('',views.template, name='home'),
    path('login/', views.login_request, name='login'),

    path('book/add/', views.Create_book.as_view(), name='create_book'),
    path('book/list/', views.View_books.as_view(), name='list_books'),
    path('book/rm/<pk>', views.Delete_book.as_view(), name='delete_book'),
    path('book/<pk>', views.Detail_book.as_view(), name='detail_book'),
    path('book/edit/<pk>', views.Update_book.as_view(), name='update_book'),

]
