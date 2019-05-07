# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import json
import datetime
from django.utils import timezone
# Create your models here.
class TodoEven(models.Model):
    user=models.ForeignKey('User', on_delete=models.CASCADE)
    title=models.CharField(max_length=35)
    startTime=models.DateField()
    exceedTime=models.DateField()
    content=models.TextField()
    priority=models.IntegerField()
    isFinish=models.BooleanField()
    def priority_cmp(self):
        pass
    priority_cmp.admin_order_field='-priority'
    priority_cmp.short_desription='sort by priority'
    def __unicode__(self):
        return '{'+self.title+','+self.content+'}'

class User(models.Model):
    userName=models.CharField(max_length=15)
    password=models.CharField(max_length=25)
    def __unicode__(self):
        return self.userName
# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):              # __unicode__ on Python 2
#         return self.question_text
#     def was_published_recently(self):
#         return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



# class Choice(models.Model):
#     question = models.ForeignKey(Question)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):              # __unicode__ on Python 2
#         return self.choice_tex
