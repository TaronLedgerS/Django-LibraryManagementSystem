# -*- coding: utf-8 -*-
from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.welcome_page,name='welcome_page'),
    url(r'^welcome/', views.welcome_page,name='welcome_page'),
    url(r'^home/$', views.home_page,name='home_page'),
    url(r'^book/(?P<book_id>[0-9]+)$', views.book_page,name='book_page'),
    url(r'^home/search/$', views.search_action,name='search_action'),
]