# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import adapters,traceback
from chongwug.commom import __errorcode__
from django.template import RequestContext
#auth:huhuaiyong
#date:2014/8/16
#discription:导航页面展示
from django.core.mail  import  send_mail
def nav_page_view(request):
    if 'visitor' not in request.session:
        request.session['visitor'] = 1
        return render_to_response('tpl/nav.html')
    else:
        return HttpResponseRedirect('/home/')

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
        return HttpResponse(__errorcode__(2))
    
    if 'pets_imgs' in data:
        return render_to_response('tpl/buy_detail_ajax.html',data)
    elif 'locations' in data:
        return HttpResponse(__errorcode__(0,data))
    else:
        return render_to_response('tpl/buy_detail.html',data,context_instance=RequestContext(request))

def buy_attention_view(request):
    data = adapters.buy_attention_adapter(request)
    return HttpResponse(data)

def knowledge_buy_view(request):
    try:
        data = adapters.get_knowledge_buy(request)
        if 'name' in data or 'idlist' in data:
            return HttpResponse(__errorcode__(0,data))
        return render_to_response('tpl/knowledge_buy.html',{'page':'knowbuy','knowledges':adapters.get_knowledge_buy(request)})
    except:
        traceback.print_exc()
        return HttpResponse('aa')

def knowledge_bringup_view(request):
    return render_to_response('tpl/knowledge_bringup.html',{'page':'knowbringup'})

def supplie_view(request):
    return render_to_response('tpl/supplie.html',{'page':'supplie'})

def contactus_view(request):
    return render_to_response('tpl/contactus.html')

def workchance_view(request):
    return render_to_response('tpl/workchance.html')

def aboutus_view(request):
    return render_to_response('tpl/aboutus.html')