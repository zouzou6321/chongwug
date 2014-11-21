# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import adapters,traceback,string
from chongwug.commom import __errorcode__,sendSMS,getalipayurl
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

#auth:huhuaiyong
#date:2014/8/16
#discription:导航页面展示
from django.core.mail  import  send_mail
def nav_page_view(request):
    if 'visitor' not in request.session:
        request.session['visitor'] = 1
        data = {}
        data['title'] = u'宠物交易平台'
        data['description'] = u'国内首个活体宠物O2O交易平台'
        if adapters.is_wap(request):
            return render_to_response('mobile/tpl/nav.html',data)
        else:
            return render_to_response('tpl/nav.html',data)
    else:
        return HttpResponseRedirect('/home/')

#auth:huhuaiyong
#date:2014/8/16
#discription:购宠首页展示
def buy_home_view(request):
    data = adapters.buy_home_adapter(request)
    data['title'] = u'宠物犬交易平台'
    data['description'] = u'专注宠物犬交易'
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/buy_index.html',data)
    else:
        return render_to_response('tpl/buy_index.html',data)

#auth:renwei
#date:2014/9/8
#discription:购宠购买展示页
def buy_main_view(request,direct='all',type='all',prince='0',age='0',epidemic='all',key='all',curpage='1'):
    data = adapters.buy_main_adapter(request,direct,type,string.atoi(prince),string.atoi(age),epidemic,key,string.atoi(curpage))
    data['title'] = u'狗狗挑选'
    data['description'] = u'国内最正规的狗狗交易平台'
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/buy_main.html',data)
    else:
        return render_to_response('tpl/buy_main.html',data)


def buy_detail_view(request,petid='-1'):
    data = adapters.buy_detail_adapter(request,string.atoi(petid))
    if data == False:
        return HttpResponse(__errorcode__(2))

    if 'locations' in data:
        return HttpResponse(__errorcode__(0,data))
    else:
        data['title'] = u'%s|%s|%s' % (data['nestpet'].type,data['nestpet'].short_desc,data['nestpet'].farm.name)
        data['description'] = u'%s|%s|%s' % (data['nestpet'].type,data['nestpet'].short_desc,data['nestpet'].farm.name)
        if adapters.is_wap(request):
            return render_to_response('mobile/tpl/buy_detail.html',data,context_instance=RequestContext(request))
        else:
            return render_to_response('tpl/buy_detail.html',data,context_instance=RequestContext(request))

def buy_attention_sendsms_view(request):
    return HttpResponse(adapters.attention_sendsms(request))

def buy_attention_view(request):
    if request.method == 'POST':
        data = adapters.buy_attention_adapter(request)
    else:
        data = adapters.buy_attention_sure(request)
    return HttpResponse(data)

@csrf_exempt
def buy_order_notify_view(request):
    return HttpResponse(adapters.alipay_notify(request))

def knowledge_buy_view(request):
    try:
        data = adapters.get_knowledge_buy(request)
        if 'name' in data or 'idlist' in data:
            return HttpResponse(__errorcode__(0,data))
        pagedata = {}
        pagedata['page'] = 'knowbuy'
        pagedata['knowledges'] = data
        pagedata['title'] = u'购犬必备知识'
        pagedata['description'] = u'让你成为宠物小专家'
        if adapters.is_wap(request):
            return render_to_response('mobile/tpl/knowledge_buy.html',pagedata)
        else:
            return render_to_response('tpl/knowledge_buy.html',pagedata)
    except:
        traceback.print_exc()
        return HttpResponse('aa')

def knowledge_bringup_view(request):
    data = adapters.get_knowledge_bringup(request)
    if 'page' in request.GET:
        if data.count() > 0:
            pageid = string.atoi(request.REQUEST.get('page')) + 1
        else:
            pageid = False
        if adapters.is_wap(request):
            return render_to_response('mobile/tpl/knowledge_bringup_ajax.html',{'knowledges':data,'pageid':pageid})
        else:
            return render_to_response('tpl/knowledge_bringup_ajax.html',{'knowledges':data,'pageid':pageid})
    pagedata = {}
    pagedata['page'] = 'knowbringup'
    pagedata['knowledges'] = data
    pagedata['title'] = u'宠物喂养'
    pagedata['description'] = u'狗狗饲养必备常识'
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/knowledge_bringup.html',pagedata)
    else:
        return render_to_response('tpl/knowledge_bringup.html',pagedata)

def supplie_view(request):
    data = {}
    data['supplies'] = adapters.get_supplies()
    data['page'] = 'supplie'
    data['title'] = u'宠物用品'
    data['description'] = u'宠物生活一条龙服务'
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/supplie.html',data)
    else:
        return render_to_response('tpl/supplie.html',data)

def contactus_view(request):
    data = {}
    data['description'] = u'联系我们'
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/contactus.html',data)
    else:
        return render_to_response('tpl/contactus.html',data)

def workchance_view(request):
    data = {}
    data['description'] = u'工作机会'
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/workchance.html',data)
    else:
        return render_to_response('tpl/workchance.html',data)

def aboutus_view(request):
    data = {}
    data['description'] = u'关于我们'
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/aboutus.html',data)
    else:
        return render_to_response('tpl/aboutus.html',data)