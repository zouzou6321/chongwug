# -*- coding: UTF-8 -*-
from petlife.commom import __errorcode__
import models,datetime
from django.template import Context, Template 
from petlife.settings import STATIC_ROOT
import traceback

def authcheck(req):
    if 'user_id' in req.session:
        return True
    return False

def login(req):
    try:
        now_user = models.user.objects.get(name=req.POST['username'],passwd=req.POST['userpassd'])
        req.session['user_id'] = now_user.id
        return True
    except:
        return False

def home_unlogin(req):
    #查询
    try:
        pet = models.petinfo.objects.get(id_num=req.POST['petidnum'],petmaster__id_num=req.POST['masteridnum'])
        return pet
    except:
        return False

def home(req):
    print req.POST
    if 'pettype' in req.POST:
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