#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.urls import path
from BookRecord import views

urlpatterns = [
    path('',views.template),
]
