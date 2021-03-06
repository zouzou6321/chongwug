# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from back_manager.models import manage
from manager.models import ad,tmppic_monitor,supplies,pclady
from customer.models import user
from petfarm.models import pet_farm,nestofpet
from PIL import Image
from chongwug import settings
from upyun import UpYun
from django.contrib.auth.models import User
import string,re
import os,uuid,datetime
import config
from django import forms
from chongwug.commom import __errorcode__,myCKEditorWidget
from chongwug import config
'''
管理员鉴权
'''
def manage_authentication(request):
    try:
        if (request.session['manage_id'] == ''):
            return False
    except:
        return False
    return True

def manage_login_check(request):
    name = request.POST['username']
    passwd = request.POST['userpassd']
    request.session['manage_id'] = ''
    try:
        _manage = manage.objects.get(name=name,passwd=passwd)
    except ObjectDoesNotExist:
        print('ObjectDoesNotExist')
        return False
    request.session['manage_id'] = _manage.id
    request.session['score'] = _manage.permission_score
    return True

def manage_home_data_get(request):
    manager = manage.objects.get(id=request.session['manage_id'])
    return {'manager':manager,'directs':config.__directs}

def addressHandle(re):
    if 'province' in re.GET:
        addresses = config.__addresses[string.atoi(re.REQUEST.get('range'))]['sublist'][string.atoi(re.REQUEST.get('province'))]
        if 'city' in re.GET:
            addresses = addresses['sublist'][string.atoi(re.REQUEST.get('city'))]
            arr = []
            for address in addresses['sublist']:
                arr.append({'id': address['index'], 'name': address['name']})
            return {'districts': arr}
        else:
            citys = []
            districts = []
            for _city in addresses['sublist']:
                citys.append({'id': _city['index'], 'name': _city['name']})
            for _district in addresses['sublist'][0]['sublist']:
                districts.append({'id': _district['index'], 'name': _district['name']})
            return {'citys':citys, 'districts':districts}
    provinces = []
    citys = []
    districts = []
    for _addresse in config.__addresses:
        rangeid = _addresse['index']
        _provinces = _addresse['sublist']
        for _province in _provinces:
            provinces.append({'rangeid':rangeid,'id':_province['index'], 'name':_province['name']})
    for _city in config.__addresses[0]['sublist'][0]['sublist']:
        citys.append({'id': _city['index'], 'name': _city['name']})
    for _district in config.__addresses[0]['sublist'][0]['sublist'][0]['sublist']:
        districts.append({'id': _district['index'], 'name': _district['name']})
    return {'provinces':provinces, 'citys':citys, 'districts':districts}

class descform(forms.Form):
    content = forms.CharField(widget=myCKEditorWidget(),label=u'详细介绍:')

def manage_pet_farm_add(request):
    try:
        if 'pwd' not in request.POST or request.POST['pwd'] == '':
            return __errorcode__(21)
        
        if 'province' not in request.POST or request.POST['province'] == '':
            province = u'四川'
        else:
            province = request.POST['province']
        if 'city' not in request.POST or request.POST['city'] == '':
            city = u'成都'
        else:
            city = request.POST['city']
        
        error = True
        
        for _addresse in config.__addresses:
            for _province in _addresse['sublist']:
                if _province['name'] == province:
                    for _city in _province['sublist']:
                        if _city['name'] == city:
                            for _district in _city['sublist']:
                                if _district['name'] == request.POST['district']:
                                    error = False
                                    break
                            break
                    break
        if error:
            return __errorcode__(11)
        
        error = True
        for _direct in config.__directs:
            if _direct == request.POST['direct']:
                error = False
                break
        if error:
            return __errorcode__(18)
        
        try:
            if request.POST['manage_score'] == '':
                manage_score = 1.0
            else:
                manage_score = string.atof(request.POST['manage_score'])
        except:
            return __errorcode__(19)
        
        p = re.compile(config.__regular_expression_chinatelnum)
        if not p.match(request.POST['tel']):
            return __errorcode__(9)
        p = re.compile(config.__regular_expression_email)
        if not p.match(request.POST['email']):
            return __errorcode__(16)
        p = re.compile(config.__regular_expression_idnum)
        if not p.match(request.POST['idnum']):
            return __errorcode__(17)
        content = descform({'content':request.POST['content']})
        if not content.is_valid():
            return __errorcode__(1)
        auth_user = User.objects.create_user(username=request.POST['name'],email=request.POST['email'],password=request.POST['pwd'])
        new_user = user(nickname = request.POST['name'],
                        tel = request.POST['tel'],
                        email = request.POST['email'],
                        id_num = request.POST['idnum'],
                        type = 1,
                        auth_user=auth_user,
                        pwd = request.POST['pwd'])
        new_user.save()
        new_pet_farm = pet_farm(name = request.POST['name'],
                                desc = request.POST['content'],
                                detail_address = request.POST['dest'],
                                province = province,
                                city = city,
                                district = request.POST['district'],
                                direct = request.POST['direct'],
                                min_prince = 10000,
                                manage_score = manage_score)
        new_pet_farm.save()
        new_user.petfarm = new_pet_farm
        new_user.save()
        return __errorcode__(0)
    except:
        return __errorcode__(2) 

def pet_farm_all():
    farms = pet_farm.objects.filter(dele=False)
    return {'farms':farms}

def manage_picupload(photo,width,height):
    if photo == None:
        return 'false'
    try:
        img = Image.open(photo)
    except:
        return 'type error'
    if img.mode != 'RGB':
        img = img.convert('RGB')
    w,h = img.size
    if (w < width) or (h < height):
        return 'size error'
    url=(settings.PIC_TMP_PATH+photo.name).encode('utf8')
    name = settings.STATIC_ROOT + url
    if os.path.exists(name):
        photo = 'NULL'
    else:
        file, ext = os.path.splitext(photo.name)
        file='%s'%str(uuid.uuid1())
        photo.name = file+'.jpg'
        url = (settings.PIC_TMP_PATH+photo.name).encode('utf8')
        name = settings.STATIC_ROOT+url
        img.save(name,'jpeg',quality=75,optimize=True, progressive=True)
        monitor = tmppic_monitor(fname=name)
        monitor.save()
    json = '{"url":"'+'/static'+url+'","width":"'+str(w)+'","height":"'+str(h)+'"}'
    return json

def pic_preupload(request,pic_dir,max_height,max_width): 
    try:
        img= Image.open(settings.ROOT + request.POST['source'])
    except:
        return 'type error'
    x1 = string.atoi(request.POST['x1'])
    y1 = string.atoi(request.POST['y1'])
    x2 = string.atoi(request.POST['x2'])
    y2 = string.atoi(request.POST['y2'])
    if (x2 - x1) + 3 < max_width or (y2 - y1) + 3 < max_height:
        return 'crop size error'
    if img.mode != 'RGB':
        img = img.convert('RGB')
    cropimg = img.crop((x1,y1,x2,y2))
    if cropimg.mode != 'RGB':
        cropimg.convert('RGB')
    if (x2 - x1) > max_width:
        cropimg.thumbnail( (max_width,max_height) )
    #file_name = '%s'%str(uuid.uuid1()) + '.png'
    file_name = request.POST['source'].split('/')[-1]
    file_path_name = pic_dir + file_name
    url = (settings.PIC_TMP_PATH+file_name).encode('utf8')
    name = settings.STATIC_ROOT + url
    cropimg.save(name,quality=75,optimize=True, progressive=True)
    
    up = UpYun(config.__upyun_picpath,config.__upyun_name,config.__upyun_pwd)
    with open(name, 'rb') as f:
        res = up.put(file_path_name, f, checksum=False)
    #rr = _u.put(file_name, cropimg, checksum=False,headers={"x-gmkerl-rotate": "180"}) 
    #删除服务器本地缓存的图片
    os.remove(name)
    #writeFile方法不会返回图片地址，所以得自己写
    img_url = settings.PIC_ROOT + file_path_name
    return img_url

def manage_ad_picpreupload(request,max_width,max_height):
    if 'source' in request.POST:
        ad_type = None
        for adtype in config.__adtypes:
            if adtype[1] == request.POST['type']:
                ad_type = adtype[1]
                break
        if not ad_type:
            return __errorcode__(16)
        try:
            start_time = datetime.datetime.strptime(request.POST['start_time'], "%Y-%m-%d %H:%M:%S")
            end_time = datetime.datetime.strptime(request.POST['end_time'], "%Y-%m-%d %H:%M:%S")
        except:
            return __errorcode__(14)
        try:
            prince = string.atoi(request.POST['prince'])
            if prince <= 0:
                return __errorcode__(15)
        except:
            return __errorcode__(15)
        img_url = pic_preupload(request,settings.PET_AD_PIC_ROOT,max_height,max_width)
        if img_url == 'type error':
            return __errorcode__(4)
        if img_url == 'crop size error':
            return __errorcode__(13)
        #把url存入数据库
        ad_sql = ad( type = ad_type,
                     tar_url = request.POST['tar_url'],
                     prince = prince,
                     start_time = start_time,
                     end_time = end_time,
                     img_url = img_url)
        ad_sql.save()
    return __errorcode__(0)

def manage_get_adtypes():
    ad_types = []
    for adtype in config.__adtypes:
        ad_types.append({'value':adtype[1],'text':adtype[2]})
    return ad_types

def manage_ad_del(request):
    if request.method == 'POST':
        try:
            ads_str = request.REQUEST.getlist('ads')
            type = request.POST['adtype']
            ads = ad.objects.filter(type=type,dele=False)
            for tmp_ad in ads_str:
                curad = ads.get(id=string.atoi(tmp_ad))
                curad.dele = True
                curad.save()
        except:
            return 'False'
    ad_types = manage_get_adtypes()
    ads = ad.objects.filter(type = config.__adtypes[0][1],dele=False)
    return {'ad_types':ad_types,'ads':ads}

def manage_ad_select(request):
    if request.method == 'GET'and 'adtype' in request.GET:
        htmltoken = ""
        ads = ad.objects.filter(type = request.REQUEST.get('adtype'),dele = False)
        for tmp_ad in ads:
            htmltoken = '<p><input type="checkbox" name="ads" value="' + tmp_ad.id + '"><img src="' + tmp_ad.img_url + '" /></input></p>'
        return htmltoken
    return  'False'

def manage_get_supplies(request):
    supplietype = request.REQUEST.get('type', config.__supplietypes[0])
    return (supplietype, supplies.objects.filter(dele=False,type=supplietype))

def manage_get_supplie(id):
    try:
        return supplies.objects.get(id=id,dele=False)
    except:
        return None

def manage_del_supplie(request):
    supplies.objects.filter(id=string.atoi(request.REQUEST.get('del')),dele=False).update(dele=True)

def manage_supplie_add(req,photo):
    if photo == None:
        return False
    try:
        img = Image.open(photo)
    except:
        return False
    filename='%s' % str(uuid.uuid1())
    photo.name = filename + '.jpg'
    url = (settings.PIC_TMP_PATH+photo.name).encode('utf8')
    name = settings.STATIC_ROOT+url
    img.save(name,'jpeg',quality=75,optimize=True, progressive=True)
    file_path_name = settings.SUPPLIE_PIC_ROOT + photo.name
    up = UpYun(config.__upyun_picpath,config.__upyun_name,config.__upyun_pwd)
    with open(name, 'rb') as f:
        res = up.put(file_path_name, f, checksum=False)
    os.remove(name)
    img_url = settings.PIC_ROOT + file_path_name
    try:
        new_supplie = supplies(type=req.POST['type'],img_url=img_url,tar_url=req.POST['tarurl'],price=string.atof(req.POST['price']),title=req.POST['title'])
        new_supplie.save()
    except:
        return False
    return True

def manage_supplie_mod(req,photo):
    supplie = supplies.objects.get(id=string.atoi(req.POST['id']),dele=False)
    img_url = supplie.img_url
    if photo != None:
        try:
            img = Image.open(photo)
            filename='%s' % str(uuid.uuid1())
            photo.name = filename + '.jpg'
            url = (settings.PIC_TMP_PATH+photo.name).encode('utf8')
            name = settings.STATIC_ROOT+url
            img.save(name,'jpeg',quality=75,optimize=True, progressive=True)
            file_path_name = settings.SUPPLIE_PIC_ROOT + photo.name
            up = UpYun(config.__upyun_picpath,config.__upyun_name,config.__upyun_pwd)
            with open(name, 'rb') as f:
                res = up.put(file_path_name, f, checksum=False)
            os.remove(name)
            img_url = settings.PIC_ROOT + file_path_name
        except:
            None
    try:
        supplie.img_url = img_url
        supplie.type = req.POST['type']
        supplie.tar_url = req.POST['tarurl']
        supplie.price = string.atof(req.POST['price'])
        supplie.title = req.POST['title']
        supplie.save()
        return True
    except:
        return False

def manage_get_knowledges(request,id=None):
    if id != None:
        return pclady.objects.get(id = id)
    if 'del' in request.GET:
        try:
            datadel = pclady.objects.get(dele=True, id = string.atoi(request.REQUEST.get('del')))
            datadel.delete()
        except:
            pass
    if 'type' in request.GET:
        return pclady.objects.filter(dele=True, classify = config.__knowledgetypes[string.atoi(request.REQUEST.get('type'))][1])
    else:
        return pclady.objects.filter(dele=True, classify = config.__knowledgetypes[0][1])
def manage_knowledge_mod(request):
        knowledge = pclady.objects.get(id=string.atoi(request.POST['id']))
        knowledge.title = request.POST['title']
        knowledge.content = request.POST['content']
        knowledge.classify = config.__knowledgetypes[string.atoi(request.POST['type'])][1]
        knowledge.contentfrom = request.POST['contentfrom']
        knowledge.dele = string.atoi(request.POST['dele'])
        knowledge.save()
        return True

import json
from chongwug.commom import flushconfig

def manage_config_address(request):
    data = []
    if 'del' in request.GET:
        isfind = False
        count = 0
        if 'street' in request.GET:
            for street in config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'][string.atoi(request.REQUEST.get('distict'))]['sublist']:
                if street['name'] == request.REQUEST.get('street') and  not isfind:
                    config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'][string.atoi(request.REQUEST.get('distict'))]['sublist'].remove(street)
                    isfind = True
                if isfind and len(config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'][string.atoi(request.REQUEST.get('distict'))]['sublist']) > count:
                    config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'][string.atoi(request.REQUEST.get('distict'))]['sublist'][count]['index'] = count
                count = count + 1
        elif 'distict' in request.GET:
            for distict in config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist']:
                if distict['name'] == request.REQUEST.get('distict') and  not isfind:
                    config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'].remove(distict)
                    isfind = True
                if isfind and len(config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist']) > count:
                    config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'][count]['index'] = count
                count = count + 1
        elif 'city' in request.GET:
            for city in config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist']:
                if city['name'] == request.REQUEST.get('city') and  not isfind:
                    config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'].remove(city)
                    isfind = True
                if isfind and len(config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist']) > count:
                    config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][count]['index'] = count
                count = count + 1
        elif 'province' in request.GET:
            for province in config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist']:
                if province['name'] == request.REQUEST.get('province') and  not isfind:
                    config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'].remove(province)
                    isfind = True
                if isfind and len(config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist']) > count:
                    config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][count]['index'] = count
                count = count + 1
        elif 'range' in request.GET:
            for range in config.__addresses:
                if range['name'] == request.REQUEST.get('range') and  not isfind:
                    config.__addresses.remove(range)
                    isfind = True
                if isfind and len(config.__addresses) > count:
                    config.__addresses[count]['index'] = count
                count = count + 1
        flushconfig()
    elif 'modify' in request.GET:
        if 'street' in request.GET:
            for street in config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'][string.atoi(request.REQUEST.get('distict'))]['sublist']:
                if street['index'] == string.atoi(request.REQUEST.get('street')):
                    config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'][string.atoi(request.REQUEST.get('distict'))]['sublist'][street['index']]['name'] = request.REQUEST.get('text')
                    break
        elif 'distict' in request.GET:
            for distict in config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist']:
                if distict['index'] == string.atoi(request.REQUEST.get('distict')):
                    config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'][distict['index']]['name'] = request.REQUEST.get('text')
                    config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'][distict['index']]['waitpoint'] = request.REQUEST.get('area')
                    break
        elif 'city' in request.GET:
            for city in config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist']:
                if city['index'] == string.atoi(request.REQUEST.get('city')):
                    config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][city['index']]['name'] = request.REQUEST.get('text')
                    break
        elif 'province' in request.GET:
            for province in config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist']:
                if province['index'] == string.atoi(request.REQUEST.get('province')):
                    config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][province['index']]['name'] = request.REQUEST.get('text')
                    break
        elif 'range' in request.GET:
            for range in config.__addresses:
                if range['index'] == string.atoi(request.REQUEST.get('range')):
                    config.__addresses[range['index']]['name'] = request.REQUEST.get('text')
                    break
        flushconfig()
    elif 'add' in request.GET:
        if 'distict' in request.GET:
            index = len(config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'][string.atoi(request.REQUEST.get('distict'))]['sublist'])
            config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'][string.atoi(request.REQUEST.get('distict'))]['sublist'].append({'name':request.REQUEST.get('text'),'index':index})
            data = {'type':'street','index':index}
        elif 'city' in request.GET:
            index = len(config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'])
            config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'].append({'name':request.REQUEST.get('text'),'index':index,'waitpoint':request.REQUEST.get('area'),'sublist':[]})
            data = {'type':'distict','index':index}
        elif 'province' in request.GET:
            index = len(config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'])
            config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'].append({'name':request.REQUEST.get('text'),'index':index,'sublist':[]})
            data = {'type':'city','index':index}
        elif 'range' in request.GET:
            index = len(config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'])
            config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'].append({'name':request.REQUEST.get('text'),'index':index,'sublist':[]})
            data = {'type':'province','index':index}
        else:
            index = len(config.__addresses)
            config.__addresses.append({'name':request.REQUEST.get('text'),'index':index,'sublist':[]})
            data = {'type':'range','index':index}
        flushconfig()
    else:
        if 'ranges' in request.GET:
            for range in config.__addresses:
                data.append({ "index" : range['index'],  "text" : range['name'], "children" : True, "type": "range" })
        elif 'provinces' in request.GET:
            for province in config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist']:
                data.append({ "index" : province['index'],  "text" : province['name'], "children" : True, "type": "province" })
        elif 'citys' in request.GET:
            for city in config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist']:
                data.append({ "index" : city['index'],  "text" : city['name'], "children" : True, "type": "city" })
        elif 'disticts' in request.GET:
            for distict in config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist']:
                data.append({ "index" : distict['index'],  "text" : distict['name'], "children" : True, "type": "distict", "area" : distict['waitpoint'] })
        elif 'streets' in request.GET:
            for street in config.__addresses[string.atoi(request.REQUEST.get('range'))]['sublist'][string.atoi(request.REQUEST.get('province'))]['sublist'][string.atoi(request.REQUEST.get('city'))]['sublist'][string.atoi(request.REQUEST.get('distict'))]['sublist']:
                data.append({ "index" : street['index'],  "text" : street['name'], "children" : False, "type": "street" })
        else:
            data = manage_home_data_get(request)
            return data,False
    return json.dumps(data),None

def manage_config(request,who):
    if who == None:
        return None
    
    if who == 'breeds':
        data = manage_home_data_get(request)
        if 'add' in request.GET:
            add = request.REQUEST.get('add')
            after = request.REQUEST.get('after')
            if after == '':
                config.__pettypes.insert(0, add)
            else:
                config.__pettypes.insert(config.__pettypes.index(after) + 1, add)
        elif 'modify' in request.GET:
            new = request.REQUEST.get('modify')
            old = request.REQUEST.get('old')
            config.__pettypes[config.__pettypes.index(old)] = new
        elif 'del' in request.GET:
            config.__pettypes.remove(request.REQUEST.get('del'))
        else:
            data['infos'] = config.__pettypes
            return data,False
        flushconfig()
        return data,True
    elif who == 'address':
        return manage_config_address(request)
    return None,None

def manage_get_newusers():
    return user.objects.filter(verify=0,dele=False,type=1)

def manage_verify_newusers(request):
    obj = user.objects.get(id=string.atoi(request.REQUEST.get('id')),verify=0,dele=False)
    obj.verify = string.atoi(request.REQUEST.get('verify'))
    obj.save()

def manage_get_newpets():
    return nestofpet.objects.filter(verify=0,dele=False,sale_out=False)

def manage_verify_newpets(request):
    obj = nestofpet.objects.get(id=string.atoi(request.REQUEST.get('id')),verify=0,dele=False,sale_out=False)
    obj.verify = string.atoi(request.REQUEST.get('verify'))
    obj.save()