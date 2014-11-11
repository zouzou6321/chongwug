/*
Navicat MySQL Data Transfer

Source Server         : chongwug
Source Server Version : 50620
Source Host           : localhost:3306
Source Database       : chongwug

Target Server Type    : MYSQL
Target Server Version : 50620
File Encoding         : 65001

Date: 2014-11-11 14:10:09
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for manager_supplies
-- ----------------------------
DROP TABLE IF EXISTS `manager_supplies`;
CREATE TABLE `manager_supplies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` longtext NOT NULL,
  `img_url` varchar(200) NOT NULL,
  `tar_url` varchar(200) NOT NULL,
  `price` double NOT NULL,
  `title` longtext NOT NULL,
  `updatetime` datetime NOT NULL,
  `dele` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of manager_supplies
-- ----------------------------
INSERT INTO `manager_supplies` VALUES ('1', '必备用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/de4d1d0f-68c1-11e4-aad4-6c3be5803607.jpg', 'http://item.taobao.com/item.htm?spm=a1z0k.7385961.1997985097.d4918997.Y1GULZ&id=16184074398&_u=589heai83f1', '95', '金毛萨摩耶狗窝房子 方管宠物狗笼子中型犬小型犬泰迪比熊狗笼子', '2014-11-10 18:11:00', '0');
INSERT INTO `manager_supplies` VALUES ('2', '必备用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/12255c5e-68c2-11e4-ab63-6c3be5803607.jpg', 'http://item.taobao.com/item.htm?spm=a1z0k.7385961.1997985097.d4918997.Y1GULZ&id=3200082346&_u=589heai2166', '36.88', '全国24省包邮 宠物粗铁丝笼泰迪狗笼猫笼兔笼 小型犬大型犬狗笼子', '2014-11-10 18:12:27', '0');
INSERT INTO `manager_supplies` VALUES ('3', '必备用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/21f58480-68c2-11e4-a707-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.44.0Mx0DQ&id=16819346423&abbucket=16&_u=589heai459e', '99', '皇家狗粮幼犬 小型犬泰迪贵宾雪纳瑞比熊幼犬粮2kg犬主粮25省包邮', '2014-11-10 18:12:53', '0');
INSERT INTO `manager_supplies` VALUES ('4', '必备用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/686d1180-68c2-11e4-bb40-6c3be5803607.jpg', 'http://item.taobao.com/item.htm?spm=a230r.1.14.236.0Mx0DQ&id=38001396506&ns=1&abbucket=16&_u=589heai8a03', '89', '14省包邮.皇家MIJ 小型犬幼犬犬粮2kg 10月龄以下狗粮', '2014-11-10 18:14:52', '0');
INSERT INTO `manager_supplies` VALUES ('5', '必备用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/78198500-68c2-11e4-b5a0-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.60.VaI1KR&id=39069939579&abbucket=16&_u=589heaibd0d', '23.8', '特惠包邮 狗碗狗盆狗狗用品狗食盆 猫碗宠物用品 不锈钢精美双碗', '2014-11-10 18:15:18', '0');
INSERT INTO `manager_supplies` VALUES ('6', '必备用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/859fe430-68c2-11e4-98ce-6c3be5803607.jpg', 'http://item.taobao.com/item.htm?spm=a230r.1.14.27.VaI1KR&id=35246549497&ns=1&abbucket=16&_u=589heaie82b#detail', '22.8', 'super休普狗碗猫碗宠物碗不锈钢单碗猫盆狗盆圆形碗 秒杀包邮', '2014-11-10 18:15:40', '0');
INSERT INTO `manager_supplies` VALUES ('7', '生活用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/9daa3800-68c2-11e4-81c1-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?id=38556844853&ali_refid=a3_420434_1006:11…6e05&ali_trackid=1_2aa53058e9c7459a38ebede1a4d46e05&spm=a230r.1.0.0.B4BDss', '27', '得乐自动伸缩牵引绳 大中小型犬金毛泰迪狗链 狗绳 猫咪可用 包邮', '2014-11-10 18:16:21', '0');
INSERT INTO `manager_supplies` VALUES ('8', '生活用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/afce3b30-68c2-11e4-b184-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.1.B4BDss&id=10376884102&abbucket=16&_u=589heaia6af', '12.8', '包邮狗链子狗狗牵引绳胸背带宠物牵引绳金毛狗绳小型犬大型犬用品', '2014-11-10 18:16:51', '0');
INSERT INTO `manager_supplies` VALUES ('9', '生活用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/be95ccf0-68c2-11e4-a4ce-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.67.79rjyy&id=41207340994&abbucket=16&_u=589heai3f01', '16', '狗狗项圈 真牛皮狗圈防走失 大中小型犬猫颈圈宠物泰迪脖圈 包邮', '2014-11-10 18:17:16', '0');
INSERT INTO `manager_supplies` VALUES ('10', '生活用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/e7847800-68c2-11e4-b231-6c3be5803607.jpg', 'http://item.taobao.com/item.htm?id=35385164882&ali_refid=a3_420435_1006:110…058a&ali_trackid=1_52c46fba8145448d85f2f772bff6058a&spm=a230r.1.0.0.79rjyy', '5', '舒乐 12颗钻泰迪镶钻项圈 带钻 猫狗项圈 宠物项圈 随机发货 BJ', '2014-11-10 18:18:24', '0');
INSERT INTO `manager_supplies` VALUES ('11', '生活用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/f8d12e00-68c2-11e4-a8d4-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.35.WxtcuS&id=39007304413&abbucket=16&_u=589heai3214', '9.9', '狗嘴套 防咬防叫口罩 狗狗用品包邮 止吠器 泰迪贵宾金毛口罩', '2014-11-10 18:18:53', '0');
INSERT INTO `manager_supplies` VALUES ('12', '生活用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/0a3d79f0-68c3-11e4-8c89-6c3be5803607.jpg', 'http://item.taobao.com/item.htm?spm=a230r.1.14.141.colv4L&id=16004537644&ns=1&abbucket=16&_u=589heaia24b#detail ', '16.56', '狗掌狗窝泰迪博美比熊狗窝狗狗睡垫狗垫PP棉窝垫可配宠物毛毯被子', '2014-11-10 18:19:23', '0');
INSERT INTO `manager_supplies` VALUES ('13', '生活用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/2fb4ff9e-68c3-11e4-b552-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.1.hsGrEa&id=27388448077&ad_id=&am_id=&cm_id=140105335569ed55e27b&pm_id=&abbucket=16', '26', '1件包邮 吉米娃娃立体小狗狗衣服秋冬装四脚加厚宠物款泰迪小型犬', '2014-11-10 18:20:27', '0');
INSERT INTO `manager_supplies` VALUES ('14', '生活用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/4023d8c0-68c3-11e4-b1b6-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?id=41391544917&ali_refid=a3_420434_1006:11…28b4&ali_trackid=1_e31dae0301066c9b2fea71474e3e28b4&spm=a230r.1.0.0.aaEvKn', '16.5', '买二送毛巾狗狗鞋子泰迪宠物狗鞋子秋冬犬小狗防水羊羔绒棉鞋雪地 ', '2014-11-10 18:20:53', '0');
INSERT INTO `manager_supplies` VALUES ('15', '保健医疗', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/885571cf-68c3-11e4-9adf-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.1.abPLGn&id=18855625313&ad_id=&am_id=&cm_id=140105335569ed55e27b&pm_id=&abbucket=16', '28', '包邮 狗狗钙片宠物钙片大型幼犬泰迪萨摩耶金毛猫卫仕乳补钙粉片', '2014-11-10 18:22:54', '0');
INSERT INTO `manager_supplies` VALUES ('16', '保健医疗', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/968d46b0-68c3-11e4-bf34-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.98.NISFy5&id=23480496988&abbucket=16&_u=589heai2211', '28', '包邮送牛肉条 卫仕狗微量元素片160片 宠物微量元素粉 狗狗营养品', '2014-11-10 18:23:18', '0');
INSERT INTO `manager_supplies` VALUES ('18', '保健医疗', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/25464b40-68c4-11e4-97e1-6c3be5803607.jpg', 'http://item.taobao.com/item.htm?spm=a230r.1.14.240.s9rRt1&id=37814974776&ns=1&abbucket=16&_u=589heai1220#detail', '3', '狗狗感冒药 美贝惠中感康口服液 宠物咳嗽流鼻涕药 10ml单支', '2014-11-10 18:27:18', '0');
INSERT INTO `manager_supplies` VALUES ('19', '保健医疗', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/369ee81e-68c4-11e4-80df-6c3be5803607.jpg', 'http://item.taobao.com/item.htm?spm=a230r.1.14.129.DKicgc&id=17915138625&ns=1&abbucket=16&_u=589heai8d2a#detail', '15', '金盾消炎杀螨膏 狗狗皮肤病 抗真菌 消炎 止痒杀螨虫宠物药品 BJ', '2014-11-10 18:27:47', '0');
INSERT INTO `manager_supplies` VALUES ('20', '保健医疗', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/40c3cccf-68c4-11e4-92bf-6c3be5803607.jpg', 'http://item.taobao.com/item.htm?spm=a230r.1.0.0.YoQ9VZ&id=39516307765&ns=1&abbucket=16&_u=589heaie073#detail ', '25', '宠物/狗狗用品 新版英特威六联疫苗 含 六种病毒正品行货 冰袋邮', '2014-11-10 18:28:04', '0');
INSERT INTO `manager_supplies` VALUES ('21', '清洁卫生', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/571b4080-68c4-11e4-9108-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.1.QHEiya&id=9012967410&ad_id=&am_id=&cm_id=140105335569ed55e27b&pm_id=&abbucket=16 ', '25', '狗狗沐浴露包邮 除螨除臭止痒 泰迪金毛萨摩比熊专用宠物用品香波', '2014-11-10 18:28:41', '0');
INSERT INTO `manager_supplies` VALUES ('22', '清洁卫生', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/6ae26c5e-68c4-11e4-b0a0-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.114.QHEiya&id=13081872725&abbucket=16&_u=589heai102d', '22.8', '澳路雪杀菌止痒宠物沐浴露狗狗香波浴液泰迪金毛洗澡宠物用品包邮', '2014-11-10 18:29:14', '0');
INSERT INTO `manager_supplies` VALUES ('23', '清洁卫生', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/78080df0-68c4-11e4-9b5f-6c3be5803607.jpg', 'http://item.taobao.com/item.htm?id=26393340245&ali_refid=a3_420434_1006:110…557a&ali_trackid=1_d3defe947ea661f25d5b7826bdde557a&spm=a230r.1.0.0.WRj5bs', '19.8', '狗狗厕所特价小号大号 泰迪金毛宠物厕所围栏尿盆小型犬便盆用品', '2014-11-10 18:29:36', '0');
INSERT INTO `manager_supplies` VALUES ('24', '清洁卫生', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/849eb5f0-68c4-11e4-9ef0-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?id=37414900786&ali_refid=a3_420434_1006:11…e124&ali_trackid=1_b82957e84d3727cadafdbb6938b9e124&spm=a230r.1.0.0.t4Hbnj', '27', '雷米高路士宠物消毒液犬瘟细小病毒消毒水驱虫杀菌杀虫去味消毒剂', '2014-11-10 18:29:57', '0');
INSERT INTO `manager_supplies` VALUES ('25', '清洁卫生', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/90c7f621-68c4-11e4-b1c1-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?id=41431394905&ali_refid=a3_420434_1006:11…ea0b&ali_trackid=1_a6be350e0d84f821ba6005648f9aea0b&spm=a230r.1.0.0.v3f2UQ', '87', 'TOBY专业宠物吹风机/狗狗猫咪电吹风机筒/大功率低噪音包邮', '2014-11-10 18:30:18', '0');
INSERT INTO `manager_supplies` VALUES ('26', '清洁卫生', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/9eb4430f-68c4-11e4-90e0-6c3be5803607.jpg', 'http://item.taobao.com/item.htm?id=36811747954&ali_refid=a3_420434_1006:110…a5ee&ali_trackid=1_2fa69055d59cc042ffb8e3eb4425a5ee&spm=a230r.1.0.0.v3f2UQ', '265', '神悦 宠物吹水机 宠物专用 狗狗吹风机大功率 狗狗吹水机吹毛机', '2014-11-10 18:30:41', '0');
INSERT INTO `manager_supplies` VALUES ('27', '清洁卫生', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/a9787500-68c4-11e4-bb52-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.30.asx835&id=39205773451&abbucket=16&_u=589heai23c8', '9.9', '包邮 狗狗用品宠物开结梳狗毛梳狗梳子泰迪梳子宠物梳子猫狗针梳', '2014-11-10 18:30:59', '0');
INSERT INTO `manager_supplies` VALUES ('28', '保健医疗', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/5478491e-68c6-11e4-b460-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.287.Cr1H73&id=19156067147&abbucket=16&_u=589heai648e', '99', '拍下99 狗狗羊奶粉 宠物奶粉幼猫幼犬奶粉 卫仕营养小狗猫羊奶粉', '2014-11-10 18:42:56', '0');
INSERT INTO `manager_supplies` VALUES ('29', '保健医疗', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/6b5121cf-68c6-11e4-b486-6c3be5803607.jpg', 'http://item.taobao.com/item.htm?spm=a230r.1.0.0.YoQ9VZ&id=39516307765&ns=1&abbucket=16&_u=589heaie073#detail', '9.9', '全国包邮德国拜耳宠物驱虫药狗狗泰迪体内打虫药片犬用内服单粒装', '2014-11-10 18:43:34', '0');
INSERT INTO `manager_supplies` VALUES ('30', '必备用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/4636e1e1-68c7-11e4-8824-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.80.0Mx0DQ&id=9119089901&abbucket=16&_u=589heaibc89', '49', '皇家狗粮 皇家奶糕 泰迪幼犬小型犬离乳期奶糕1kg 比熊贵宾粮包邮', '2014-11-10 18:49:41', '0');
INSERT INTO `manager_supplies` VALUES ('31', '必备用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/77b7758f-68c7-11e4-8c63-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=a230r.1.14.249.0Mx0DQ&id=22269559298&abbucket=16&_u=589heai2346', '89', '22省包邮 皇家狗粮室内小型犬幼犬粮1.5KG泰迪博美小狗犬宠物主粮', '2014-11-10 18:51:04', '0');
INSERT INTO `manager_supplies` VALUES ('32', '保健医疗', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/bce4330f-68c7-11e4-be46-6c3be5803607.jpg', 'http://detail.tmall.com/item.htm?spm=608.7065813.ne.1.rkq0n3&id=12961947772&tracelog=jubuybigpic', '130', '狗狗羊奶粉安贝宠物羊奶粉泰迪金毛宠物幼犬幼猫咪奶粉300G包邮', '2014-11-10 18:53:00', '0');
INSERT INTO `manager_supplies` VALUES ('35', '清洁卫生', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/42ee0300-68c8-11e4-9395-6c3be5803607.jpg', 'http://item.taobao.com/item.htm?id=39829946989', '12', '宠物除臭剂杀菌喷剂 猫咪狗狗祛味香水 杀菌消毒环境消毒液 包邮', '2014-11-10 18:56:45', '0');
INSERT INTO `manager_supplies` VALUES ('36', '必备用品', 'http://chongwug-pic.b0.upaiyun.com/suppliepic/fef73a30-68d7-11e4-a33b-6c3be5803607.jpg', 'test', '22', '333', '2014-11-10 20:49:25', '1');
