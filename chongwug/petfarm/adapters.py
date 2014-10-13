# -*- coding: UTF-8 -*-
from customer.models import user
from manager.models import tmppic_monitor
from petfarm.models import pet_farm,pet_farm_img,nestofpet,nestofpet_img,pet
from PIL import Image
from chongwug import settings
from upyun import UpYun
from django.shortcuts import get_object_or_404
from django.contrib import auth

import os,uuid,string,re,datetime
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
        print new_nestofpet.num
    except NameError:
        return False
    try:
        new_petscount = string.atoi(request.POST['count'])
        petnum = 0
        while petnum < new_petscount:
            petnum += 1
            try:
                new_pet = pet(  nestofpet = new_nestofpet,
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
        return False
    return True

def manage_nestofpet_picadd(request):
    curuser = user.objects.get(auth_user=auth.get_user(request),dele = False)
    use_fors = []
    use_fors.append('buy_main')
    use_fors.append('narmol')
    farm_pets = nestofpet.objects.filter(farm=curuser.petfarm,dele=False,sale_out=False)
    return {'use_fors':use_fors,'farm_pets':farm_pets}

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
        return 'type error'
    if img.mode != 'RGB':
        img = img.convert('RGB')
    w,h = img.size
    if w > 1170:
        img.thumbnail((1170,3000))
        w,h = img.size
    if (w < width) or (h < height):
        return 'size error'
    url=('/manage/pictest/'+photo.name).encode('utf8')
    name = settings.STATIC_ROOT + url
    if os.path.exists(name):
        photo = 'NULL'
    else:
        file, ext = os.path.splitext(photo.name)
        file='%s'%str(uuid.uuid1())
        photo.name = file+'.jpg'
        url = ('/manage/pictest/'+photo.name).encode('utf8')
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
    url = ('/manage/pictest/'+file_name).encode('utf8')
    name = settings.STATIC_ROOT + url
    cropimg.save(name)
    cropimg.close()
    
    up = UpYun('chongwug-pic','chongwug','weet6321')
    with open(name, 'rb') as f:
        res = up.put(file_path_name, f, checksum=False)
    #rr = _u.put(file_name, cropimg, checksum=False,headers={"x-gmkerl-rotate": "180"}) 
    #删除服务器本地缓存的图片
    os.remove(name)
    #writeFile方法不会返回图片地址，所以得自己写
    img_url = settings.PIC_ROOT + file_path_name
    return img_url
    
def manage_pet_farm_picpreupload(request):
    if 'source' in request.POST:
        max_height = 178
        max_width = 250
        img_url = pic_preupload(request,settings.PET_FARM_PIC_ROOT,max_height,max_width)
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
    return 'true'

def manage_nestofpet_picpreupload(request):
    if 'source' in request.POST:
        max_height = 180
        max_width = 275
        if request.POST['usefor'] == 'narmol':
            max_width = 600
            max_height = 400
        elif request.POST['usefor'] == 'buy_main':
            max_width = 275
            max_height = 180
        img_url = pic_preupload(request,settings.PET_PIC_ROOT,max_height,max_width)
        if img_url == 'type error':
            return 'type error'
        #把url存入数据库
        pet_sql = nestofpet_img( nestofpet_id = get_object_or_404(nestofpet,pk=string.atoi(request.POST['pet_id'])),
                                img_url = img_url,
                                img_with = string.atoi(request.POST['x2']) - string.atoi(request.POST['x1']),
                                img_height = string.atoi(request.POST['y2']) - string.atoi(request.POST['y1']),
                                #img_type:jpg/png/...
                                img_type = 'png',
                                #图片用途
                                img_usefor = request.POST['usefor'])
        pet_sql.save()
        return 'true'
    return 'false'

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
        return 'False'
    return 'True'
        
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
            curpet = nestofpet.objects.get(id=string.atoi(request.POST['pet_id']),farm=curuser.petfarm,dele=True,sale_out=False)
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