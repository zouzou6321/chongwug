# -*- coding: UTF-8 -*-
from customer.models import user
from manager.models import tmppic_monitor
from petfarm.models import pet_farm,pet_farm_img,nestofpet,nestofpet_img,pet
from PIL import Image
from chongwug import settings
from chongwug.config import __epidemics,__regular_expression_email,__regular_expression_chinatelnum,__directs,__addresses,__petpictypes,__upyun_picpath,__upyun_name,__upyun_pwd,__farmpictypes,__pettypes,__petages
from django import forms
from chongwug.commom import __errorcode__,myCKEditorWidget
from upyun import UpYun
from django.contrib import auth
import traceback
import os,uuid,string,re,datetime,json

def pic_crop_save(pic_args,pic_dir,max_height,max_width): 
    try:
        img= Image.open(settings.STATIC_ROOT + settings.PIC_TMP_PATH + pic_args['source'])
    except:
        traceback.print_exc()
        return 'type error'
    
    x1 = int(pic_args['x1'])
    y1 = int(pic_args['y1'])
    x2 = int(pic_args['x2'])
    y2 = int(pic_args['y2'])
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
    file_name = pic_args['source'].split('/')[-1]
    file_path_name = pic_dir + file_name
    url = (settings.PIC_TMP_PATH + file_name).encode('utf8')
    name = settings.STATIC_ROOT + url
    cropimg.save(name,quality=75,optimize=True, progressive=True)
    up = UpYun(__upyun_picpath,__upyun_name,__upyun_pwd)
    with open(name, 'rb') as f:
        res = up.put(file_path_name, f, checksum=False)
    #rr = _u.put(file_name, cropimg, checksum=False,headers={"x-gmkerl-rotate": "180"}) 
    #删除服务器本地缓存的图片
    os.remove(name)
    #writeFile方法不会返回图片地址，所以得自己写
    img_url = settings.PIC_ROOT + file_path_name
    return img_url

'''
管理员鉴权
'''
def manage_authentication(request):
    if not request.user.is_authenticated():
        return False
    cur_user = user.objects.get(auth_user=auth.get_user(request),dele=False)
    if cur_user.type < 1:
        return False
    return True

def manage_login_check(request):
    name = request.POST['username']
    passwd = request.POST['userpassd']
    user = auth.authenticate(username=name, password=passwd)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return True
    else:
        # Show an error page
        return False

def manage_home_data_get(request):
    manager = user.objects.get(auth_user=auth.get_user(request),dele = False)
    return {'manager':manager}

def get_pet_types():
    return {'pettypes':__pettypes}

def get_pet_ages():
    return {'petages':__petages}

def get_petpic_types():
    types = []
    for petpictype in __petpictypes:
        types.append({'type':petpictype[1],'desc':petpictype[2],'width':petpictype[3],'height':petpictype[4]})
    return {'types':types}

def get_farmpics(manager):
    return manager.petfarm.pet_farm_img_set.filter(dele=False)

def get_farmpic_types():
    types = []
    for farmpictype in __farmpictypes:
        types.append({'type':farmpictype[1],'desc':farmpictype[2],'width':farmpictype[3],'height':farmpictype[4]})
    return {'types':types}

def petpic_upload_pre(request):
    imgw,imgh = 0,0
    for petpictype in __petpictypes:
        if imgw < petpictype[3]:
            imgw = petpictype[3]
        if imgh < petpictype[4]:
            imgh = petpictype[4]
    return imgw,imgh

def farmpic_upload_pre(request):
    imgw,imgh = 0,0
    for farmpictype in __farmpictypes:
        if imgw < farmpictype[3]:
            imgw = farmpictype[3]
        if imgh < farmpictype[4]:
            imgh = farmpictype[4]
    return imgw,imgh

def manage_picpreupload(request,_from,_nestofpet=None):
    if 'img-count' not in request.POST:
        return __errorcode__(4)
    img_count = string.atoi(request.POST['img-count'])
    if _from == 'farm':
        pictypes = __farmpictypes
        pic_root = settings.PET_FARM_PIC_ROOT
    elif _from == 'pet' or _from == 'petmod':
        pictypes = __petpictypes
        pic_root = settings.PET_PIC_ROOT
    #挨个处理上传的图片数据
    imgusefor = pictypes[1][1]
    itr = 0
    while itr < img_count:
        itr += 1
        #挨个获取图片并且判断图片是否存在
        try:
            imgw,imgh = pictypes[1][3],pictypes[1][4]
            if request.POST['img-main'] == request.POST['img-%d' % itr]:
                imgw = pictypes[0][3]
                imgh = pictypes[0][4]
                imgusefor = pictypes[0][1]
        except:
            continue
        #判断图片类型是否有异常
        if imgw == 0 or imgh == 0:
            return __errorcode__(1)
        imginfo_json = json.loads(request.POST['img-%d-position' % itr])
        #整理 数据，以便截图保存模块使用
        pic_args = {'source':request.POST['img-%d' % itr].split('/')[-1],'x1':imginfo_json['x'],
                    'x2':imginfo_json['x2'],'y1':imginfo_json['y'],'y2':imginfo_json['y2']}

        img_url = pic_crop_save(pic_args,pic_root,imgh,imgw)
        if img_url == 'type error':
            if _from == 'pet':
                _nestofpet.delete()
            return __errorcode__(4)
        if img_url == 'crop size error':
            if _from == 'pet':
                _nestofpet.delete()
            return __errorcode__(13)
        
        #把url存入数据库
        if _from == 'farm':
            pet_farm_sql = pet_farm_img( pet_farm_id = user.objects.get(auth_user=auth.get_user(request),dele = False).petfarm,
                                    img_url = img_url,
                                    img_with = int(pic_args['x2'] - pic_args['x1']),
                                    img_height = int(pic_args['y2'] - pic_args['y1']),
                                    #img_type:jpg/png/...
                                    img_type = 'jpg',
                                    #图片用途
                                    img_usefor = imgusefor)
            pet_farm_sql.save()
        elif _from == 'pet':
            pet_sql = nestofpet_img( nestofpet_id = _nestofpet,
                                img_url = img_url,
                                img_with = int(pic_args['x2'] - pic_args['x1']),
                                img_height = int(pic_args['y2'] - pic_args['y1']),
                                #img_type:jpg/png/...
                                img_type = 'jpg',
                                #图片用途
                                img_usefor = imgusefor)
            pet_sql.save()
        elif _from == 'petmod':
            pet_sql = nestofpet_img( nestofpet_id = _nestofpet,
                                img_url = img_url,
                                img_with = int(pic_args['x2'] - pic_args['x1']),
                                img_height = int(pic_args['y2'] - pic_args['y1']),
                                #img_type:jpg/png/...
                                img_type = 'jpg',
                                #图片用途
                                img_usefor = imgusefor)
            pet_sql.save()
    return __errorcode__(0)

def manage_nestofpet_add(request):
    img_count = string.atoi(request.POST['img-count'])
    if img_count <= 0:
        return __errorcode__(4)
    petnum = 0
    while petnum <= img_count:
        petnum += 1
        if 'img-main' in request.POST:
            break;
    if petnum > img_count:
        return __errorcode__(4)
    
    if request.POST['nest-desc'] == '':
        return __errorcode__(20)
    if request.POST['nest-longdesc'] == '':
        return __errorcode__(20)
    new_petscount = string.atoi(request.POST['count'])
    petnum = 0
    while petnum < new_petscount:
        petnum += 1
        try:
            if ('price%d' % petnum) in request.POST and string.atoi(request.POST['price%d' % petnum]) <= 0:
                return __errorcode__(15)
        except:
            return __errorcode__(15)
    try:
        farm = user.objects.get(auth_user=auth.get_user(request),dele = False).petfarm
        new_nestofpet = nestofpet(farm = farm,
                                color = request.POST['nest-color'],
                                age = string.atoi(request.POST['nest-age']),
                                type = request.POST['nest-type'],
                                short_desc = request.POST['nest-desc'],
                                txt_desc = request.POST['nest-longdesc'])
        new_nestofpet.save()
        cur_datetime = datetime.datetime.now()
        new_nestofpet.num = "%d%d%d%d%d" % (farm.id,cur_datetime.year,cur_datetime.month,cur_datetime.day,new_nestofpet.id)
        new_nestofpet.save()
    except NameError:
        return __errorcode__(2)
    try:
        petnum = 0
        while petnum < new_petscount:
            petnum += 1
            try:
                new_pet = pet(  nestofpet = new_nestofpet,
                                index = chr(ord('A') + (petnum - 1)),
                                color = request.POST['color%d' % petnum],
                                epidemic_period = request.POST['epidemic%d' % petnum],
                                price = string.atoi(request.POST['price%d' % petnum]),
                                sex = request.POST['sex%d' % petnum],
                                sale_out = ((request.POST['sale%d' % petnum] == '1') and 1) or 0)
                new_pet.save()
            except:
                if petnum > 1:
                    pass
                else:
                    raise NameError,("first pet can't create","in adapters.py")
    except:
        new_nestofpet.delete()
        return __errorcode__(2)
    return manage_picpreupload(request,'pet',new_nestofpet)

def pet_farm_all():
    farms = pet_farm.objects.filter(dele=False)
    return {'farms':farms}

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

class descform(forms.Form):
    content = forms.CharField(widget=myCKEditorWidget(),label=u'详细介绍:')

def manage_pet_farm_mod(request):
    try:
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
        
        p = re.compile(__regular_expression_chinatelnum)
        if not p.match(request.POST['tel']):
            return __errorcode__(9)
        p = re.compile(__regular_expression_email)
        if not p.match(request.POST['email']):
            return __errorcode__(16)
        content = descform({'content':request.POST['content']})
        if not content.is_valid():
            return __errorcode__(1)
        curuser = user.objects.get(auth_user=auth.get_user(request),dele=False)
        curuser.tel = request.POST['tel']
        curuser.email = request.POST['email']
        if request.POST['pwd'] != '':
            curuser.pwd = request.POST['pwd']
        curuser.petfarm.name = request.POST['name']
        curuser.petfarm.desc = request.POST['content']
        curuser.petfarm.detail_address = request.POST['detail_address']
        curuser.petfarm.province = province
        curuser.petfarm.city = city
        curuser.petfarm.district = request.POST['district']
        curuser.petfarm.direct = request.POST['direct']
        curuser.petfarm.save()
        curuser.save()
        if 'img-main' not in request.POST:
            return __errorcode__(22)
        else:
            curuser.petfarm.pet_farm_img_set.filter(img_usefor=__farmpictypes[0][1],dele=False).update(img_usefor=__farmpictypes[1][1])
            curuser.petfarm.pet_farm_img_set.filter(img_url=request.POST['img-main'],dele=False).update(img_usefor=__farmpictypes[0][1])
        print request.POST
        if 'del[]' in request.POST:
            imgids = request.POST.getlist('del[]')
            for imgid in imgids:
                curuser.petfarm.pet_farm_img_set.filter(id=string.atoi(imgid),img_usefor=__petpictypes[1][1]).update(dele=True)
    except NameError:
        return __errorcode__(2)
    return manage_picpreupload(request,'farm')

def manage_picupload(photo,width,height):
    if photo == None:
        return 'false'
    try:
        img = Image.open(photo)
    except:
        return __errorcode__(2)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    w,h = img.size
    
    if w > 1170:
        img.thumbnail((1170,3000))
        w,h = img.size
    if (w < width) or (h < height):
        return __errorcode__(6)
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
    data = {'url':'/static'+url,"width":str(w),"height":str(h)}
    return __errorcode__(0,data)

def manage_get_pets(request):
    curuser = user.objects.get(auth_user=auth.get_user(request),dele = False)
    if 'id' in request.GET:
        pet_one = nestofpet.objects.get(id=string.atoi(request.REQUEST.get('id')),farm=curuser.petfarm,dele=False,sale_out=False)
        return pet_one
    else:
        pets = nestofpet.objects.filter(farm=curuser.petfarm,dele=False,sale_out=False)
        return pets

def manage_del_pet(request):
    try:
        curuser = user.objects.get(auth_user=auth.get_user(request),dele=False)
        cur_nestofpet = nestofpet.objects.get(id=string.atoi(request.REQUEST.get('id')),farm=curuser.petfarm,sale_out=False)
        cur_nestofpet.dele=True
        cur_nestofpet.save()
        cur_nestofpet.pet_set.filter(dele=False).update(dele=True)
    except:
        traceback.print_exc()
        return __errorcode__(1)
    return __errorcode__(0)

def manage_nestofpet_mod_info(request):
    data = {}
    pets = manage_get_pets(request)
    data['pets'] = pets
    if not isinstance(pets, nestofpet) and pets.count() > 0:
        data['pet_one'] = pets[0]
        data['pet_set'] = pets[0].pet_set.filter(dele=False)
        data['pet_types'] = __pettypes
        data['pet_ages'] = __petages
        data['epidemics'] = __epidemics
        data['petimgs'] = pets[0].nestofpet_img_set.filter(dele=False)
    elif isinstance(pets, nestofpet):
        data['pet_one'] = pets
        data['pet_set'] = pets.pet_set.filter(dele=False)
        data['pet_types'] = __pettypes
        data['pet_ages'] = __petages
        data['epidemics'] = __epidemics
        data['petimgs'] = pets.nestofpet_img_set.filter(dele=False)
    return data
def manage_nestofpet_mod(request):
    try:
        curuser = user.objects.get(auth_user=auth.get_user(request),dele=False)
        curnestofpet = nestofpet.objects.get(id=string.atoi(request.POST['pet_id']),farm=curuser.petfarm,dele=False,sale_out=False)
        curnestofpet.color = request.POST['color']
        curnestofpet.age = string.atoi(request.POST['age'])
        curnestofpet.type = request.POST['type']
        curnestofpet.short_desc = request.POST['short_desc']
        curnestofpet.txt_desc = request.POST['nest-longdesc']
        curnestofpet.save()
        petids = request.POST.getlist('pets[]')
        for petid in petids:
            curpet = curnestofpet.pet_set.get(id=string.atoi(petid))
            curpet.color = request.POST['color%s' % petid]
            curpet.epidemic_period = request.POST['epidemic%s' % petid]
            curpet.price = request.POST['price%s' % petid]
            curpet.sex = request.POST['sex%s' % petid]
            if request.POST['sale%s' % petid] == 'True':
                curpet.sale_out = 1
            else:
                curpet.sale_out = 0
            curpet.save()
        if 'img-main' not in request.POST:
            return __errorcode__(22)
        else:
            curnestofpet.nestofpet_img_set.filter(img_usefor=__petpictypes[0][1],dele=False).update(img_usefor=__petpictypes[1][1])
            curnestofpet.nestofpet_img_set.filter(img_url=request.POST['img-main'],dele=False).update(img_usefor=__petpictypes[0][1])
        if 'del[]' in request.POST:
            imgids = request.POST.getlist('del[]')
            for imgid in imgids:
                curnestofpet.nestofpet_img_set.filter(id=string.atoi(imgid),img_usefor=__petpictypes[1][1]).update(dele=True)
    except NameError:
        return __errorcode__(2)
    return manage_picpreupload(request,'petmod',curnestofpet)