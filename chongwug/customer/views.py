# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import adapters
from chongwug.commom import __errorcode__
from django.template import RequestContext
#auth:huhuaiyong
#date:2014/8/16
#discription:导航页面展示
def nav_page_view(request):
    return render_to_response("tpl/delay.html")
    if 'visitor' not in request.session:
        request.session['visitor'] = 1
        return render_to_response('tpl/nav.html')
    else:
        return HttpResponseRedirect('/home/')

#auth:huhuaiyong
#date:2014/8/16
#discription:购宠首页展示
def buy_home_view(request):
    if 'visitor' not in request.session:
        request.session['visitor'] = 1
    data = adapters.buy_home_adapter(request)
    return render_to_response('tpl/buy_index.html',data)

#auth:renwei
#date:2014/9/8
#discription:购宠购买展示页
def buy_main_view(request):
    if 'visitor' not in request.session:
        request.session['visitor'] = 1
    data = adapters.buy_main_adapter(request)
    return render_to_response('tpl/buy_main.html',data)


def buy_detail_view(request):
    if 'visitor' not in request.session:
        request.session['visitor'] = 1
    data = adapters.buy_detail_adapter(request)
    if data == False:
        return HttpResponse(__errorcode__(2))
    
    if 'pets_imgs' in data:
        return render_to_response('tpl/buy_detail_ajax.html',data)
    elif 'html' in data:
        return HttpResponse(__errorcode__(0,data))
    else:
        return render_to_response('tpl/buy_detail.html',data,context_instance=RequestContext(request))

def buy_attention_view(request):
    if 'visitor' not in request.session:
        request.session['visitor'] = 1
    data = adapters.buy_attention_adapter(request)
    return HttpResponse(data)

def knowledge_buy_view(request):
    return render_to_response('tpl/knowledge_buy.html',{'page':'knowbuy'})