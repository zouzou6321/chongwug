# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson

#auth:huhuaiyong
#date:2014/8/16
#discription:导航页面展示
def nav_page_view(request):
    return render_to_response('tpl/nav.html')

#auth:huhuaiyong
#date:2014/8/16
#discription:购宠首页展示
def buy_home_view(request):
    return render_to_response('tpl/buy_index.html')