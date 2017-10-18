# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Book,Reader

class BooksAdmin(admin.ModelAdmin):
    list_display = ('Title','Author','ISBN','Publisher','Pages','Pub_Time','Position','Number')
    list_filter = ('Pub_Time','Position',)

admin.site.register(Book,BooksAdmin)

class ReadersAdmin(admin.ModelAdmin):
    list_display = ('Name','Password')
admin.site.register(Reader,ReadersAdmin)



