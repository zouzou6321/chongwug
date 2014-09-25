# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.
    
#管理员帐号，不一定每个都有，主要是负责数据编辑的人员使用
class manage(models.Model):
    name = models.TextField()
    passwd = models.TextField()
    #作业类型
    type = models.TextField()
    permission_score = models.IntegerField()
    dele = models.BooleanField(default=False)