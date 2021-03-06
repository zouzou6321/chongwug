# -*- coding: UTF-8 -*-
'''
Created on 2014年10月15日

@author: hhy
'''
from chongwug.config import __errorcode
import json,traceback,urllib,urllib2
from chongwug.settings import CKEDITOR_STATIC_URL,WAPALIPAY,ALIPAY_ID,ALIPAY_KEY,ALIPAY_EMAIL,ALIPAY
from ckeditor.widgets import CKEditorWidget
from django.core.exceptions import ImproperlyConfigured
from customer.models import appointorders
from random import Random

def random_str(randomlength=16):
    str = ''
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str

def __errorcode__(errornum,otherdata = None):
    index = 0
    for errorcode in __errorcode:
        if errornum == errorcode[0]:
            errornum = index
            break
        index += 1
    if otherdata != None:
        otherdata['status'] = __errorcode[errornum][0]
        otherdata['message'] = __errorcode[errornum][2]
        return json.dumps(otherdata)
    return json.dumps({"status":__errorcode[errornum][0],"message":__errorcode[errornum][2]})

def getalipayurl(out_trade_no, subject, total_fee,  notify_url,iswap):
    if iswap:
        return WAPALIPAY.create_direct_pay_by_user_url(out_trade_no=out_trade_no, subject=subject, total_fee=total_fee,seller_account_name="zhifubao@chongwug.com", call_back_url="http://m.chongwug.com/home/",notify_url=notify_url)
    else:
        return ALIPAY.create_direct_pay_by_user_url(out_trade_no=out_trade_no, subject=subject, total_fee=total_fee, notify_url=notify_url)

def sendSMS(telnum,SMScontent):
    url=u'http://api.cnsms.cn/?ac=send&uid=106869&pwd=4da6bfc8811f85d9d10b59690e31f6fc&mobile=%s&content=%s&encode=utf8' % (telnum, SMScontent)
    url=url.encode('utf-8')
    url=urllib2.unquote(url)
    content_stream = urllib.urlopen(url) 
    content = content_stream.read()
    if content != '100':
        return content
    return True

import config,sys,os

def flushconfig():
    keylist = dir(config)
    configfile = open(os.path.dirname(__file__).replace('\\','/') + '/config.py','w')
    configfile.write("# -*- coding: UTF-8 -*-\r\n")
    for key in keylist:
        if key == '__builtins__' or key == '__name__' or key == '__file__' or key == '__doc__' or key == '__package__':
            continue
        if len(key.split('regular_expression')) > 1 or len(key.split('upyun')) > 1:
            if len(key.split ('regular_expression_username')) > 1:
                str = u"%s = u'%s'\r\n" % (key, eval('config.' + key))
            else:
                str = u"%s = r'%s'\r\n" % (key, eval('config.' + key))
        else:
            str = u"%s = %s\r\n" % (key, eval('config.' + key))
        configfile.write(str.encode('utf8'))
    configfile.close()
    reload(config)  
    __import__('chongwug.config')

class SubdomainMiddleware(object):
    def process_request(self, request):
        domain_parts = request.get_host().split('.')
        if domain_parts[0] == 'm':
            # 将subdomain的信息放到URI的第一层级
            request.path_info = '/%s%s' % (domain_parts[0], request.path)
        return None

#重载CKEditorWidget,不要直接使用STATIC_URL作为目录，改成使用CKEDITOR_STATIC_URL
class myCKEditorWidget(CKEditorWidget):
    """
    Widget providing CKEditor for Rich Text Editing.
    Supports direct image uploads and embed.
    """
    class Media:
        js = ()
        try:
            js += (
                CKEDITOR_STATIC_URL + 'ckeditor/ckeditor.js',
                CKEDITOR_STATIC_URL + 'ckeditor/ckeditor-init.js',
            )
        except AttributeError:
            raise ImproperlyConfigured("django-ckeditor requires \
                    CKEDITOR_MEDIA_PREFIX setting. This setting specifies a \
                    URL prefix to the ckeditor JS and CSS media (not \
                    uploaded media). Make sure to use a trailing slash: \
                    CKEDITOR_MEDIA_PREFIX = '/media/ckeditor/'")