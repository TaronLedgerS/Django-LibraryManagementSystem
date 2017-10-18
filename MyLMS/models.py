# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    Title = models.CharField(max_length=64,default='')
    Author = models.CharField(max_length=32, default='')
    ISBN = models.CharField(max_length=32, default='')
    Publisher = models.CharField(max_length=32, default='')
    Pub_Time = models.DateField(null=True)
    Pages = models.IntegerField(null=True)
    Description = models.TextField(null=True)
    Number = models.IntegerField(default=1)
    Position = models.CharField(max_length=8, default='A-101')
    #Modified_Time = models.DateTimeField(auto_now=True)
    #此方法为打印到屏幕上对象的标记为其title值
    def __unicode__(self):
        return self.Title
class Reader(models.Model):
    Name = models.CharField(max_length=64, default='')
    Password = models.CharField(max_length=32, default='')
    def __unicode__(self):
        return self.Name