#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from BookRecord import views
from django.contrib.auth.views import LogoutView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.template, name='home'),
    path('login/', views.login_request, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name='BookRecord/logout.html'), name='logout'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),

    path('book/search/', views.search_book, name='search_book'),
    path('search/book/',views.search_book_action),
    path('book/add/', views.Create_book.as_view(), name='create_book'),
    path('book/list/', views.View_books.as_view(), name='list_books'),
    path('book/rm/<pk>', views.Delete_book.as_view(), name='delete_book'),
    path('book/<pk>', views.Detail_book.as_view(), name='detail_book'),
    path('book/edit/<pk>', views.Update_book.as_view(), name='update_book'),

    path('author/search/', views.search_author, name='search_author'),
    path('search/author/',views.search_author_action),
    path('author/add/', views.Create_author.as_view(), name='create_author'),
    path('author/list/', views.View_authors.as_view(), name='list_authors'),
    path('author/rm/<pk>', views.Delete_author.as_view(), name='delete_author'),
    path('author/<pk>', views.Detail_author.as_view(), name='detail_author'),
    path('author/edit/<pk>', views.Update_author.as_view(), name='update_author'),

    path('avatar_create',views.create_avatar,name='create_avatar'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
