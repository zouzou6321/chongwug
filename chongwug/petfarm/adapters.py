# -*- coding: UTF-8 -*-
from customer.models import user
from manager.models import tmppic_monitor
from petfarm.models import pet_farm,pet_farm_img,nestofpet,nestofpet_img,pet
from PIL import Image
from chongwug import settings
from chongwug.config import __petpictypes,__upyun_picpath,__upyun_name,__upyun_pwd,__farmpictypes
from chongwug.commom import __errorcode__
from upyun import UpYun
from django.contrib import auth

import os,uuid,string,re,datetime,json

def pic_crop_save(pic_args,pic_dir,max_height,max_width): 
    try:
        img= Image.open(settings.STATIC_ROOT + settings.PIC_TMP_PATH + pic_args['source'])
    except:
        return 'type error'
    
    x1 = int(pic_args['x1'])
    y1 = int(pic_args['y1'])
    x2 = int(pic_args['x2'])
    y2 = int(pic_args['y2'])
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
    cropimg.save(name)
    cropimg.close()
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
    name = request.REQUEST.get('username')
    passwd = request.REQUEST.get('userpassd')
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

def get_petpic_types():
    types = []
    for petpictype in __petpictypes:
        types.append({'type':petpictype[1],'desc':petpictype[2],'width':petpictype[3],'height':petpictype[4]})
    return {'types':types}


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

def manage_nestofpet_picpreupload(request,_nestofpet):
    img_count = string.atoi(request.POST['img-count'])
    #挨个处理上传的图片数据
    itr = 0
    while itr < img_count:
        itr += 1
        #挨个获取图片并且判断图片是否存在
        try:
            imgw,imgh = 0,0
            for petpictype in __petpictypes:
                if request.POST['img-%d-type' % itr] == petpictype[1]:
                    imgw = petpictype[3]
                    imgh = petpictype[4]
                    break
        except:
            continue
        
        #判断图片类型是否有异常
        if imgw == 0 or imgh == 0:
            return __errorcode__(1)
        imginfo_json = json.loads(request.POST['img-%d-position' % itr])
        #整理 数据，以便截图保存模块使用
        pic_args = {'source':request.POST['img-%d' % itr].split('/')[-1],'x1':imginfo_json['x'],
                    'x2':imginfo_json['x2'],'y1':imginfo_json['y'],'y2':imginfo_json['y2']}

        img_url = pic_crop_save(pic_args,settings.PET_PIC_ROOT,imgh,imgw)
        if img_url == 'type error':
            _nestofpet.delete()
            return __errorcode__(4)
        
        #把图片信息存入数据库
        pet_sql = nestofpet_img( nestofpet_id = _nestofpet,
                                img_url = img_url,
                                img_with = int(pic_args['x2'] - pic_args['x1']),
                                img_height = int(pic_args['y2'] - pic_args['y1']),
                                #img_type:jpg/png/...
                                img_type = 'jpg',
                                #图片用途
                                img_usefor = request.POST['img-%d-type' % itr])
        pet_sql.save()
    return __errorcode__(0)
def manage_nestofpet_add(request):
    try:
        farm = user.objects.get(auth_user=auth.get_user(request),dele = False).petfarm
        new_nestofpet = nestofpet(farm = farm,
                                color = request.POST['nest-color'],
                                age = string.atoi(request.POST['nest-age']),
                                type = request.POST['nest-type'],
                                short_desc = request.POST['nest-desc'])
        new_nestofpet.save()
        cur_datetime = datetime.datetime.now()
        new_nestofpet.num = "%d%d%d%d%d" % (farm.id,cur_datetime.year,cur_datetime.month,cur_datetime.day,new_nestofpet.id)
        new_nestofpet.save()
    except NameError:
        return __errorcode__(2)
    try:
        new_petscount = string.atoi(request.POST['count'])
        petnum = 0
        while petnum < new_petscount:
            petnum += 1
            try:
                new_pet = pet(  nestofpet = new_nestofpet,
                                index = chr(ord('A') + (petnum - 1)),
                                color = request.POST['color%d' % petnum],
                                epidemic_period = request.POST['epidemic%d' % petnum],
                                price = request.POST['price%d' % petnum],
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
    
    return manage_nestofpet_picpreupload(request,new_nestofpet)

def manage_pet_farm_picadd(request):
    use_fors = []
    use_fors.append('buy_home')
    use_fors.append('narmol')
    return {'use_fors':use_fors}

def pet_farm_all():
    farms = pet_farm.objects.filter(dele=False)
    return {'farms':farms}

def manage_pet_farm_mod(request):
    try:
        if request.POST['province'] == '':
            province = '四川'
        else:
            province = request.POST['province']
        if request.POST['city'] == '':
            city = '成都'
        else:
            city = request.POST['city']
        curuser = user.objects.get(auth_user=auth.get_user(request),dele=False)
        curuser.petfarm.name = request.POST['name']
        curuser.petfarm.desc = request.POST['desc']
        curuser.petfarm.detail_address = request.POST['detail_address']
        curuser.petfarm.province = province
        curuser.petfarm.city = city
        curuser.petfarm.district = request.POST['district']
        curuser.petfarm.direct = request.POST['direct']
        curuser.petfarm.min_prince = request.POST['min_prince']
        curuser.save()
    except NameError:
        return False
    return True

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
        img.save(name,'jpeg',quality=75)
        monitor = tmppic_monitor(fname=name)
        monitor.save()
    data = {'url':'/static'+url,"width":str(w),"height":str(h)}
    return __errorcode__(0,data)
    
def manage_pet_farm_picpreupload(request):
    if 'source' in request.POST:
        max_height = 178
        max_width = 250
        img_url = pic_crop_save(request,settings.PET_FARM_PIC_ROOT,max_height,max_width)
        if img_url == 'type error':
            return 'type error'
        #把url存入数据库
        pet_farm_sql = pet_farm_img( pet_farm_id = user.objects.get(auth_user=auth.get_user(request),dele = False).petfarm,
                                img_url = img_url,
                                img_with = string.atoi(request.POST['x2']) - string.atoi(request.POST['x1']),
                                img_height = string.atoi(request.POST['y2']) - string.atoi(request.POST['y1']),
                                #img_type:jpg/png/...
                                img_type = 'png',
                                #图片用途
                                img_usefor = request.POST['usefor'])
        pet_farm_sql.save()
    return __errorcode__()

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
        new_nestofpet = nestofpet.objects.get(id=string.atoi(request.REQUEST.get('id')),farm=curuser.petfarm,sale_out=False)
        new_nestofpet.dele = True
        new_nestofpet.save()
    except:
        return __errorcode__(1)
    return __errorcode__(0)
        
def manage_nestofpet_mod(request):
    try:
        curuser = user.objects.get(auth_user=auth.get_user(request),dele=False)
        new_nestofpet = nestofpet.objects.get(id=string.atoi(request.POST['pet_id']),farm=curuser.petfarm,dele=False,sale_out=False)
        new_nestofpet.color = request.POST['color']
        new_nestofpet.age = string.atoi(request.POST['age'])
        new_nestofpet.type = request.POST['type']
        new_nestofpet.short_desc = request.POST['short_desc']
        new_nestofpet.save()
    except NameError:
        return False
    return True

def manage_get_del_farmpics(request):
    try:
        curuser = user.objects.get(auth_user=auth.get_user(request),dele=False)
        if request.method == 'POST':
            pics_str = request.REQUEST.getlist('farmpics')
            farmpics = pet_farm_img.objects.filter(pet_farm_id=curuser.petfarm,dele=False)
            for tmp_pic in pics_str:
                try:
                    curpic = farmpics.get(id=string.atoi(tmp_pic))
                    curpic.dele = True
                    curpic.save()
                except:
                    return 'False'
        return pet_farm_img.objects.filter(pet_farm_id=curuser.petfarm,dele=False)
    except:
        return 'False'

def manage_get_del_petpics(request):
    try:
        curuser = user.objects.get(auth_user=auth.get_user(request),dele=False)
        if request.method == 'POST':
            pics_str = request.REQUEST.getlist('petpics')
            curpet = nestofpet.objects.get(id=string.atoi(request.POST['pet_id']),farm=curuser.petfarm,dele=False,sale_out=False)
            petpics = nestofpet_img.objects.filter(nestofpet_id=curpet,dele=False)
            for tmp_pic in pics_str:
                try:
                    curpic = petpics.get(id=string.atoi(tmp_pic))
                    curpic.dele = True
                    curpic.save()
                except:
                    return 'False'
        if 'id' not in request.GET:
            pets = manage_get_pets(request)
            petpics = nestofpet_img.objects.filter(nestofpet_id=pets[0],dele=False)
            return {'pets':pets,'petpics':petpics}
        else:
            pet_one = manage_get_pets(request)
            petpics = nestofpet_img.objects.filter(nestofpet_id=pet_one,dele=False)
            return {'petpics':petpics}
    except:
        return 'False'
    return 'False'