# -*- coding: UTF-8 -*-
__regular_expression_username = u'^([\u4e00-\u9fa5]+|([a-zA-Z]+\s?)+)$'
__regular_expression_idnum = r"^(^\d{15}$|^\d{18}$|^\d{17}(\d|X|x))$"

__pettypes = __pettypes = [u'金毛',u'拉布拉多',u'泰迪熊',u'比熊',u'博美犬',u'贵宾犬',u'哈士奇',u'萨摩耶',u'边境牧羊犬',u'松狮',u'雪纳瑞',u'德国牧羊犬',u'巴哥犬',u'罗威纳',u'喜乐蒂',u'斗牛犬',u'约克夏',u'古牧',u'阿拉斯加',u'柯基犬',u'牛头梗',u'吉娃娃',u'腊肠犬',u'卡斯罗',u'中亚牧羊犬',u'拳师犬',u'比格犬',u'杜宾犬',u'杜高犬',u'比特犬',u'高加索犬',u'可卡犬',u'马犬',u'秋田犬',u'史宾格',u'柴犬']
#系统错误码
__errorcode = [
               [0,u'success',u'成功'],
               [1,u'false',u'失败'],
               [2,u'email not exist',u'邮箱不存在'],
               [3,u'verifycode timeout',u'验证码超期，请重新获取验证码'],
               [4,u'verifycode out of time',u'验证码尝试超过三次，已经锁定,请24小时后重新获取验证码'],
               [5,u'verifycode error',u'验证码错误，请重新输入'],
               [6,u'verifycode send error',u'验证码发送错误，请联系管理员'],
               [7,u'verifycode times over',u'今天已经获取过验证码，请24小时后再来'],
               [404,u'page not found',u'页面不存在'],
               [500,u'internal fault',u'服务器内部错误']
              ]