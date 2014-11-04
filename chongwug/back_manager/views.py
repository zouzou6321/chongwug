# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import adapters
MANAGE_ROOT='/back_manage/'
def manage_login(request):
    return render_to_response('manage/tpl/manage_login.html',{},context_instance=RequestContext(request))
#auth:huhuaiyong
#date:2014/8/23
#discription:管理员首页展示
def manage_home_view(request):
    if request.method == 'POST' and 'username' in request.POST and 'userpassd'  in request.POST:
        if adapters.manage_login_check(request) == True:
            return HttpResponseRedirect(MANAGE_ROOT)
    if request.method == 'GET' and 'logout' in request.GET:
        del request.session['name']
        del request.session['passwd']
        return HttpResponseRedirect(MANAGE_ROOT)
    if adapters.manage_authentication(request) == False:
        return manage_login(request)
    data = adapters.manage_home_data_get(request)
    return render_to_response('manage/tpl/manage_home.html',data)

def manage_manager_add_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    if request.method == 'POST':
        if adapters.manage_manager_add(request) == False:
            return HttpResponse("data error occur!!!")
    data = adapters.manage_home_data_get(request)
    return render_to_response('manage/tpl/manage_manager_add.html',data,context_instance=RequestContext(request))

def manage_manager_del_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_manager_del(request)
    if data == True or data == False:
        return HttpResponse(data)
    return render_to_response('manage/tpl/manage_manager_del.html',data)

def manage_adshow_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    data = adapters.manage_home_data_get(request)
    data['adinfo'] = adapters.manage_ad_info(request) 
    if data['adinfo'] == 'False':
        return HttpResponse("删除数据没有成功")
    else:
        return render_to_response('manage/tpl/manage_ad_show.html',data,context_instance=RequestContext(request))
    return render_to_response('manage/tpl/manage_ad_show.html',data,context_instance=RequestContext(request))