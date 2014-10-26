# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.


class user(models.Model):
    name = models.TextField()
    passwd = models.TextField()
    id_num = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)

class personinfo(models.Model):
    name = models.TextField()
    id_num = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)

class petinfo(models.Model):
    id_num = models.TextField()
    type = models.TextField()
    englishname = models.TextField()
    sex = models.TextField()
    color = models.TextField()
    birthdate = models.TimeField()
    #宠物主人
    petmaster = models.ForeignKey(personinfo,blank=True, null=True,related_name='petmaster')
    #宠物繁殖者
    petbreeder = models.ForeignKey(personinfo,blank=True, null=True,related_name='petbreeder')
    father = models.TextField()
    mather = models.TextField()