# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
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

def market_attention_data_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MARKET_ROOT)
    if request.session['score'] < 20:
        return render_to_response('404.html')
    return HttpResponse(adapters.attention_data(request))

def market_usr_attention_info_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MARKET_ROOT)
    if request.session['score'] < 20:
        return render_to_response('404.html')
    data = adapters.manage_home_data_get(request)
    data['page'] = 'attention'
    return render_to_response('market/tpl/market_attentions.html',data)

def market_usr_processed_info_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MARKET_ROOT)
    if request.session['score'] < 20:
        return render_to_response('404.html')
    data = adapters.manage_home_data_get(request)
    data['page'] = 'processed'
    return render_to_response('market/tpl/market_processed.html',data)

def market_usr_untreated_info_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MARKET_ROOT)
    if request.session['score'] < 20:
        return render_to_response('404.html')
    data = adapters.manage_home_data_get(request)
    data['page'] = 'untreated'
    return render_to_response('market/tpl/market_untreated.html',data)

def market_usr_fail_info_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MARKET_ROOT)
    if request.session['score'] < 20:
        return render_to_response('404.html')
    data = adapters.manage_home_data_get(request)
    data['page'] = 'fail'
    return render_to_response('market/tpl/market_fail.html',data)

@csrf_exempt
def market_usr_attention_mod_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MARKET_ROOT)
    if request.session['score'] < 20:
        return render_to_response('404.html')
    data = adapters.market_attention_mod(request)
    return HttpResponse(data)

def market_nestofpet_info_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MARKET_ROOT)
    if request.session['score'] < 20:
        return render_to_response('404.html')
    if 'id' and 'sale' in request.GET:
        return HttpResponse(adapters.market_nestofpet_sale_set(request))
    data = adapters.manage_home_data_get(request)
    data['infos'] = adapters.market_nestofpet_info_get(request)
    data['page'] = 'nestofpet'
    return render_to_response('market/tpl/market_nestofpet_info.html',data)