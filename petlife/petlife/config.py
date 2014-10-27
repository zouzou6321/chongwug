# -*- coding: UTF-8 -*-
#系统错误码
__errorcode = [
               [0,u'success',u'成功'],
               [1,u'false',u'失败'],
               [2,u'email not exist',u'邮箱不存在'],
               [3,u'verifycode timeout',u'验证码超期，请重新获取验证码'],
               [4,u'verifycode out of time',u'验证码尝试超过三次，已经锁定,请24小时后重新获取验证码'],
               [5,u'verifycode error',u'验证码错误，请重新输入'],
               [6,u'verifycode send error',u'验证码发送错误，请联系管理员'],
               [6,u'verifycode times over',u'今天已经获取过验证码，请24小时后再来'],
               [404,u'page not found',u'页面不存在'],
               [500,u'internal fault',u'服务器内部错误']
              ]