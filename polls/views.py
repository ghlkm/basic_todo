# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from polls.models import User, TodoEven
from polls.serializers import UserSerializer, TodoEvenSerializer
from rest_framework import generics
class UserListCreate(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class TodoEvenListCreate(generics.ListCreateAPIView):
    queryset=TodoEven.objects.all()
    serializer_class=TodoEvenSerializer

# Create your views here.
def index(request):
    result = TodoEven.objects.order_by('title')
    output = ', '.join([p.title for p in result])
    return HttpResponse(output)


def detail(request, todoEven_id):
    return HttpResponse("You're looking at todo even%s." % todoEven_id)


def id(request, todoEven_id):
    return HttpResponse("You're looking at todo even%s." % todoEven_id)

