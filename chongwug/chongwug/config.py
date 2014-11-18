# -*- coding: UTF-8 -*-
#所有图片的图片用途,目前暂时包括广告图片、宠物图片、养殖场图片
__adtypes = [[0,'nav_m','首页主广告',1920,530]]
__petpictypes = [[0,u'buy_main',u'主图',750,500],[1,u'normal',u'辅图',750,500]]
__farmpictypes = [[0,u'buy_home',u'首页展示图',427,300],[1,u'normal',u'养殖场介绍图',427,300]]
__supplietypes = [u'必备用品',u'生活用品',u'保健医疗',u'清洁卫生']
__onepageofdata__ = 12
#系统支持的犬种
__pettypes = [u'金毛',u'拉布拉多',u'泰迪熊',u'比熊',u'博美犬',u'贵宾犬',u'哈士奇',u'萨摩耶',u'边境牧羊犬',u'松狮',u'雪纳瑞',u'德国牧羊犬',u'巴哥犬',u'罗威纳',u'喜乐蒂',u'斗牛犬',u'约克夏',u'古牧',u'阿拉斯加',u'柯基犬',u'牛头梗',u'吉娃娃',u'腊肠犬',u'卡斯罗',u'中亚牧羊犬',u'拳师犬',u'比格犬',u'杜宾犬',u'杜高犬',u'比特犬',u'高加索犬',u'可卡犬',u'马犬',u'秋田犬',u'史宾格',u'柴犬']
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

#地址信息
__addresses = [
               {'name':'L-S','index':0,'sublist':[
                   {'name':u'四川','index':0,'sublist':[
                        {'name':u'成都','index':0,'sublist':[
                            {'name':u'高新区','index':0,'waitpoint':'成都市地铁一号线世纪城地铁站C1出口','sublist':[
                                {'name':'大源村','index':0},{'name':'芳草','index':1},{'name':'金融城','index':2},{'name':'理想中心','index':3},{'name':'美年广场','index':4},{'name':'南延线','index':5},{'name':'南苑','index':6},{'name':'神仙树','index':7},{'name':'世纪城','index':8},{'name':'天府长城','index':9},{'name':'肖家河','index':10},{'name':'中和镇','index':11},{'name':'紫荆','index':12}
                                ]
                            },
                            {'name':u'武侯区','index':1,'waitpoint':'成都市地铁一号线世纪城地铁站C1出口','sublist':[
                                {'name':'川大','index':0},{'name':'川音','index':1},{'name':'簇桥','index':2},{'name':'芳草街','index':3},{'name':'高攀路','index':4},{'name':'高升桥','index':5},{'name':'广福桥','index':6},{'name':'航空路','index':7},{'name':'好望角','index':8},{'name':'红牌楼','index':9},{'name':'红瓦寺','index':10},{'name':'火车南站','index':11},{'name':'金花镇','index':12},{'name':'机投镇','index':13},{'name':'科华路','index':14},{'name':'磨子桥','index':15},{'name':'内双楠','index':16},{'name':'清水河','index':17},{'name':'十二中','index':18},{'name':'跳伞塔','index':19},{'name':'桐梓林','index':20},{'name':'外双楠','index':21},{'name':'望江路','index':22},{'name':'五大花园','index':23},{'name':'武侯祠大街','index':24},{'name':'武侯周边','index':25},{'name':'肖家河','index':26},{'name':'小天竺街','index':27},{'name':'洗面桥','index':28},{'name':'衣冠庙','index':29},{'name':'玉林','index':30},{'name':'棕北','index':31},{'name':'棕南','index':32}
                                ]
                            },
                            {'name':u'金牛区','index':2,'waitpoint':'成都市地铁一号线世纪城地铁站C1出口','sublist':[
                                {'name':'茶店子','index':0},{'name':'抚琴小区','index':1},{'name':'国宾','index':2},{'name':'荷花池','index':3},{'name':'黄忠','index':4},{'name':'欢乐谷','index':5},{'name':'花牌坊','index':6},{'name':'火车北站','index':7},{'name':'交大路','index':8},{'name':'金牛万达','index':9},{'name':'金牛周边','index':10},{'name':'九里堤','index':11},{'name':'梁家巷','index':12},{'name':'李家沱','index':13},{'name':'马鞍路','index':14},{'name':'人民北路','index':15},{'name':'沙河源','index':16},{'name':'沙湾','index':17},{'name':'蜀汉路','index':18},{'name':'五块石','index':19},{'name':'营门口','index':20},{'name':'银沙','index':21},{'name':'一品天下','index':22}
                                ]
                            },
                            {'name':u'锦江区','index':3,'waitpoint':'成都市地铁一号线世纪城地铁站C1出口','sublist':[
                                {'name':'成仁路','index':0},{'name':'川师','index':1},{'name':'春熙路','index':2},{'name':'大慈寺','index':3},{'name':'大观','index':4},{'name':'东大街','index':5},{'name':'东光小区','index':6},{'name':'东教场','index':7},{'name':'海椒市','index':8},{'name':'合江亭','index':9},{'name':'红星路','index':10},{'name':'静居寺','index':11},{'name':'锦江周边','index':12},{'name':'九眼桥','index':13},{'name':'莲桂路','index':14},{'name':'龙舟路','index':15},{'name':'牛沙路','index':16},{'name':'牛市口','index':17},{'name':'牛王庙','index':18},{'name':'三圣乡','index':19},{'name':'沙河堡','index':20},{'name':'水碾河','index':21},{'name':'万达','index':22},{'name':'新南门','index':23},{'name':'盐市口','index':24}
                                ]
                            },
                            {'name':u'成华区','index':4,'waitpoint':'成都市地铁一号线世纪城地铁站C1出口','sublist':[
                                {'name':'八里小区','index':0},{'name':'财富又一城','index':1},{'name':'成华周边','index':2},{'name':'成渝立交','index':3},{'name':'崔家店','index':4},{'name':'东风路','index':5},{'name':'动物园','index':6},{'name':'二仙桥','index':7},{'name':'府青路','index':8},{'name':'槐树店','index':9},{'name':'火车东站','index':10},{'name':'建设路','index':11},{'name':'龙潭寺','index':12},{'name':'猛追湾','index':13},{'name':'青龙场','index':14},{'name':'杉板桥','index':15},{'name':'圣灯路','index':16},{'name':'十里店','index':17},{'name':'双林路','index':18},{'name':'双桥子','index':19},{'name':'驷马桥','index':20},{'name':'SM广场','index':21},{'name':'万年场','index':22},{'name':'五桂桥','index':23},{'name':'新鸿路','index':24},{'name':'新华公园','index':25}
                                ]
                            },
                            {'name':u'新都区','index':5,'waitpoint':'成都市地铁一号线世纪城地铁站C1出口','sublist':[
                                {'name':'斑竹园','index':0},{'name':'大丰','index':1},{'name':'军屯','index':2},{'name':'龙桥','index':3},{'name':'马家','index':4},{'name':'木兰','index':5},{'name':'清流','index':6},{'name':'三河','index':7},{'name':'石板滩','index':8},{'name':'泰兴','index':9},{'name':'新都老城区','index':10},{'name':'新都新城区','index':11},{'name':'新繁','index':12},{'name':'新民','index':13}
                                ]
                            },
                            {'name':u'双流县','index':6,'waitpoint':'成都市地铁一号线世纪城地铁站C1出口','sublist':[
                                {'name':'白家','index':0},{'name':'东升镇','index':1},{'name':'航空港','index':2},{'name':'黄龙溪','index':3},{'name':'华阳','index':4},{'name':'蛟龙港','index':5},{'name':'麓山','index':6},{'name':'牧马山','index':7},{'name':'彭镇','index':8},{'name':'双流周边','index':9},{'name':'文星','index':10}
                                ]
                            },
                            {'name':u'温江区','index':7,'waitpoint':'成都市地铁二号线犀浦地铁站A出口','sublist':[
                                {'name':'北部新城','index':0},{'name':'公平镇','index':1},{'name':'光华大道','index':2},{'name':'金马镇','index':3},{'name':'南熏大道','index':4},{'name':'寿安','index':5},{'name':'踏水镇','index':6},{'name':'万春镇','index':7},{'name':'温江城区','index':8},{'name':'永宁镇','index':9}
                                ]
                            },
                            {'name':u'龙泉驿区','index':8,'waitpoint':'成都市地铁二号线龙泉驿地铁站A出口','sublist':[
                                {'name':'滨河片区','index':0},{'name':'大面镇','index':1},{'name':'航天片区','index':2},{'name':'恒大绿洲','index':3},{'name':'洪河镇','index':4},{'name':'龙泉驿周边','index':5},{'name':'商业片区','index':6},{'name':'十陵镇','index':7},{'name':'阳光城','index':8},{'name':'总站片区','index':9}
                                ]
                            },
                            {'name':u'青羊区','index':9,'waitpoint':'成都市地铁一号线世纪城地铁站C1出口','sublist':[
                                {'name':'八宝街','index':0},{'name':'白果林','index':1},{'name':'贝森','index':2},{'name':'草市街','index':3},{'name':'草堂','index':4},{'name':'长顺街','index':5},{'name':'府南新区','index':6},{'name':'浣花小区','index':7},{'name':'金沙','index':8},{'name':'内光华','index':9},{'name':'宁夏街','index':10},{'name':'青羊周边','index':11},{'name':'人民公园','index':12},{'name':'石人','index':13},{'name':'顺城街','index':14},{'name':'太升路','index':15},{'name':'天府广场','index':16},{'name':'同仁路','index':17},{'name':'外光华','index':18},{'name':'外金沙','index':19},{'name':'文殊坊','index':20},{'name':'西南财大区','index':21},{'name':'新城市广场','index':22},{'name':'西月城街','index':23},{'name':'中医附院','index':24}
                                ]
                            },
                            {'name':u'郫县','index':10,'waitpoint':'成都市地铁二号线犀浦地铁站A出口','sublist':[
                                {'name':'安德','index':0},{'name':'安靖','index':1},{'name':'德源','index':2},{'name':'古城','index':3},{'name':'红光','index':4},{'name':'郫筒','index':5},{'name':'三道堰','index':6},{'name':'唐昌','index':7},{'name':'唐元','index':8},{'name':'团结','index':9},{'name':'新民场','index':10},{'name':'犀浦','index':11},{'name':'友爱','index':12}
                                ]
                            },
                            {'name':u'高新西区','index':11,'waitpoint':'成都市地铁二号线犀浦地铁站A出口','sublist':[
                                {'name':'土桥','index':0},{'name':'何家桥','index':1},{'name':'中海国际','index':2}
                                ]
                            },
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
               [23,u'sms send times to many',u'今天的短信获取已达上限，请24小时过后再尝试'],
               [24,u'aready attentioned',u'您已经预约了去看本窝犬了'],
               [404,u'page not found',u'页面不存在'],
               [500,u'internal fault',u'服务器内部错误']
              ]