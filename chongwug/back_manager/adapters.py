# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from models import manage,supermanager
from manager.models import ad
from customer.models import uvpviptongji,pviptongji
import string
import datetime
import config
from django.contrib.auth.hashers import make_password, check_password
'''
管理员鉴权
'''
def manage_authentication(request):
    try:
        supermanager.objects.get(name=request.session['name'],passwd=request.session['passwd'])
    except:
        return False
    return True

def manage_login_check(request):
    name = request.POST['username']
    passwd = request.POST['userpassd']
    if supermanager.objects.all().count() == 0:
        passwdhash = make_password(passwd,None)
        num_one = supermanager(name=name,passwd=passwdhash)
        num_one.save()
    try:
        superm = supermanager.objects.get(name=name)
        if check_password(passwd,superm.passwd):
            request.session['name'] = name
            request.session['passwd'] = superm.passwd
    except ObjectDoesNotExist:
        print('ObjectDoesNotExist')
        return False
    return True

def manage_home_data_get(request):
    manager = {'name':'超级管理员'}
    return {'manager':manager}

def manage_get_adtypes():
    ad_types = []
    for adtype in config.__adtypes:
        ad_types.append({'value':adtype[1],'text':adtype[2]})
    return ad_types

def manage_ad_info(request):
    if request.method == 'POST':
        try:
            ads_str = request.REQUEST.getlist('ads')
            type = request.POST['adtype']
            ads = ad.objects.filter(type=type,dele=False)
            for tmp_ad in ads_str:
                print ads.count()
                curad = ads.get(id=string.atoi(tmp_ad))
                curad.dele = True
                curad.save()
        except:
            return 'False'
    ad_types = manage_get_adtypes()
    ads = ad.objects.filter(type = config.__adtypes[0][1],dele=False)
    return {'ad_types':ad_types,'ads':ads}

def manage_manager_add(request):
    try:
        new_manage = manage(name = request.POST['name'],
                            passwd = request.POST['passwd'],
                            type = request.POST['type'],
                            permission_score = string.atoi(request.POST['permission_score']))
        new_manage.save()
    except NameError:
        return False
    return True

def manage_manager_del(request):
    if request.method == 'GET' and 'id' in request.GET:
        try:
            print "aaa"
            cumanage = manage.objects.get(id=string.atoi(request.REQUEST.get('id')),dele=False)
            cumanage.dele = True
            cumanage.save()
            return True
        except:
            return False
    return {'managers':manage.objects.filter(dele=False)}

def manage_tongji_get():
    datas = []
    today = datetime.date.today()
    endofday = today + datetime.timedelta(days = 1)
    kwargs = {}
    kwargs['time__lte'] = endofday
    kwargs['time__gte'] = endofday - datetime.timedelta(days = 30)
    pvall = uvpviptongji.objects.filter(**kwargs)
    count = 0
    while count < 30:
        count = count + 1
        kwargs['time__lte'] = endofday
        startofday = endofday - datetime.timedelta(days = 1)
        kwargs['time__gte'] = startofday
        daypv = pvall.filter(**kwargs)
        dayip = daypv.values('ip').distinct()
        dayuv = daypv.values('uv').distinct()
        print 'pv:%d,uv:%d,ip:%d' % (daypv.count(),dayuv.count(),dayip.count())
        datas.append({'time':'%d/%d/%d' % (startofday.year,startofday.month,startofday.day),'pv':daypv.count(),'ip':dayip.count(),'uv':dayuv.count()})
        endofday = startofday
    
    return datas