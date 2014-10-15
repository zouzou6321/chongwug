# -*- coding: UTF-8 -*-
__adtypes = [[0,'nav_m','首页主广告']]
__petpictypes = [[0,u'buy_main',u'主图',275,180],[1,u'normal',u'辅图',600,400]]
__farmpictypes = [[0,u'buy_home',u'首页展示图',275,180],[1,u'normal',u'养殖场介绍图',600,400]]
__pettypes = [u'泰迪',u'比熊',u'金毛',u'萨摩耶',u'哈士奇',u'拉布拉多',u'边牧',u'松狮',u'阿拉斯加', u'博美',u'巴哥',
              u'雪纳瑞',u'约克夏',u'德牧',u'古牧',u'比格',u'喜乐蒂',u'斗牛犬',u'杜宾',u'罗威纳',u'吉娃娃']

#筛选页预置筛选条件
__prices = [{'a':'1','b':600,'c':1000},{'a':'2','b':1000,'c':1500},{'a':'3','b':1500,'c':2000},
            {'a':'4','b':2000,'c':2500},{'a':'5','b':2500,'c':1000000}]
__ages = [{'a':'1','b':0,'c':3},{'a':'2','b':3,'c':5},{'a':'3','b':5,'c':12},{'a':'4','b':12,'c':100000}]
__epidemics = [u'已种疫苗',u'可种疫苗',u'未种疫苗']
__directs = [u'东',u'西',u'南',u'北',u'中']
__errorcode = [
               [0,u'success',u'成功'],
               [1,u'false',u'失败'],
               [2,u'data error',u'提交的数据异常'],
               [3,u'primission delay',u'出现越权操作'],
               [4,u'picture not found',u'找不到图片'],
               [5,u'database access error',u'数据库访问错误'],
               [6,u'picture too small',u'图片太小'],
               [7,u'imperfect information',u'信息不完整，可能系统有虫子，请联系我们，谢谢~！'],
               [8,u'the pet sale out',u'实在抱歉，您想预定的宠物售罄了！'],
               [9,u'telephone num error',u'您这电话号码不对哦，任谁都通过它联系不到您呢~！'],
               [10,u'name error',u'您的名字~！'],
               [404,u'page not found',u'页面不存在'],
               [500,u'internal fault',u'服务器内部错误']
              ]