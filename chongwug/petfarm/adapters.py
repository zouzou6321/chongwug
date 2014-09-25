# -*- coding: UTF-8 -*-
from customer.models import user
from petfarm.models import pet_farm,pet_farm_img,nestofpet,nestofpet_img
from PIL import Image
from chongwug import settings
from upyun import UpYun
from django.shortcuts import get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User

import os,uuid,string
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
    manager = user.objects.get(id=string.atoi(request.session['petfarmuser']),type = 1,dele = False)
    return {'manager':manager}

def manage_nestofpet_add(request):
    try:
        new_nestofpet = nestofpet(farm = get_object_or_404(pet_farm,pk=string.atoi(request.POST['pet_farm_id'])),
                                color = request.POST['color'],
                                age = string.atoi(request.POST['age']),
                                epidemic_period = request.POST['epidemic'],
                                type = request.POST['type'],
                                txt_desc = request.POST['desc'],
                                min_price = string.atof(request.POST['min_prince']),
                                max_price = string.atof(request.POST['max_prince']))
        new_nestofpet.save()
    except NameError:
        return False
    return True

def manage_nestofpet_picadd(request):
    farms = pet_farm.objects.filter(dele=False)
    use_fors = []
    use_fors.append('buy_main')
    use_fors.append('narmol')
    farm_pets = nestofpet.objects.filter(farm=farms[0],dele=False,sale_out=False)
    return {'farms':farms,'use_fors':use_fors,'farm_pets':farm_pets}

def manage_pet_farm_picadd(request):
    farms = pet_farm.objects.filter(dele=False)
    use_fors = []
    use_fors.append('buy_home')
    use_fors.append('narmol')
    return {'farms':farms,'use_fors':use_fors}

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
        photo.name = file+ext
        url = ('/manage/pictest/'+photo.name).encode('utf8')
        name = settings.STATIC_ROOT+url
        img.save(name)
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
    img = img.convert('RGB')
    cropimg = img.crop((x1,y1,x2,y2))
    cropimg.convert('RGB')
    if (x2 - x1) > max_width:
        cropimg.thumbnail( (max_width,max_height) )
    #file_name = '%s'%str(uuid.uuid1()) + '.png'
    file_name = request.POST['source'].split('/')[-1]
    file_path_name = pic_dir + file_name
    url = ('/manage/pictest/'+file_name).encode('utf8')
    name = settings.STATIC_ROOT + url
    cropimg.save(name,'png')
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
        pet_farm_sql = pet_farm_img( pet_farm_id = get_object_or_404(pet_farm,pk=string.atoi(request.POST['pet_farm_id'])),
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