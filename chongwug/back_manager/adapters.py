# -*- coding: UTF-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from models import manage,pet_farm,pet_farm_img,ad
import string
from PIL import Image
import os,uuid,datetime
from chongwug import settings
from upyun import UpYun
from django.shortcuts import get_object_or_404

def manage_authentication(request):
    try:
        if (request.session['manage_id'] == ''):
            return False
    except NameError:
        return False
    return True

def manage_login_check(request):
    name = request.REQUEST.get('username')
    passwd = request.REQUEST.get('userpassd')
    request.session['manage_id'] = ''
    try:
        manage_id = manage.objects.get(name=name,passwd=passwd).id
    except ObjectDoesNotExist:
        print('ObjectDoesNotExist')
        return False
    request.session['manage_id'] = manage_id
    return True

def manage_home_data_get(request):
    manager = manage.objects.get(id=request.session['manage_id'])
    return {'manager':manager}

def manage_pet_farm_add(request):
    try:
        if request.POST['province'] == '':
            province = '四川'
        else:
            province = request.POST['province']
        if request.POST['city'] == '':
            city = '成都'
        else:
            city = request.POST['city']
        if request.POST['manage_score'] == '':
            manage_score = 1.0
        else:
            manage_score = string.atof(request.POST['manage_score'])
        new_pet_farm = pet_farm(name = request.POST['name'],
                                desc = request.POST['desc'],
                                province = province,
                                city = city,
                                district = request.POST['district'],
                                direct = request.POST['direct'],
                                min_prince = request.POST['min_prince'],
                                manage_score = manage_score)
        new_pet_farm.save()
    except NameError:
        return False
    return True

def manage_pet_farm_picadd(request):
    farms = pet_farm.objects.filter(dele=False)
    use_fors = []
    use_fors.append('buy_home')
    use_fors.append('narmol')
    return {'farms':farms,'use_fors':use_fors}

def manage_pet_farm_picupload(photo):
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
    if (w < 1170) or (h < 500):
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

def manage_pet_farm_picpreupload(request):
    if 'source' in request.POST:
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
        if (x2 - x1) > 243:
            cropimg.thumbnail( (243,150) )
        #file_name = '%s'%str(uuid.uuid1()) + '.png'
        file_name = request.POST['source'].split('/')[-1]
        file_path_name=settings.PET_FARM_PIC_ROOT + file_name
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
        #把url存入数据库
        pet_img = pet_farm_img( pet_farm_id = get_object_or_404(pet_farm,pk=string.atoi(request.POST['pet_farm_id'])),
                                img_url = img_url,
                                img_with = x2 - x1,
                                img_height = y2 - y1,
                                #img_type:jpg/png/...
                                img_type = 'png',
                                #图片用途
                                img_usefor = request.POST['usefor'])
        pet_img.save()
    return 'true'

def manage_ad_picpreupload(request):
    if 'source' in request.POST:
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
        if (x2 - x1) > 1170:
            cropimg.thumbnail( (1170,500) )
        #file_name = '%s'%str(uuid.uuid1()) + '.png'
        file_name = request.POST['source'].split('/')[-1]
        file_path_name=settings.PET_AD_ROOT + file_name
        url = ('/manage/pictest/'+file_name).encode('utf8')
        name = settings.STATIC_ROOT + url
        cropimg.save(name,'png')
        cropimg.close()
        print('111')
        up = UpYun('chongwug-pic','chongwug','weet6321')
        print('111')
        with open(name, 'rb') as f:
            res = up.put(file_path_name, f, checksum=False)
        #rr = _u.put(file_name, cropimg, checksum=False,headers={"x-gmkerl-rotate": "180"}) 
        #删除服务器本地缓存的图片
        os.remove(name)
        print('111')
        #writeFile方法不会返回图片地址，所以得自己写
        img_url = settings.PIC_ROOT + file_path_name
        #把url存入数据库
        print('111')
        ad_sql = ad( type = request.POST['type'],
                     tar_url = request.POST['tar_url'],
                     prince = string.atoi(request.POST['prince']),
                     start_time = datetime.datetime.strptime(request.POST['start_time'], "%Y-%m-%d %H:%M:%S"),
                     end_time = datetime.datetime.strptime(request.POST['end_time'], "%Y-%m-%d %H:%M:%S"),
                     img_url = img_url)
        print('111')
        ad_sql.save()
    return 'true'