# -*- coding: UTF-8 -*-
'''
Created on 2014年10月15日

@author: hhy
'''
from chongwug.config import __errorcode
import json,traceback,urllib,urllib2
from django.utils.log import AdminEmailHandler
from django.core.mail  import  send_mail
from chongwug.settings import EMAIL_HOST_USER,ADMINS
from django.views.debug import get_exception_reporter_filter
def __errorcode__(errornum,otherdata = None):
    index = 0
    for errorcode in __errorcode:
        if errornum == __errorcode[index][0]:
            errornum = index
            break
        index += 1
    if otherdata != None:
        otherdata['status'] = __errorcode[errornum][0]
        otherdata['message'] = __errorcode[errornum][2]
        return json.dumps(otherdata)
    return json.dumps({"status":__errorcode[errornum][0],"message":__errorcode[errornum][2]})

def sendSMS(telnum,SMScontent):
    url=u'http://api.cnsms.cn/?ac=send&uid=106869&pwd=4da6bfc8811f85d9d10b59690e31f6fc&mobile=%s&content=%s&encode=utf8' % (telnum, SMScontent)
    url=url.encode('utf-8')
    url=urllib2.unquote(url)
    content_stream = urllib.urlopen(url) 
    content = content_stream.read()
    if content != '100':
        return content
    return True

class myAdminEmailHandler(AdminEmailHandler):
    def emit(self, record):
        stack_trace = '\n'.join(traceback.format_exception(*record.exc_info))
        try:
            request = record.request
            subject = '%s ( IP): %s' % (
                record.levelname,
                record.getMessage()
            )
            filter = get_exception_reporter_filter(request)
            request_repr = filter.get_request_repr(request)
        except Exception:
            subject = '%s: %s' % (
                record.levelname,
                record.getMessage()
            )
            request = None
            request_repr = "Request repr() unavailable."
        message = "%s\n\n%s" % (stack_trace, request_repr)
        sender=EMAIL_HOST_USER
        mail_list= ADMINS
        send_mail(
                    subject=subject,  
                    message=message,  
                    from_email=sender,
                    recipient_list=mail_list,  
                    fail_silently=False,  
                    connection=None  
                ) 