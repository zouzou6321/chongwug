# -*- coding: UTF-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
import adapters,traceback
from petlife.commom import __errorcode__
from django.template import RequestContext
from petlife.config import __pettypes
CURRENT_NAME = 'petmicro'
def home(req):
    if adapters.authcheck(req):
        if req.method == 'POST':
            return HttpResponse(adapters.home(req))
        data = {}
        data['types'] = __pettypes
        return render_to_response('%s/tpl/home.html' % CURRENT_NAME,data)
    else:
        if req.method == 'POST':
            data = adapters.home_unlogin(req)
            if data == False:
                return render_to_response('%s/tpl/search.html' % CURRENT_NAME,{'error':True})
            else:
                return render_to_response('%s/tpl/home_unlogin.html' % CURRENT_NAME,{'error':False,'pet':data})
        return render_to_response('%s/tpl/search.html' % CURRENT_NAME,{'error':False})
        
def login(req):
    if req.method == 'POST':
        data = adapters.login(req)
        if data:
            return HttpResponseRedirect("/%s/" % CURRENT_NAME)
        else:
            return render_to_response('%s/tpl/login.html' % CURRENT_NAME,{'error':True})
    if adapters.authcheck(req):
        if 'logout' in req.GET and req.REQUEST.get('logout') == '1':
            del req.session['user_id']
            return render_to_response('%s/tpl/login.html' % CURRENT_NAME,{'error':False})
        return HttpResponseRedirect("/%s/" % CURRENT_NAME)
    return render_to_response('%s/tpl/login.html' % CURRENT_NAME,{'error':False})

def pwdback(req):
    if req.method == 'POST':
        return HttpResponse(adapters.pwdback(req))
    return render_to_response('%s/tpl/pwdback.html' % CURRENT_NAME,{'error':False})