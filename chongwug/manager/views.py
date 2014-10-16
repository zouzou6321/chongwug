# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import adapters,config
from chongwug.commom import __errorcode__
MANAGE_ROOT='/manage/'

def manage_login(request):
    return render_to_response('manager/tpl/manage_login.html')

#auth:huhuaiyong
#date:2014/8/23
#discription:管理员首页展示
def manage_home_view(request):
    if request.method == 'GET' and 'username' in request.GET and 'userpassd'  in request.GET:
        if adapters.manage_login_check(request) == True:
            return HttpResponseRedirect(MANAGE_ROOT)
    if request.method == 'GET' and 'logout' in request.GET:
        del request.session['manage_id']
        del request.session['score']
        return HttpResponseRedirect(MANAGE_ROOT)
    if adapters.manage_authentication(request) == False:
        return manage_login(request)
    data = adapters.manage_home_data_get(request)
    return render_to_response('manager/tpl/manage_home.html',data)

def manage_pet_farm_add_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    if request.session['score'] < 50:
        return render_to_response('404.html')
    if request.method == 'POST':
        if adapters.manage_pet_farm_add(request) == False:
            return HttpResponse(__errorcode__(2))
    data = adapters.manage_home_data_get(request)
    return render_to_response('manager/tpl/manage_pet_farm_add.html',data,context_instance=RequestContext(request))

def manage_ad_add_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    if request.session['score'] < 50:
        return render_to_response('404.html')
    data = adapters.manage_home_data_get(request)
    ad_types = adapters.manage_get_adtypes()
    data['ad_types'] = ad_types
    return render_to_response('manager/tpl/manage_ad_picadd.html',data,context_instance=RequestContext(request))

@csrf_exempt
def manage_ad_pic_upload_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponse(__errorcode__(404))
    if request.session['score'] < 50:
        return render_to_response('404.html')
    photo = request.FILES.get('Filedata',None)
    return HttpResponse(adapters.manage_picupload(photo,1170,323))

def manage_ad_picpre_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    if request.session['score'] < 50:
        return render_to_response('404.html')
    return HttpResponse(adapters.manage_ad_picpreupload(request))

def manage_ad_del_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    if request.session['score'] < 50:
        return render_to_response('404.html')
    data = adapters.manage_home_data_get(request)
    data['adinfo'] = adapters.manage_ad_del(request) 
    if data['adinfo'] == 'False':
        return HttpResponse(__errorcode__(1))
    else:
        return render_to_response('manager/tpl/manage_ad_del.html',data,context_instance=RequestContext(request))

def manage_ad_select_view(request):
    if adapters.manage_authentication(request) == False:
        return HttpResponseRedirect(MANAGE_ROOT)
    if request.session['score'] < 50:
        return render_to_response('404.html')
    return HttpResponse(adapters.manage_ad_select(request))