# -*- coding: utf-8 -*-
from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^$', views.welcome_page,name='welcome_page'),
    url(r'^welcome/', views.welcome_page,name='welcome_page'),
    url(r'^home/$', views.home_page,name='home_page'),

    url(r'^book/(?P<book_id>[0-9]+)$', views.book_page,name='book_page'),
    url(r'^home/search/$', views.search_action,name='search_action'),

    url(r'^login/$', views.login_page,name='login_page'),
    url(r'^login/1$', views.login_action,name='login_action'),
    url(r'^record/$', views.record_page,name='record_page'),
    url(r'^record/borrow$', views.borrow_action,name='borrow_action'),
    url(r'^signup/$', views.signup_page,name='signup_page'),
    url(r'^signup/1$', views.login_action,name='signup_action'),

]