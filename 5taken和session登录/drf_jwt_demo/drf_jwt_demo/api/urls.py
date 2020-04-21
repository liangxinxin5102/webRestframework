#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url, include
from api import views

urlpatterns = [
    url('^login/$', views.LoginView.as_view()),
    url('^order/$', views.OrderView.as_view()),
]
