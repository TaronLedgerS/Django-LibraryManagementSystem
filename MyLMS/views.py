# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import  HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from . import models
reader_info ={}

#欢迎界面
def welcome_page(request):
    return render(request,'welcome.html')
#用户首页
def home_page(request):
    books = models.Book.objects.all()
    global reader_info
    return render(request, 'home.html', {'books': books,'reader_info' : reader_info})

#书籍详情页
def book_page(request,book_id):
    book = models.Book.objects.get(pk=book_id)
    global reader_info
    return render(request,'book_page.html',{'book':book,'reader_info' : reader_info})

#借书记录
def record_page(request):
    global reader_info
    records = models.Record.objects.filter(Reader=reader_info.id)
    return render(request,'record_page.html',{'records': records,'reader_info' : reader_info})

#搜索并返回结果
def search_action(request):
    title = request.POST.get('title', None)
    if title:
        books = models.Book.objects.filter(Title=title)
        return render(request, 'home.html', {'books': books})
    else:
        books = models.Book.objects.all()
        return render(request, 'home.html', {'books': books})
def login_page(request):
    return render(request,'login.html',{'line': 'please input your readername and your password!'})

def signup_page(request):
    return render(request,'signup.html',{'line': 'please input your readername and your password!'})

def login_action(request):
    readername = request.POST.get('readername', None)
    readerpwd = request.POST.get('pwd', None)
    if readername :
        if readerpwd:
            reader = models.Reader.objects.get(Name=readername,Password = readerpwd)
            if reader :
                global reader_info
                reader_info = reader
                books = models.Book.objects.all()
                return render(request, 'home.html', {'books': books,'reader_info' : reader_info})
    return render(request, 'login.html', {'line': 'login failure!please checkout your readername and your password!'})

def signup_action(request):
    readername = request.POST.get('readername', None)
    readerpwd = request.POST.get('pwd', None)
    if readername :
        if readerpwd:
            r = models.Reader(Name=readername, Password = readerpwd)
            r.save()
            return render(request, 'login.html', {'line': 'signup Success!'})
    return render(request, 'signup.html', {'line': 'signup failure!please checkout your readername and your password!'})

def borrow_action(request):
    Bookid = request.POST.get('book_id', None)
    book = models.Book.objects.get(pk=Bookid)
    reader = models.Reader.objects.get(pk=reader_info.id)
    if book :
        r = models.Record(Book=book, Reader=reader)
        r.save()
    global reader_info
    records = models.Record.objects.filter(Reader=reader_info.id)
    return render(request, 'record_page.html', {'records': records, 'reader_info': reader_info})