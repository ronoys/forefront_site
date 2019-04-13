# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Post


def home(request):
    #return HttpResponse('<h1>Blog Home</h1>') # just print explicit html
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'blog/home.html', context) # print the html file

def about(request):
    #return HttpResponse('<h2> Blog About </h2>')
    return render(request,'blog/about.html')
