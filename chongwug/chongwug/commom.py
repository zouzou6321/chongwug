# -*- coding: UTF-8 -*-
'''
Created on 2014年10月15日

@author: hhy
'''
from chongwug.config import __errorcode
import json
def __errorcode__(errornum,otherdata = None):
    if otherdata != None:
        otherdata['status'] = __errorcode[errornum][0]
        otherdata['message'] = __errorcode[errornum][2]
        return json.dumps(otherdata,ensure_ascii = False)
    return json.dumps({"status":__errorcode[errornum][0],"message":__errorcode[errornum][2]},ensure_ascii = False)