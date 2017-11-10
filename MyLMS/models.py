# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

#书库
class Book(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Book_ID')
    Available = models.BooleanField(default=1)
    Title = models.CharField(max_length=64,default='')
    Author = models.CharField(max_length=32, default='')
    ISBN = models.CharField(max_length=32, default='')
    Publisher = models.CharField(max_length=32, default='')
    Pub_Time = models.DateField(null=True)
    Pages = models.IntegerField(null=True)
    Description = models.TextField(null=True)
    Position = models.CharField(max_length=8, default='A-101')
    #Modified_Time = models.DateTimeField(auto_now=True)
    #此方法为打印到屏幕上对象的标记为其title值
    def __unicode__(self):
        return  str(self.id)

class Reader(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Reader_ID')
    Name = models.CharField(max_length=16, null=False,unique=True)
    Password = models.CharField(max_length=16, null=False)
    Active = models.BooleanField(default=1)
    def __unicode__(self):
        return str(self.id)

class Record(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Record_ID')
    Book = models.ForeignKey('Book',on_delete=models.CASCADE,related_name="The_Book")
    Reader = models.ForeignKey('Reader',on_delete=models.CASCADE,)
    Created_time = models.DateTimeField(auto_now_add = True)
    Modified_time = models.DateTimeField(auto_now=True)

    WAITFORCHECK = 'WAITFORCHECK'
    BORROWED = 'BORROWED'
    RETURNED = 'RETURNED'
    TURNDOWN = 'TURNDOWN'
    STATUS_CHOICES = (
        ( WAITFORCHECK, 'WAITFORCHECK'),
        ( BORROWED , 'BORROWED'),
        ( RETURNED , 'RETURNED'),
        ( TURNDOWN , 'TURNDOWN'),
    )
    Status = models.CharField(
        max_length=16,
        choices=STATUS_CHOICES,
        default=WAITFORCHECK,
    )

    def __unicode__(self):
        return str(self.id)