# -*- coding: UTF-8 -*-
__regular_expression_username = u'^([\u4e00-\u9fa5]+|([a-zA-Z]+\s?)+)$'
__regular_expression_idnum = r"^(^\d{15}$|^\d{18}$|^\d{17}(\d|X|x))$"

__pettypes = [u'泰迪',u'比熊',u'金毛',u'萨摩耶',u'哈士奇',u'拉布拉多',u'边牧',u'松狮',u'阿拉斯加', u'博美',u'巴哥',
              u'雪纳瑞',u'约克夏',u'德牧',u'古牧',u'比格',u'喜乐蒂',u'斗牛犬',u'杜宾',u'罗威纳',u'吉娃娃',u'卡斯罗',
              u'贵宾',u'马犬',u'史宾格']
__petcolors = [u'黑色',u'黑白斑点',u'黑白色',u'黄色',u'金黄色',u'白色',u'棕褐色',u'棕色']
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