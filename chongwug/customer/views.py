# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import adapters,traceback,string
from chongwug.commom import __errorcode__,sendSMS,getalipayurl
from manager.adapters import manage_authentication
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from chongwug.settings import WAP_ROOT
from chongwug import config

#auth:huhuaiyong
#date:2014/8/16
#discription:购宠首页展示
def buy_home_view(request):
    
    adapters.UVPVIPtongji(request)
    data = adapters.buy_home_adapter(request)
    if 'visitor' not in request.session:
        request.session['visitor'] = 1
        if not adapters.is_wap(request):
            if adapters.redict_wap(request):
                return HttpResponseRedirect(WAP_ROOT)
        data['visitor'] = True
    else:
        data['visitor'] = False
    data['city'] = adapters.getipcity(request)
    data['title'] = u'首页 | 宠物购交易平台-呵护爱犬和爱犬的您-国内首个活体宠物O2O交易平台'
    data['keywords'] = u'成都买狗网，成都淘狗网，成都宠物交易网，宠物购'
    data['description'] = u'狗狗宠物养殖场销售，创新平台，提供买狗建议，注册芯片，通过与养殖场和客户签订买狗协议，保障爱狗人士权益。提供全程接送养殖场看犬买犬服务。要买哈士奇，泰迪，金毛犬，阿拉斯加，比熊犬，罗威纳，贵宾犬，拉布拉多，史宾格犬，边境牧羊犬，松狮犬，博美犬,买狗，淘狗。宠物GPS定位器。请到宠物购平台。'
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/buy_index.html',data)
    else:
        return render_to_response('tpl/buy_index.html',data)

#auth:renwei
#date:2014/9/8
#discription:购宠购买展示页
def buy_main_view(request,direct='all',type='all',prince='0',age='0',epidemic='all',key='all',curpage='1',farmtype='1'):
    adapters.UVPVIPtongji(request)
    data = adapters.buy_main_adapter(request,direct,type,string.atoi(prince),string.atoi(age),epidemic,key,string.atoi(curpage),string.atoi(farmtype))
    data['title'] = u'狗狗挑选| 宠物购交易平台-成都市%s-国内首个活体宠物O2O交易平台' % (data['title'])
    data['keywords'] = u'成都买宠物狗，纯种健康，精细化维度挑选'
    data['description'] = u'国内最正规的狗狗交易平台，第一个以规范宠物犬市场为目标的宠物狗交易平台。通过平台咨询，确认过后进行预约，去宠物狗繁育基地挑选爱犬，全部宠物为纯种犬（价格在1000-2000），部分为高级血统（父母是赛犬，有参加比赛获奖。价格2000-10000）'
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/buy_main.html',data)
    else:
        return render_to_response('tpl/buy_main.html',data)


def buy_detail_view(request,petid='-1'):
    adapters.UVPVIPtongji(request)
    data = adapters.buy_detail_adapter(request,string.atoi(petid))
    if data == False:
        return render_to_response('500.html')

    if 'locations' in data:
        return HttpResponse(__errorcode__(0,data))
    else:
        data['title'] = u'%s|%s|%s' % (data['nestpet'].type,data['nestpet'].short_desc,data['nestpet'].farm.name)
        data['keywords'] = u'成都买宠物狗，纯种健康，消费者保障协议,免费医院体检，平台接送'
        data['description'] = u'%s|%s|%s' % (data['nestpet'].type,data['nestpet'].short_desc,data['nestpet'].farm.name)
        if adapters.is_wap(request):
            return render_to_response('mobile/tpl/buy_detail.html',data,context_instance=RequestContext(request))
        else:
            if manage_authentication(request) == True and request.session['score'] >= 50:
                data['manager'] = True
            return render_to_response('tpl/buy_detail.html',data,context_instance=RequestContext(request))

def buy_gettel_view(request):
    adapters.UVPVIPtongji(request)
    return HttpResponse(adapters.buy_gettel(request))
        

def buy_attention_sendsms_view(request):
    adapters.UVPVIPtongji(request)
    return HttpResponse(adapters.attention_sendsms(request))

def buy_attention_view(request):
    adapters.UVPVIPtongji(request)
    if request.method == 'POST':
        data = adapters.buy_attention_adapter(request)
    else:
        data = adapters.buy_attention_sure(request)
    return HttpResponse(data)

@csrf_exempt
def buy_order_notify_view(request):
    return HttpResponse(adapters.alipay_notify(request))

def knowledge_buy_view(request):
    adapters.UVPVIPtongji(request)
    try:
        data = adapters.get_knowledge_buy(request)
        if 'name' in data or 'idlist' in data:
            return HttpResponse(__errorcode__(0,data))
        pagedata = {}
        pagedata['page'] = 'knowbuy'
        pagedata['knowledges'] = data
        pagedata['title'] = u'购犬必备知识| 宠物购交易平台-让你成为宠物专家-国内首个活体宠物O2O交易平台'
        pagedata['keywords'] = u'买狗知识，辨别宠物，健康识别指导，买狗专业指导'
        pagedata['description'] = u'纯种哈士奇，纯种泰迪，纯种金毛犬，纯种阿拉斯加，纯种比熊犬，纯种罗威纳，纯种贵宾犬，纯种拉布拉多，纯种史宾格犬，纯种边境牧羊犬，纯种松狮犬，纯种博美犬,识别。细小、犬瘟等疾病鉴别。提供宠物喂养初步知识，根据各种狗狗不同的特征，选择最适合自己的宠物狗狗，手把手教您如何购买安全高质量的汪星人回家'
        if adapters.is_wap(request):
            return render_to_response('mobile/tpl/knowledge_buy.html',pagedata)
        else:
            return render_to_response('tpl/knowledge_buy.html',pagedata)
    except:
        traceback.print_exc()
        return HttpResponse('aa')

def knowledge_bringup_view(request):
    adapters.UVPVIPtongji(request)
    pagedata = {}
    pagedata['page'] = 'knowbringup'
    pagedata['title'] = u'宠物喂养| 宠物购交易平台-狗狗饲养必备常识-国内首个活体宠物O2O交易平台'
    pagedata['keywords'] = u'养狗知识，如何养狗，养狗注意事项'
    pagedata['description'] = u'血统哈士奇，血统泰迪，血统金毛犬，血统阿拉斯加，血统比熊犬，血统罗威纳，血统贵宾犬，血统拉布拉多，血统史宾格犬，血统边境牧羊犬，血统松狮犬，血统博美犬,学习如何养好一只狗狗，毛发打理，口水，喂养，食物。笼子的挑选知识。'
    if adapters.is_wap(request):
        pagedata['categorys'] = config.__knowledgetypes
        return render_to_response('mobile/tpl/knowledge_bringup.html',pagedata)
    else:
        pagedata['categorys'] = config.__knowledgetypes
        return render_to_response('tpl/knowledge_bringup.html',pagedata)

def knowledge_bringup_category_view(request,page,category):
    adapters.UVPVIPtongji(request)
    
    pagedata = adapters.get_knowledge_bringup_category(page,category)
    if pagedata == False:
        return render_to_response('404.html')
    pagedata['page'] = 'knowbringup'
    pagedata['title'] = u'宠物喂养| 宠物购交易平台-狗狗饲养必备常识-国内首个活体宠物O2O交易平台'
    pagedata['keywords'] = u'养狗知识，如何养狗，养狗注意事项'
    pagedata['description'] = u'血统哈士奇，血统泰迪，血统金毛犬，血统阿拉斯加，血统比熊犬，血统罗威纳，血统贵宾犬，血统拉布拉多，血统史宾格犬，血统边境牧羊犬，血统松狮犬，血统博美犬,学习如何养好一只狗狗，毛发打理，口水，喂养，食物。笼子的挑选知识。'
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/knowledge_bringup_category.html',pagedata)
    else:
        return render_to_response('tpl/knowledge_bringup_category.html',pagedata)

def knowledge_bringup_detail_view(request,id):
    adapters.UVPVIPtongji(request)
    data = {}
    data['bringup'] = adapters.get_knowledge_bringup_detail(id)
    if data['bringup'] == None:
        return render_to_response('404.html')
    data['page'] = 'knowbringup'
    data['title'] = u'宠物喂养| 宠物购交易平台-%s-国内首个活体宠物O2O交易平台' % (data['bringup'].title)
    data['keywords'] = u'养狗知识，如何养狗，养狗注意事项,狗狗护理'
    data['description'] = data['bringup'].content
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/knowledge_bringup_detail.html',data)
    else:
        return render_to_response('tpl/knowledge_bringup_detail.html',data)
def supplie_view(request):
    adapters.UVPVIPtongji(request)
    data = {}
    data['supplies'] = adapters.get_supplies()
    data['page'] = 'supplie'
    data['title'] = u'宠物用品| 宠物购交易平台-宠物生活一条龙服务-国内首个活体宠物O2O交易平台'
    data['keywords'] = u'宠物用品，推荐用品，必备用品，日常用品'
    data['description'] = u'GPS定位器，追踪器，防止狗狗丢失。生活必备用品，洗漱用品，运动多功能项圈。狗粮。只要是您需要的，我们都去给您挑选，物美价廉。您的狗狗健康可爱，聪明机灵，就是我们的目标。'
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/supplie.html',data)
    else:
        return render_to_response('tpl/supplie.html',data)

def contactus_view(request):
    adapters.UVPVIPtongji(request)
    data = {}
    data['title'] = u'联系宠物购| 宠物购交易平台-国内首个活体宠物O2O交易平台'
    data['keywords'] = u'宠物购官方，联系方式'
    data['description'] = u'宠物购针对本地青年，老人，提供健康、安全、透明的宠物狗购买交易。欢迎各大养殖场联系我们洽谈合作事宜。'
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/contactus.html',data)
    else:
        return render_to_response('tpl/contactus.html',data)

def workchance_view(request):
    adapters.UVPVIPtongji(request)
    data = {}
    data['title'] = u'宠物购招聘| 宠物购交易平台-国内首个活体宠物O2O交易平台'
    data['keywords'] = u'宠物购招聘,加入宠物购'
    data['description'] = u'宠物购针对本地青年，老人，提供健康、安全、透明的宠物狗购买交易。我们提供高于本地薪酬水平的工资福利 ，营造互联网文化浓郁的的公司氛围.'
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/workchance.html',data)
    else:
        return render_to_response('tpl/workchance.html',data)

def aboutus_view(request):
    adapters.UVPVIPtongji(request)
    data = {}
    data['title'] = u'关于宠物购|宠物购怎么样 宠物购交易平台-国内首个活体宠物O2O交易平台'
    data['keywords'] = u'宠物购针对本地青年，老人，提供健康、安全、透明的宠物狗购买交易。宠物购卖的不是狗，是生活的伴侣，心灵的港湾。'
    data['description'] = u'关于宠物购,宠物购怎么样 '
    if adapters.is_wap(request):
        return render_to_response('mobile/tpl/aboutus.html',data)
    else:
        return render_to_response('tpl/aboutus.html',data)

def changecity_view(request):
    adapters.UVPVIPtongji(request)
    if 'ipcity' and 'ipprovince' in request.GET:
        adapters.setipcity(request)
        return HttpResponseRedirect('/')
    data = {}
    data['title'] = u'城市切换|宠物购怎么样 宠物购交易平台-国内首个活体宠物O2O交易平台'
    data['keywords'] = u''
    data['description'] = u'城市切换'
    data['addresses'] = config.__addresses
    return render_to_response('tpl/changecity.html',data)

def adclicktongji_view(request):
    return HttpResponse(adapters.ADclicktongji(request))

def uvtongji_view(request):
    return HttpResponse(adapters.UVPVIPtongji(request))