# -*- coding: UTF-8 -*-
from petlife.commom import __errorcode__,sendemailbythread
import models,datetime
from django.template import Context, Template 
from petlife.settings import STATIC_ROOT
import traceback,random,thread,re
from petlife.config import __regular_expression_username,__regular_expression_idnum

def authcheck(req):
    if 'user_id' in req.session:
        return True
    return False

def login(req):
    try:
        now_user = models.user.objects.get(name=req.POST['username'],passwd=req.POST['userpassd'])
        now_user.verifytimes = 0
        now_user.verifydatetime = datetime.datetime(1980,7,1)
        now_user.save()
        req.session['user_id'] = now_user.id
        if 'remember' in req.POST and req.POST['remember'] == 'true':
            req.session.set_expiry(60 * 60 * 24 * 14)
        else:
            req.session.set_expiry(0)
        return True
    except:
        return False

def pwdback(req):
    try:
        user = models.user.objects.get(email=req.POST['email'])
    except:
        return __errorcode__(2)
    dt = user.verifydatetime
    dt = dt.replace(tzinfo=None)
    if 'newpwd' in req.POST:
        try:
            if (datetime.datetime.now() - dt).seconds > 60 * 60 * 24:
                return __errorcode__(3)
            if user.verifytimes >= 3:
                return __errorcode__(4)
            if user.verifycode == req.POST['verifycode']:
                user.verifytimes = 0
                user.passwd = req.POST['newpwd']
                user.verifydatetime = datetime.datetime(1980,7,1)
                user.save()
                return __errorcode__(0)
            else:
                user.verifytimes = user.verifytimes + 1
                user.save()
                return __errorcode__(5)
        except:
            return __errorcode__(3)
    try:
        print (datetime.datetime.now() - dt).days
        if (datetime.datetime.now() - dt).days < 1:
            return __errorcode__(7)
        if user.verifytimes >= 3:
            return __errorcode__(4)
        verifycode = random.randint(1000, 9999)
        subject=u'忘记密码，获取验证码'
        html_content = u'您好，%s,您的验证码是%d，请在忘记密码页面输入此验证码重新设置您的密码!' % (user.name, verifycode)
        thread.start_new_thread(sendemailbythread, (user.email,html_content,subject))
        user.verifycode = verifycode
        user.verifydatetime = datetime.datetime.now()
        user.save()
    except:
        return __errorcode__(6)
    return __errorcode__(0)

def home_unlogin(req):
    #查询
    try:
        pet = models.petinfo.objects.get(id_num=req.POST['petidnum'],petmaster__id_num=req.POST['masteridnum'])
        return pet
    except:
        return False

def home(req):
    if 'pettype' in req.POST:
        p = re.compile(__regular_expression_username)
        if not p.match(req.POST['mastername']):
            return __errorcode__(10)
        p = re.compile(__regular_expression_username)
        if not p.match(req.POST['breedername']):
            return __errorcode__(10)
        
        p = re.compile(__regular_expression_idnum)
        if not p.match(req.POST['masteridnum']):
            return __errorcode__(17)
        p = re.compile(__regular_expression_idnum)
        if not p.match(req.POST['breederidnum']):
            return __errorcode__(17)
        #录入
        pet = models.petinfo.objects.filter(id_num=req.POST['petidnum'])
        if pet.count() > 0:
            return __errorcode__(1)
        try:
            master = models.personinfo.objects.get(id_num=req.POST['masteridnum'])
        except:
            master = models.personinfo(name = req.POST['mastername'],
                                        id_num = req.POST['masteridnum'],
                                        contact = req.POST['mastercontact'],
                                       )
            master.save()
        try:
            master = models.personinfo.objects.get(id_num=req.POST['masteridnum'])
        except:
            master = models.personinfo(name = req.POST['mastername'],
                                        id_num = req.POST['masteridnum'],
                                        contact = req.POST['mastercontact'],
                                       )
            master.save()
        try:
            breeder = models.personinfo.objects.get(id_num=req.POST['breederidnum'])
        except:
            breeder = models.personinfo(name = req.POST['breedername'],
                                        id_num = req.POST['breederidnum'],
                                        contact = req.POST['breedercontact'],
                                       )
            breeder.save()
        try:
            new_pet = models.petinfo(id_num = req.POST['petidnum'],
                                    type = req.POST['pettype'],
                                    englishname = req.POST['petenglish'],
                                    sex = req.POST['petsex'],
                                    color = req.POST['petcolor'],
                                    birthdate = datetime.datetime.strptime(req.POST['petbirthdate'], "%Y-%m-%d"),
                                    petmaster = master,
                                    petbreeder = breeder,
                                    father = req.POST['petfather'],
                                    mather = req.POST['petmather'],
                                     )
            new_pet.save()
            fp = open('%s/petmicro/tpl/home_get_ajax.html' % STATIC_ROOT)  
            t = Template(fp.read())
            c = Context({'pet':new_pet})  
            html = t.render(c)  
            return __errorcode__(0,{'html':html})
        except:
            traceback.print_exc()
    elif 'idnum' in req.POST:
        #查询
        try:
            pet = models.petinfo.objects.get(id_num=req.POST['idnum'])
            fp = open('%s/petmicro/tpl/home_get_ajax.html' % STATIC_ROOT)  
            t = Template(fp.read())
            c = Context({'pet':pet})  
            html = t.render(c)  
            return __errorcode__(0,{'html':html})
        except:
            return __errorcode__(1)
    return __errorcode__(1)