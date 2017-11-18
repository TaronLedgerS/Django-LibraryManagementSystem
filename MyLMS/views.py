# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from . import models
from django.db.models import Q,Count,Sum


#欢迎界面
def welcome_page(request):
    return render(request,'welcome.html')

#登陆界面
def login_page(request):
    return render(request,'login.html',{'line': 'Please input your readername and your password!'})

#登陆操作处理
def login_action(request):
    namefield = request.POST.get('namefield', None)
    pwdfield = request.POST.get('pwdfield', None)
    if namefield:
        if pwdfield:
            reader = models.Reader.objects.filter(Name=namefield, Password=pwdfield).first()
            if reader :
                request.session['reader_id'] = reader.id
                request.session.set_expiry(600)
                request.session['reader_name'] = reader.Name
                books = models.Book.objects.all()
                if reader.Active :
                    return render(request, 'index.html',)
                else:
                    return render(request, 'login.html',{'line': 'Please Active your account First!'})
    return render(request, 'login.html', {'line': 'Login failure!Please checkout your readername and your password!'})

#注册界面
def signup_page(request):
    return render(request,'signup.html',{'line': 'Please input your readername and your password!'})


#注册操作处理
def signup_action(request):
    namefield = request.POST.get('namefield', None)
    pwdfield = request.POST.get('pwdfield', None)
    scfield = request.POST.get('scfield', None)
    if namefield :
        r = models.Reader.objects.filter(Name=namefield).first()
        if r:
            return render(request, 'signup.html',
                          {'line': 'Signup failure!Readername has been used!'})
        if scfield:
            r = models.Reader.objects.filter(Name=namefield).first()
            if r:
                return render(request, 'signup.html',
                              {'line': 'Signup failure!StudentCard has been used!'})
        if pwdfield:
            r = models.Reader(Name=namefield, Password = pwdfield,StudentCard = scfield)
            r.save()
            return render(request, 'login.html', {'line': 'Signup Success!'})
    return render(request, 'signup.html', {'line': 'Signup failure!Please checkout your readername and your password!'})

#用户登出
def logout_action(request):
    try:
        del request.session['reader_id']
    except KeyError:
        pass
    return render(request, 'login.html', {'line': 'You have logged out!'})

#用户首页
def index(request):
    if "reader_id" not in request.session:
        return render(request, 'login.html', {'line': 'Please login first!'})
    #最活跃的3个用户
    readers = models.Record.objects.values_list('Reader').annotate(Borrow_num=Count('id')).order_by('-Borrow_num')
    reader = models.Reader.objects.get(pk=readers[0][0])
    Top1={'id':readers[0][0],'name':reader.Name,'Act_times':readers[0][1]}
    reader = models.Reader.objects.get(pk=readers[1][0])
    Top2 = {'id': readers[1][0], 'name': reader.Name, 'Act_times': readers[1][1]}
    reader = models.Reader.objects.get(pk=readers[2][0])
    Top3 = {'id': readers[2][0], 'name': reader.Name, 'Act_times': readers[2][1]}
    #最新增加的7本书记
    Newbooks = models.Book.objects.all().order_by('-id')[0:7]
    #可用/总数目
    sum = models.Book.objects.all().count()
    available = models.Book.objects.filter(Available=True).count()
    per = (float (available) / float (sum) )*100
    booksum = {'sum':sum,'available':available,'per':int(per)}
    #借书记录
    records = models.Record.objects.filter(Reader=request.session["reader_id"]).values_list('Status').annotate(Count('id'))
    BORROWED = 0
    WAITFORCHECK = 0
    TURNDOWN = 0
    DEMAGE = 0
    RETURNED = 0
    for item in records:
        if item[0] == 'BORROWED':
            BORROWED=item[1]
        if item[0] == 'WAITFORCHECK':
            WAITFORCHECK=item[1]
        if item[0] == 'TURNDOWN':
            TURNDOWN=item[1]
        if item[0] == 'DEMAGE':
            DEMAGE=item[1]
        if item[0] == 'RETURNED':
            RETURNED=item[1]
    #罚款总数
    record = models.Record.objects.filter(Reader=request.session["reader_id"])
    t = record.aggregate(Sum('Fine'))['Fine__sum']
    if t:
        TotalFine = t
    else:
        TotalFine = 0
    return render(request,'index.html',{'Top1':Top1,'Top2':Top2,'Top3':Top3,'Newbooks':Newbooks,'booksum':booksum,'TotalFine':TotalFine,'BORROWED':BORROWED,'WAITFORCHECK':WAITFORCHECK,'TURNDOWN':TURNDOWN,'DEMAGE':DEMAGE,'RETURNED':RETURNED})

#图书馆书单
def bookslist(request):
    if "reader_id" in request.session:
        books = models.Book.objects.all()
        booksall = books.count()
        limit = 13  # 每页显示的记录数
        paginator = Paginator(books, limit)  # 实例化一个分页对象
        page = request.GET.get('page')  # 获取页码
        try:
            books = paginator.page(page)  # 获取某页对应的记录
        except PageNotAnInteger:  # 如果页码不是个整数
            books = paginator.page(1)  # 取第一页的记录
        except EmptyPage:  # 如果页码太大，没有相应的记录
            books = paginator.page(paginator.num_pages)  # 取最后一页的记录
        reader = models.Reader.objects.get(pk=request.session["reader_id"])
        return render(request, 'bookslist.html', {'books': books,'booksall': booksall, 'reader' : reader})
    else:
        return render(request, 'login.html', {'line': 'Please login first!'})

# 借书记录
def record_page(request):
    if "reader_id" not in request.session:
        return render(request, 'login.html', {'line': 'Please login first!'})
    records = models.Record.objects.filter(Reader=request.session["reader_id"]).order_by('-Created_time')
    recordsall = records.count()
    limit = 13  # 每页显示的记录数
    paginator = Paginator(records, limit)  # 实例化一个分页对象
    page = request.GET.get('page')  # 获取页码
    try:
        records = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        records = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        records = paginator.page(paginator.num_pages)  # 取最后一页的记录
    return render(request, 'record_page.html', {'records': records,'recordsall': recordsall,'line':"(●'◡'●) Your Borrow Record As Follow :" })

#用户删除申请借书记录
def delete_waiting(request,record_id):
    models.Record.objects.filter(pk=record_id).delete()
    records = models.Record.objects.filter(Reader=request.session["reader_id"])
    recordsall = records.count()
    return render(request, 'record_page.html', {'records': records,'recordsall': recordsall,'line':"(●'◡'●) Delete the borrow request sucessfully:" })


#书籍详情页
def book_page(request,book_id):
    if "reader_id" not in request.session:
        return render(request, 'login.html', {'line': 'Please login first!'})
    book = models.Book.objects.get(pk=book_id)
    return render(request,'book_page.html',{'book':book})

#用户发出借书申请
def borrow_action(request):
    if "reader_id" not in request.session:
        return render(request, 'login.html', {'line': 'Please login first!'})
    Bookid = request.POST.get('book_id', None)
    book = models.Book.objects.get(pk=Bookid)
    # 最多同时借两本书
    records = models.Record.objects.filter(Reader=request.session["reader_id"]).filter(Q(Status='BORROWED')|Q(Status='WAITFORCHECK'))
    if records.count() > 1:
        return render(request, 'book_page.html',
                      {'book': book, 'line': "You have already borrowed or tried to borrow Two book!"})
    # 不能借同一本书
    BookISBN = request.POST.get('book_ISBN', None)
    for record in records:
        if BookISBN == record.Book.ISBN:
            return render(request, 'book_page.html', {'book': book,'line':"You have borrowed or tried to borrow this book!"})

    #正常申请并跳转
    book = models.Book.objects.get(pk=Bookid)
    reader = models.Reader.objects.get(pk=request.session["reader_id"])
    if book :
        r = models.Record(Book=book, Reader=reader)
        r.save()
    records = models.Record.objects.filter(Reader=request.session["reader_id"])
    return render(request, 'record_page.html', {'records': records , 'line':"(●'◡'●) Now you can bring the book and find Libarian to check out:"})



#搜索并返回结果
def search_action(request):
    if "reader_id" in request.session:
        title = request.POST.get('title', None)
        if title:
            books = models.Book.objects.filter(Title=title)
        else:
            books = models.Book.objects.all()
        booksall = books.count()
        limit = 13  # 每页显示的记录数
        paginator = Paginator(books, limit)  # 实例化一个分页对象
        page = request.GET.get('page')  # 获取页码
        try:
            books = paginator.page(page)  # 获取某页对应的记录
        except PageNotAnInteger:  # 如果页码不是个整数
            books = paginator.page(1)  # 取第一页的记录
        except EmptyPage:  # 如果页码太大，没有相应的记录
            books = paginator.page(paginator.num_pages)  # 取最后一页的记录
        reader = models.Reader.objects.get(pk=request.session["reader_id"])
        return render(request, 'bookslist.html', {'books': books,'booksall': booksall, 'reader' : reader})
    else:
        return render(request, 'login.html', {'line': 'Please login first!'})


def settings(request):
    if "reader_id" not in request.session:
        return render(request, 'login.html', {'line': 'Please login first!'})
    reader = models.Reader.objects.get(pk=request.session["reader_id"])
    return render(request,'settings.html',{'reader':reader})
    pass

