# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
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
    data = adapters.buy_main_adapter(request)
    return render_to_response('tpl/buy_main.html',data)


def buy_detail_view(request):
    data = adapters.buy_detail_adapter(request)
    if data == False:
        return HttpResponse("DATA ERROR")
    if 'pets_imgs' not in data:
        return render_to_response('tpl/buy_detail.html',data)
    else:
        return render_to_response('tpl/buy_detail_ajax.html',data)

def buy_attention_view(request):
    data = adapters.buy_attention_adapter(request)
    return HttpResponse(data)