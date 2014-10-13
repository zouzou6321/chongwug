# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import adapters
MARKET_ROOT='/market/'

def manage_login(request):
    return render_to_response('market/tpl/manage_login.html')

#auth:huhuaiyong
#date:2014/8/23
#discription:管理员首页展示
def manage_home_view(request):
    if request.method == 'GET' and 'username' in request.GET and 'userpassd'  in request.GET:
        if adapters.manage_login_check(request) == True:
            return HttpResponseRedirect(MARKET_ROOT)
    if request.method == 'GET' and 'logout' in request.GET:
        del request.session['manage_id']
        del request.session['score']
        return HttpResponseRedirect(MARKET_ROOT)
    if adapters.manage_authentication(request) == False:
        return manage_login(request)
    data = adapters.manage_home_data_get(request)
    return render_to_response('market/tpl/manage_home.html',data)

def market_usr_attention_info_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MARKET_ROOT)
    if request.session['score'] < 20:
        return HttpResponse("Page Not Find!!!")
    data = adapters.manage_home_data_get(request)
    return render_to_response('market/tpl/market_attentions.html',data)

@csrf_exempt
def market_usr_attention_mod_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MARKET_ROOT)
    if request.session['score'] < 20:
        return HttpResponse("Page Not Find!!!")
    data = adapters.market_attention_mod(request)
    return HttpResponse(data)

def market_nestofpet_info_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MARKET_ROOT)
    if request.session['score'] < 20:
        return HttpResponse("Page Not Find!!!")
    if 'id' and 'sale' in request.GET:
        return HttpResponse(adapters.market_nestofpet_sale_set(request))
    data = adapters.manage_home_data_get(request)
    data['infos'] = adapters.market_nestofpet_info_get(request)
    return render_to_response('market/tpl/market_nestofpet_info.html',data)