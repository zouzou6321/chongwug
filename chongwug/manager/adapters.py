# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from back_manager.models import manage
from manager.models import ad,tmppic_monitor,supplies
from customer.models import user
from petfarm.models import pet_farm
from PIL import Image
from chongwug import settings
from upyun import UpYun
from django.contrib.auth.models import User
import string,re
import os,uuid,datetime
import config
from chongwug.commom import __errorcode__
from chongwug.config import __directs,__addresses,__regular_expression_idnum,__regular_expression_chinatelnum,__regular_expression_email,__upyun_picpath,__upyun_name,__upyun_pwd
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
    return {'manager':manager,'directs':__directs}

def addressHandle(re):
    if 'province' in re.GET:
        addresses = __addresses[string.atoi(re.REQUEST.get('range'))]['sublist'][string.atoi(re.REQUEST.get('province'))]
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
    for _addresse in __addresses:
        rangeid = _addresse['index']
        _provinces = _addresse['sublist']
        for _province in _provinces:
            provinces.append({'rangeid':rangeid,'id':_province['index'], 'name':_province['name']})
    for _city in __addresses[0]['sublist'][0]['sublist']:
        citys.append({'id': _city['index'], 'name': _city['name']})
    for _district in __addresses[0]['sublist'][0]['sublist'][0]['sublist']:
        districts.append({'id': _district['index'], 'name': _district['name']})
    return {'provinces':provinces, 'citys':citys, 'districts':districts}

def manage_pet_farm_add(request):
    try:
        if 'pwd' not in request.POST or request.POST['pwd'] == '':
            return __errorcode__(21)
        
        if 'province' not in request.POST or request.POST['province'] == '':
            province = '四川'
        else:
            province = request.POST['province']
        if 'city' not in request.POST or request.POST['city'] == '':
            city = '成都'
        else:
            city = request.POST['city']
        
        error = True
        for _addresse in __addresses:
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
        for _direct in __directs:
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
        
        p = re.compile(__regular_expression_chinatelnum)
        if not p.match(request.POST['tel']):
            return __errorcode__(9)
        p = re.compile(__regular_expression_email)
        if not p.match(request.POST['email']):
            return __errorcode__(16)
        p = re.compile(__regular_expression_idnum)
        if not p.match(request.POST['idnum']):
            return __errorcode__(17)
        
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
                                desc = request.POST['desc'],
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
        img.save(name,'jpeg',quality=75)
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
    cropimg.save(name)
    
    up = UpYun(__upyun_picpath,__upyun_name,__upyun_pwd)
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
                print ads.count()
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

def manage_get_supplies():
    return supplies.objects.filter(dele=False)

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
    img.save(name,'jpeg',quality=75)
    file_path_name = settings.SUPPLIE_PIC_ROOT + photo.name
    up = UpYun(__upyun_picpath,__upyun_name,__upyun_pwd)
    with open(name, 'rb') as f:
        res = up.put(file_path_name, f, checksum=False)
    os.remove(name)
    img_url = settings.PIC_ROOT + file_path_name
    new_supplie = supplies(type=req.POST['type'],img_url=img_url,tar_url=req.POST['tarurl'],price=string.atof(req.POST['price']),title=req.POST['title'])
    new_supplie.save()
    return True