# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.utils import simplejson
import adapters
#auth:huhuaiyong
#date:2014/8/16
#discription:导航页面展示
def nav_page_view(request):
    return render_to_response('tpl/nav.html')

#auth:huhuaiyong
#date:2014/8/16
#discription:购宠首页展示
def buy_home_view(request):
    data = adapters.buy_home_adapter(request)
    return render_to_response('tpl/buy_index.html',data)

#auth:renwei
#date:2014/9/8
#discription:购宠购买展示页
def buy_main_view(request):
    data = adapters.buy_home_adapter(request)
    return render_to_response('tpl/buy_main.html',data)
