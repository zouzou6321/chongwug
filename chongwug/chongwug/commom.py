# -*- coding: UTF-8 -*-
'''
Created on 2014年10月15日

@author: hhy
'''
from chongwug.config import __errorcode
def __errorcode__(errornum):
    return '{"status":"%d","message":"%s"}' % (__errorcode[errornum][0], __errorcode[errornum][2])