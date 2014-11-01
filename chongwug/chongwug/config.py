# -*- coding: UTF-8 -*-
#所有图片的图片用途,目前暂时包括广告图片、宠物图片、养殖场图片
__adtypes = [[0,'nav_m','首页主广告',1920,530]]
__petpictypes = [[0,u'buy_main',u'主图',750,500],[1,u'normal',u'辅图',750,500]]
__farmpictypes = [[0,u'buy_home',u'首页展示图',427,300],[1,u'normal',u'养殖场介绍图',427,300]]

#系统支持的犬种
__pettypes = [u'泰迪',u'比熊',u'金毛',u'萨摩耶',u'哈士奇',u'拉布拉多',u'边牧',u'松狮',u'阿拉斯加', u'博美',u'巴哥',
              u'雪纳瑞',u'约克夏',u'德牧',u'古牧',u'比格',u'喜乐蒂',u'斗牛犬',u'杜宾',u'罗威纳',u'吉娃娃',u'卡斯罗',
              u'贵宾',u'马犬',u'史宾格']
__petcolors = [u'黑色',u'黑白斑点',u'黑白色',u'黄色',u'金黄色',u'白色',u'棕褐色',u'棕色']
__petages = [1,2,3,4,5,6,7,8,9,10,11,12]
#筛选页预置筛选条件
__prices = [{'a':'1','b':600,'c':1000,'d':'600-1000'},{'a':'2','b':1000,'c':1500,'d':'1000-1500'},{'a':'3','b':1500,'c':2000,'d':'1500-2000'},
            {'a':'4','b':2000,'c':2500,'d':'2000-2500'},{'a':'5','b':2500,'c':1000000,'d':'2500以上'}]
__ages = [{'a':'1','b':0,'c':3,'d':'0-3月'},{'a':'2','b':3,'c':5,'d':'3-5月'},{'a':'3','b':5,'c':12,'d':'5-12月'},{'a':'4','b':12,'c':100000,'d':'12个月以上'}]
__epidemics = [u'已种疫苗',u'可种疫苗',u'未种疫苗']
__directs = [u'东',u'西',u'南',u'北']

#账号密码
__upyun_picpath = 'chongwug-pic'
__upyun_name = 'chongwug'
__upyun_pwd = 'weet6321'

#系统使用的正则表达式
__regular_expression_telnum = r'1\d{10}'
__regular_expression_chinatelnum = r'^\(?0\d{2,3}\)?[- ]?\d{7,8}|^0\d{2,3}[- ]?\d{7,8}|^1\d{10}|\(?\+?\d{2,3}\)?[- ]?0\d{2,3}[- ]?\d{7,8}|^\d{7,8}'
__regular_expression_username = u'^([\u4e00-\u9fa5]+|([a-zA-Z]+\s?)+)$'
__regular_expression_email = r"^(\w)+(\.\w+)*@(\w)+((\.\w+)+)$"
__regular_expression_idnum = r"^(^\d{15}$|^\d{18}$|^\d{17}(\d|X|x))$"

#评分档次
__petfeaturescore = [45,70,100]

#服务费与交通费
__servpay = 15
__transpay = 5

#预约时间信息
__appointtime = {'time1':'9:30','time2':'15:00'}
__appointdays = [
                    {'day':20,'year':2014,'mouth':10,'week':'周一','selectable':{'time1':True,'time2':True}},
                    {'day':23,'year':2014,'mouth':10,'week':'周四','selectable':{'time1':True,'time2':True}},
                    {'day':26,'year':2014,'mouth':10,'week':'周日','selectable':{'time1':False,'time2':True}},
                    {'day':29,'year':2014,'mouth':10,'week':'周三','selectable':{'time1':True,'time2':True}},
                    {'day':1,'year':2014,'mouth':11,'week':'周六','selectable':{'time1':False,'time2':True}},
                    {'day':4,'year':2014,'mouth':11,'week':'周二','selectable':{'time1':True,'time2':True}},
                    {'day':7,'year':2014,'mouth':11,'week':'周五','selectable':{'time1':True,'time2':True}},
                    {'day':10,'year':2014,'mouth':11,'week':'周一','selectable':{'time1':True,'time2':True}}
                ]
#地址信息
__addresses = [
               {'name':'L-S','index':0,'sublist':[
                   {'name':u'四川','index':0,'sublist':[
                        {'name':u'成都','index':0,'sublist':[
                            {'name':u'高新区','index':0,'waitpoint':'成都市世纪城地铁站C出口','sublist':[
                                {'name':u'天府一街','index':0},
                                {'name':u'软件园','index':1},
                                {'name':u'天河一路','index':2},
                                {'name':u'世纪城','index':3}
                                ]
                            },
                            {'name':u'武侯区','index':1,'waitpoint':'四川大学望江小区西门','sublist':[
                                {'name':u'青羊宫','index':0}
                                ]
                            },
                            {'name':u'金牛区','index':2,'waitpoint':'成都市金牛万达广场','sublist':[
                                {'name':u'金牛万达','index':0},
                                {'name':u'荷花池','index':1},
                                {'name':u'火车北站','index':2}
                                ]
                            },
                            {'name':u'锦江区','index':3,'waitpoint':'成都市天府广场','sublist':[
                                {'name':u'天府一街','index':0},
                                {'name':u'软件园','index':1},
                                {'name':u'天河一路','index':2},
                                {'name':u'世纪城','index':3}
                                ]
                            },
                            {'name':u'新堵区','index':4,'waitpoint':'不晓得哪个地名可以用','sublist':[
                                {'name':u'天府一街','index':0},
                                {'name':u'软件园','index':1},
                                {'name':u'天河一路','index':2},
                                {'name':u'世纪城','index':3}
                                ]
                            },
                            {'name':u'双流县','index':5,'waitpoint':'成都市双流县双流客运站入口处','sublist':[
                                {'name':u'天府一街','index':0},
                                {'name':u'软件园','index':1},
                                {'name':u'天河一路','index':2},
                                {'name':u'世纪城','index':3}
                                ]
                            }
                            ]
                        }
                        ]
                   }
                   ]
                }
            ]

#系统错误码
__errorcode = [
               [0,u'success',u'成功'],
               [1,u'false',u'失败'],
               [2,u'data error',u'提交的数据异常'],
               [3,u'primission delay',u'出现越权操作'],
               [4,u'picture not found',u'找不到图片,请重新上传'],
               [5,u'database access error',u'数据库访问错误'],
               [6,u'picture too small',u'图片太小'],
               [7,u'imperfect information',u'信息不完整，可能系统有虫子，请联系我们，谢谢~！'],
               [8,u'the pet sale out',u'实在抱歉，您想预定的宠物售罄了！'],
               [9,u'telephone num error',u'您这电话号码不对哦，任谁都通过它联系不到您呢~！'],
               [10,u'name error',u'您的名字~！'],
               [11,u'address error',u'您选择的地址不对呢！'],
               [12,u'time error',u'您选择的时间不对呢！'],
               [13,u'crop size error',u'截取图片的长宽不匹配，请尝试重新截取'],
               [14,u'time format error',u'时间格式不正确，示例：2014-10-22 14:22:35'],
               [15,u'prince error',u'价格输入错误，请输入正整数'],
               [16,u'email error',u'错误的邮箱'],
               [17,u'idnum error',u'身份证号不正确'],
               [18,u'direct error',u'方位选择不正确'],
               [19,u'manage score error',u'评分数据不正确'],
               [20,u'short desc error',u'简介不可以为空'],
               [21,u'pwd can not be null',u'密码不能为空'],
               [22,u'main img lost',u'未识别到主图，请确保主图存在'],
               [404,u'page not found',u'页面不存在'],
               [500,u'internal fault',u'服务器内部错误']
              ]