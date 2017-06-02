# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from djnago.http import HttpResponse

def index(request):
    return HttpResponse("hello,world. you're at the poll index")