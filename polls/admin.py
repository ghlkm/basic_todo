# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import TodoEven, User
# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     fields=['userName', 'password']

class TodoEvenAdmin(admin.ModelAdmin):
    fields= [   'user',
                'title',
                'startTime',
                'exceedTime',
                'content',
                'priority',
                'isFinish'
    ]
    list_display = ('user', 
                    'title', 
                    'startTime', 
                    'exceedTime', 
                    'priority', 
                    'isFinish')
    list_filter=['priority']
    search_fields=['title']
    list_per_page=10
admin.site.register(User)

admin.site.register(TodoEven, TodoEvenAdmin)