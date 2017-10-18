# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import  HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from . import models

def welcome_page(request):
    return render(request,'welcome.html')

def home_page(request):
    books = models.Book.objects.all()
    return render(request, 'home.html', {'books': books})

def book_page(request,book_id):
    book = models.Book.objects.get(pk=book_id)
    return render(request,'book_page.html',{'book':book})


'''
def welcome_action(request):
    # 如果点击的是Reader，获取到按钮的value值，如果点击的是Administrator，则submit为None
    submit = request.POST.get('submit_type', None)
    if submit == "Reader":
       books = models.Book.objects.all()
       return render(request, 'home.html', {'books': books})
    else:
        #return HttpResponse('11111111')
        books = models.Book.objects.all()
        render(request, 'home.html', {'books': books})
'''
def search_action(request):
    title = request.POST.get('title', None)
    if title:
        books = models.Book.objects.filter(Title='book1')
        return render(request, 'home.html', {'books': books})
    else:
        books = models.Book.objects.all()
        return render(request, 'home.html', {'books': books})