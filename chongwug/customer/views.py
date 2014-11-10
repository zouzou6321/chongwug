# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import adapters,traceback,string
from chongwug.commom import __errorcode__,sendSMS
from django.template import RequestContext
#auth:huhuaiyong
#date:2014/8/16
#discription:导航页面展示
from django.core.mail  import  send_mail
def nav_page_view(request):
    if 'visitor' not in request.session:
        request.session['visitor'] = 1
        data = {}
        data['title'] = u'宠物购 |创新的宠物狗狗交易平台，全面保障购犬用户的经济、身心利益'
        data['description'] = u'宠物购平台是一个新成立的平台，立志于降低爱犬人士购犬成本，包括经济成本，时间成本以及心理成本。通过人工筛选的方式，为用户提供健康实惠的购犬养犬一站式服务。健康有保障，价格很公道，品相很优质，流程很标准，赶紧去挑选吧。'
        return render_to_response('tpl/nav.html',data)
    else:
        return HttpResponseRedirect('/home/')

#auth:huhuaiyong
#date:2014/8/16
#discription:购宠首页展示
def buy_home_view(request):
    data = adapters.buy_home_adapter(request)
    data['title'] = u'首页 |宠物服务推荐，四川成都市选择精选养殖场购犬 '
    data['description'] = u'成都市城南精品养殖场购犬，成都市城 北精品养殖场购宠犬，成都市城西精品养殖场购犬，成都市城东精品养殖场购犬。'
    return render_to_response('tpl/buy_index.html',data)

#auth:renwei
#date:2014/9/8
#discription:购宠购买展示页
def buy_main_view(request):
    data = adapters.buy_main_adapter(request)
    data['title'] = u'购犬|通过宠物犬品种、颜色、月龄、疫苗、价格、养殖场位置等筛选宠物 '
    data['description'] = u'目前平台支持成都市区和周边养殖场直接购犬，喜欢宠物狗狗的您，为了狗狗的健康，我们建议您选择就近的养殖场购犬，禁止跨城市购犬。'
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
        data['title'] = u'%s|%s|%s' % (data['nestpet'].type,data['nestpet'].short_desc,data['nestpet'].farm.name)
        data['description'] = data['nestpet'].txt_desc
        return render_to_response('tpl/buy_detail.html',data,context_instance=RequestContext(request))

def buy_attention_sendsms_view(request):
    return HttpResponse(adapters.attention_sendsms(request))

def buy_attention_view(request):
    if request.method == 'POST':
        data = adapters.buy_attention_adapter(request)
    else:
        data = adapters.buy_attention_sure(request)
    return HttpResponse(data)

def knowledge_buy_view(request):
    try:
        data = adapters.get_knowledge_buy(request)
        if 'name' in data or 'idlist' in data:
            return HttpResponse(__errorcode__(0,data))
        pagedata = {}
        pagedata['page'] = 'knowbuy'
        pagedata['knowledges'] = data
        pagedata['title'] = u'购犬须知|收集各类犬种多方面的数据，让购犬用户根据自身条件和生活环境选择适合自己的宠物狗狗'
        pagedata['description'] = u'提供市场价格、体重，智商排名、是否掉毛、是否粘人、是否有攻击型，城市生活适应程度、是否吠叫、活泼程度，等多方面二十几个维度的数据以供参考。'
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
        return render_to_response('tpl/knowledge_bringup_ajax.html',{'knowledges':data,'pageid':pageid})
    pagedata = {}
    pagedata['page'] = 'knowbringup'
    pagedata['knowledges'] = data
    pagedata['title'] = u'养犬必知|收集整理狗狗养护知识，提供养护指导'
    pagedata['description'] = u'狗狗带回家之前你要做好以下准备工作，狗狗带回家后2周以内必须严格按以下方式饲养，狗狗日常饲养必备常识'
    return render_to_response('tpl/knowledge_bringup.html',pagedata)

def supplie_view(request):
    data = {}
    data['supplies'] = adapters.get_supplies()
    data['page'] = 'supplie'
    data['title'] = u'宠物用品|精选必备用品，生活用品，保健医疗，清洁卫生物品 '
    data['description'] = u'人工精选高性价比，质量可靠，销量领先的宠物用品，让用户不用花冤枉钱走冤枉路。客户放心，我们安心'
    return render_to_response('tpl/supplie.html',data)

def contactus_view(request):
    return render_to_response('tpl/contactus.html')

def workchance_view(request):
    return render_to_response('tpl/workchance.html')

def aboutus_view(request):
    return render_to_response('tpl/aboutus.html')