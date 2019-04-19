/*
Navicat MySQL Data Transfer

Source Server         : 本地数据库
Source Server Version : 50549
Source Host           : localhost:3306
Source Database       : cshop

Target Server Type    : MYSQL
Target Server Version : 50549
File Encoding         : 65001

Date: 2019-04-19 15:31:42
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------
INSERT INTO `auth_group` VALUES ('1', '商家');

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------
INSERT INTO `auth_group_permissions` VALUES ('6', '1', '31');
INSERT INTO `auth_group_permissions` VALUES ('1', '1', '32');
INSERT INTO `auth_group_permissions` VALUES ('2', '1', '33');
INSERT INTO `auth_group_permissions` VALUES ('3', '1', '40');
INSERT INTO `auth_group_permissions` VALUES ('4', '1', '41');
INSERT INTO `auth_group_permissions` VALUES ('5', '1', '42');
INSERT INTO `auth_group_permissions` VALUES ('7', '1', '59');

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('5', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('8', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('9', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can add user', '4', 'add_user');
INSERT INTO `auth_permission` VALUES ('11', 'Can change user', '4', 'change_user');
INSERT INTO `auth_permission` VALUES ('12', 'Can delete user', '4', 'delete_user');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '5', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '5', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '5', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can add session', '6', 'add_session');
INSERT INTO `auth_permission` VALUES ('17', 'Can change session', '6', 'change_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can delete session', '6', 'delete_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can add 买家信息', '7', 'add_user_message');
INSERT INTO `auth_permission` VALUES ('20', 'Can change 买家信息', '7', 'change_user_message');
INSERT INTO `auth_permission` VALUES ('21', 'Can delete 买家信息', '7', 'delete_user_message');
INSERT INTO `auth_permission` VALUES ('22', 'Can add 商品', '8', 'add_goodsinfo');
INSERT INTO `auth_permission` VALUES ('23', 'Can change 商品', '8', 'change_goodsinfo');
INSERT INTO `auth_permission` VALUES ('24', 'Can delete 商品', '8', 'delete_goodsinfo');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 商品分类', '9', 'add_goodstype');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 商品分类', '9', 'change_goodstype');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 商品分类', '9', 'delete_goodstype');
INSERT INTO `auth_permission` VALUES ('28', 'Can add 买家信息', '7', 'add_user');
INSERT INTO `auth_permission` VALUES ('29', 'Can change 买家信息', '7', 'change_user');
INSERT INTO `auth_permission` VALUES ('30', 'Can delete 买家信息', '7', 'delete_user');
INSERT INTO `auth_permission` VALUES ('31', 'Can add 商品', '10', 'add_goodsinfo');
INSERT INTO `auth_permission` VALUES ('32', 'Can change 商品', '10', 'change_goodsinfo');
INSERT INTO `auth_permission` VALUES ('33', 'Can delete 商品', '10', 'delete_goodsinfo');
INSERT INTO `auth_permission` VALUES ('34', 'Can add 商品分类', '11', 'add_goodstype');
INSERT INTO `auth_permission` VALUES ('35', 'Can change 商品分类', '11', 'change_goodstype');
INSERT INTO `auth_permission` VALUES ('36', 'Can delete 商品分类', '11', 'delete_goodstype');
INSERT INTO `auth_permission` VALUES ('37', 'Can add 商品大类', '12', 'add_bigtype');
INSERT INTO `auth_permission` VALUES ('38', 'Can change 商品大类', '12', 'change_bigtype');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete 商品大类', '12', 'delete_bigtype');
INSERT INTO `auth_permission` VALUES ('40', 'Can add 商品细节', '13', 'add_detail');
INSERT INTO `auth_permission` VALUES ('41', 'Can change 商品细节', '13', 'change_detail');
INSERT INTO `auth_permission` VALUES ('42', 'Can delete 商品细节', '13', 'delete_detail');
INSERT INTO `auth_permission` VALUES ('43', 'Can add 购物车', '14', 'add_car');
INSERT INTO `auth_permission` VALUES ('44', 'Can change 购物车', '14', 'change_car');
INSERT INTO `auth_permission` VALUES ('45', 'Can delete 购物车', '14', 'delete_car');
INSERT INTO `auth_permission` VALUES ('46', 'Can add 收货地址', '15', 'add_adress');
INSERT INTO `auth_permission` VALUES ('47', 'Can change 收货地址', '15', 'change_adress');
INSERT INTO `auth_permission` VALUES ('48', 'Can delete 收货地址', '15', 'delete_adress');
INSERT INTO `auth_permission` VALUES ('49', 'Can add 收货地址', '15', 'add_address');
INSERT INTO `auth_permission` VALUES ('50', 'Can change 收货地址', '15', 'change_address');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete 收货地址', '15', 'delete_address');
INSERT INTO `auth_permission` VALUES ('52', 'Can add 收藏', '16', 'add_collection');
INSERT INTO `auth_permission` VALUES ('53', 'Can change 收藏', '16', 'change_collection');
INSERT INTO `auth_permission` VALUES ('54', 'Can delete 收藏', '16', 'delete_collection');
INSERT INTO `auth_permission` VALUES ('59', 'Can change 订单总览', '18', 'change_orders');
INSERT INTO `auth_permission` VALUES ('60', 'Can delete 订单总览', '18', 'delete_orders');

-- ----------------------------
-- Table structure for auth_user
-- ----------------------------
DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user
-- ----------------------------
INSERT INTO `auth_user` VALUES ('1', 'pbkdf2_sha256$100000$t9DpUtmKcwn8$AglNtgMdSO+z05pX6yaAcmsnoQmQmYavuWwW9SPRj5Q=', '2019-03-29 02:19:12', '1', 'liuhuan', '刘欢', '', '18737307883@sina.cn', '1', '1', '2019-03-21 06:10:00');
INSERT INTO `auth_user` VALUES ('2', 'pbkdf2_sha256$100000$KEA9WbXaE773$cT3JVmKGZgcWZoLnNGy3MTsq9GZS0gSX/ZwPpC++cBQ=', '2019-03-29 02:57:11', '0', 'xiaoxiaocao', '肖晓草', '肖', '', '1', '1', '2019-03-21 10:48:00');

-- ----------------------------
-- Table structure for auth_user_groups
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_groups
-- ----------------------------
INSERT INTO `auth_user_groups` VALUES ('1', '2', '1');

-- ----------------------------
-- Table structure for auth_user_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_user_user_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-03-21 06:27:03', '1', '个护美妆', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2019-03-21 06:30:03', '2', '服装', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2019-03-21 06:30:26', '3', '电子产品', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2019-03-21 06:30:55', '4', '鞋子', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2019-03-21 06:31:38', '5', '零食', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2019-03-21 06:32:04', '6', '生活用品', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2019-03-21 06:32:44', '7', '背包', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2019-03-21 06:33:10', '1', '面部护肤', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2019-03-21 06:33:45', '2', '洗发护发', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2019-03-21 06:36:22', '3', '身体护理', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2019-03-21 06:36:37', '4', '口腔护理', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2019-03-21 06:37:00', '5', '女性个护', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2019-03-21 06:37:21', '6', '香水彩妆', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2019-03-21 06:38:10', '7', '电脑', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2019-03-21 06:38:25', '8', '手机', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2019-03-21 06:38:46', '9', '充电宝', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2019-03-21 06:39:00', '10', '手环', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2019-03-21 06:39:33', '11', '女士上衣', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2019-03-21 06:39:51', '12', '男士上衣', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2019-03-21 06:40:08', '13', '男士裤子', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('21', '2019-03-21 06:40:36', '14', '女士裤子', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('22', '2019-03-21 06:41:05', '15', '男士运动装', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('23', '2019-03-21 06:41:25', '15', '男士运动装', '2', '[{\"changed\": {\"fields\": [\"type\"]}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('24', '2019-03-21 06:41:41', '16', '女士运动装', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('25', '2019-03-21 06:42:08', '17', '男士休闲鞋', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('26', '2019-03-21 06:42:20', '18', '男士篮球鞋', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('27', '2019-03-21 06:42:35', '18', '男士篮球鞋', '2', '[{\"changed\": {\"fields\": [\"type\"]}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('28', '2019-03-21 06:43:28', '19', '皮鞋', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('29', '2019-03-21 10:47:43', '1', 'liuhuan', '2', '[{\"changed\": {\"fields\": [\"last_login\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('30', '2019-03-21 10:48:17', '2', 'xiaoxiaocao', '1', '[{\"added\": {}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('31', '2019-03-21 10:49:00', '2', 'xiaoxiaocao', '2', '[{\"changed\": {\"fields\": [\"first_name\", \"last_name\", \"is_staff\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('32', '2019-03-21 10:49:26', '1', 'liuhuan', '2', '[{\"changed\": {\"fields\": [\"first_name\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('33', '2019-03-21 10:57:57', '1', '商家', '1', '[{\"added\": {}}]', '3', '1');
INSERT INTO `django_admin_log` VALUES ('34', '2019-03-21 10:58:29', '2', 'xiaoxiaocao', '2', '[{\"changed\": {\"fields\": [\"groups\"]}}]', '4', '1');
INSERT INTO `django_admin_log` VALUES ('35', '2019-03-21 11:27:44', '20', '女士运动鞋', '1', '[{\"added\": {}}]', '11', '1');
INSERT INTO `django_admin_log` VALUES ('36', '2019-03-21 11:33:03', '1', '乐途女士经典跑鞋', '1', '[{\"added\": {}}, {\"added\": {\"name\": \"\\u5546\\u54c1\\u7ec6\\u8282\", \"object\": \"Detail object (1)\"}}, {\"added\": {\"name\": \"\\u5546\\u54c1\\u7ec6\\u8282\", \"object\": \"Detail object (2)\"}}, {\"added\": {\"name\": \"\\u5546\\u54c1\\u7ec6\\u8282\", \"object\": \"Detail object (3)\"}}]', '10', '2');
INSERT INTO `django_admin_log` VALUES ('37', '2019-03-26 10:43:23', '2', '运动休闲鞋', '1', '[{\"added\": {}}, {\"added\": {\"name\": \"\\u5546\\u54c1\\u7ec6\\u8282\", \"object\": \"Detail object (4)\"}}, {\"added\": {\"name\": \"\\u5546\\u54c1\\u7ec6\\u8282\", \"object\": \"Detail object (5)\"}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('38', '2019-03-26 10:45:18', '2', '运动休闲鞋', '2', '[{\"changed\": {\"fields\": [\"oprice\", \"xprice\"]}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('39', '2019-03-26 10:53:09', '3', '跑步鞋', '1', '[{\"added\": {}}, {\"added\": {\"name\": \"\\u5546\\u54c1\\u7ec6\\u8282\", \"object\": \"Detail object (6)\"}}, {\"added\": {\"name\": \"\\u5546\\u54c1\\u7ec6\\u8282\", \"object\": \"Detail object (7)\"}}, {\"added\": {\"name\": \"\\u5546\\u54c1\\u7ec6\\u8282\", \"object\": \"Detail object (8)\"}}]', '10', '1');
INSERT INTO `django_admin_log` VALUES ('40', '2019-03-29 02:35:56', '20', '1553775121610677', '2', '[{\"changed\": {\"fields\": [\"send_status\"]}}]', '18', '1');
INSERT INTO `django_admin_log` VALUES ('41', '2019-03-29 02:50:46', '55', 'seller | 订单详情 | Can add 订单详情', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('42', '2019-03-29 02:50:46', '56', 'seller | 订单详情 | Can change 订单详情', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('43', '2019-03-29 02:50:46', '57', 'seller | 订单详情 | Can delete 订单详情', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('44', '2019-03-29 02:52:00', '58', 'seller | 订单总览 | Can add 订单总览', '3', '', '2', '1');
INSERT INTO `django_admin_log` VALUES ('45', '2019-03-29 02:55:01', '1', '商家', '2', '[{\"changed\": {\"fields\": [\"permissions\"]}}]', '3', '1');
INSERT INTO `django_admin_log` VALUES ('46', '2019-03-29 02:56:39', '2', 'xiaoxiaocao', '2', '[{\"changed\": {\"fields\": [\"password\"]}}]', '4', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('4', 'auth', 'user');
INSERT INTO `django_content_type` VALUES ('5', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('12', 'goods', 'bigtype');
INSERT INTO `django_content_type` VALUES ('13', 'goods', 'detail');
INSERT INTO `django_content_type` VALUES ('10', 'goods', 'goodsinfo');
INSERT INTO `django_content_type` VALUES ('11', 'goods', 'goodstype');
INSERT INTO `django_content_type` VALUES ('8', 'seller', 'goodsinfo');
INSERT INTO `django_content_type` VALUES ('9', 'seller', 'goodstype');
INSERT INTO `django_content_type` VALUES ('18', 'seller', 'orders');
INSERT INTO `django_content_type` VALUES ('17', 'seller', 'order_info');
INSERT INTO `django_content_type` VALUES ('6', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('15', 'users', 'address');
INSERT INTO `django_content_type` VALUES ('14', 'users', 'car');
INSERT INTO `django_content_type` VALUES ('16', 'users', 'collection');
INSERT INTO `django_content_type` VALUES ('7', 'users', 'user');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('2', 'auth', '0001_initial', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('3', 'admin', '0001_initial', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('4', 'admin', '0002_logentry_remove_auto_add', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('5', 'contenttypes', '0002_remove_content_type_name', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0002_alter_permission_name_max_length', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0003_alter_user_email_max_length', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0004_alter_user_username_opts', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0005_alter_user_last_login_null', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0006_require_contenttypes_0002', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0007_alter_validators_add_error_messages', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('12', 'auth', '0008_alter_user_username_max_length', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('13', 'auth', '0009_alter_user_last_name_max_length', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('14', 'seller', '0001_initial', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('15', 'seller', '0002_auto_20190127_2013', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('16', 'sessions', '0001_initial', '2019-03-07 10:11:39');
INSERT INTO `django_migrations` VALUES ('17', 'users', '0001_initial', '2019-03-07 10:11:40');
INSERT INTO `django_migrations` VALUES ('18', 'users', '0002_auto_20190313_1730', '2019-03-13 09:30:15');
INSERT INTO `django_migrations` VALUES ('19', 'users', '0003_auto_20190320_1556', '2019-03-20 07:56:22');
INSERT INTO `django_migrations` VALUES ('20', 'goods', '0001_initial', '2019-03-21 06:07:40');
INSERT INTO `django_migrations` VALUES ('21', 'seller', '0003_auto_20190321_1407', '2019-03-21 06:07:40');
INSERT INTO `django_migrations` VALUES ('22', 'goods', '0002_auto_20190321_1425', '2019-03-21 06:26:06');
INSERT INTO `django_migrations` VALUES ('23', 'goods', '0003_auto_20190321_1844', '2019-03-21 10:44:47');
INSERT INTO `django_migrations` VALUES ('24', 'goods', '0004_auto_20190321_1939', '2019-03-21 11:40:02');
INSERT INTO `django_migrations` VALUES ('25', 'users', '0004_car', '2019-03-22 02:53:23');
INSERT INTO `django_migrations` VALUES ('26', 'goods', '0005_detail_num', '2019-03-22 03:35:35');
INSERT INTO `django_migrations` VALUES ('27', 'users', '0005_auto_20190322_1526', '2019-03-22 07:26:08');
INSERT INTO `django_migrations` VALUES ('28', 'users', '0006_adress', '2019-03-22 07:57:31');
INSERT INTO `django_migrations` VALUES ('29', 'users', '0007_auto_20190326_1648', '2019-03-26 08:48:20');
INSERT INTO `django_migrations` VALUES ('30', 'users', '0008_collection', '2019-03-26 09:42:20');
INSERT INTO `django_migrations` VALUES ('33', 'seller', '0004_auto_20190327_1955', '2019-03-27 11:55:09');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('2m94vatym9siftpoujeq3n25mudzbsw6', 'MzYyZTcwYzM3ZDY1MjI5YzE1MTU5NDc2YTcwOTFlZjE3OTNiNWZiNjp7InVzZXIiOiJhZG1pbiIsImlkIjoxfQ==', '2019-03-27 10:34:08');
INSERT INTO `django_session` VALUES ('3zwqgjz80zqegildirhtdps4dk1kkzuf', 'MTlkZjc1OThjZDIwYmQ3OWU5YmNlZTZjOWM5NjNhYzE4NmM4N2NlNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiMzdiZWZjYWY2YmJkMmY5ZTk1ZGJlOTBlY2EyNDQ0YWI4Yjk5M2EwIn0=', '2019-04-10 02:36:10');
INSERT INTO `django_session` VALUES ('57iwfy00y9nf39kwl7sp2xz5dx3rl66i', 'MjYzNjBhYTViYzBlNmM3ZDY0NzQ5ODFlYjQ0NTA4Y2M1MjVjNWM0ZDp7InVzZXIiOiJcdTVjMGZcdTczOGIiLCJpZCI6Mn0=', '2019-04-10 07:09:03');
INSERT INTO `django_session` VALUES ('5pvw6ib5jik6w9w95akc2gcc58rncasf', 'MDc2Y2Y1ZTczNmIyNjFkNGMzNDg5ZDRkMjRmNTU3ODI1MjNhMzVmYzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZjdiMTJhMzhkYzc5YzY4OWExZDFlN2E5ZmUwNmZkNzAyNmZjNjUwIn0=', '2019-04-04 12:02:25');
INSERT INTO `django_session` VALUES ('7ei7x82y0ist7cc1hyfqb39t6y6bo0ju', 'MjYzNjBhYTViYzBlNmM3ZDY0NzQ5ODFlYjQ0NTA4Y2M1MjVjNWM0ZDp7InVzZXIiOiJcdTVjMGZcdTczOGIiLCJpZCI6Mn0=', '2019-04-05 06:09:38');
INSERT INTO `django_session` VALUES ('88ixxp8odtkbtvzweppla29pce0yc9qw', 'MjYzNjBhYTViYzBlNmM3ZDY0NzQ5ODFlYjQ0NTA4Y2M1MjVjNWM0ZDp7InVzZXIiOiJcdTVjMGZcdTczOGIiLCJpZCI6Mn0=', '2019-04-10 05:27:31');
INSERT INTO `django_session` VALUES ('ddsmtvur16lpq8ynvi9riauqu83b2oin', 'OGRiZmYwMTUyNzM3NGNiZDk3ZmIzYjc1ZDY5NDdiNTU1Zjg5MDA2MTqABJUcAAAAAAAAAH2UKIwCaWSUSwKMBHVzZXKUjAblsI/njouUdS4=', '2019-04-12 06:54:35');
INSERT INTO `django_session` VALUES ('fh1ydvz1ffg9hfpy8kcppuwbwawiuihm', 'MDc2Y2Y1ZTczNmIyNjFkNGMzNDg5ZDRkMjRmNTU3ODI1MjNhMzVmYzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZjdiMTJhMzhkYzc5YzY4OWExZDFlN2E5ZmUwNmZkNzAyNmZjNjUwIn0=', '2019-04-04 11:29:01');
INSERT INTO `django_session` VALUES ('hqgku7s2vds55v8uj284ewgy01olqf4p', 'NGEzYmViZGI0NDE4ODY1Y2I2ZDkyOGY3ZGFjYWExYjYyZWIxNTk2Nzp7InVzZXIiOiJcdTVjMGZcdTczOGIiLCJpZCI6MiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImIzN2JlZmNhZjZiYmQyZjllOTVkYmU5MGVjYTI0NDRhYjhiOTkzYTAifQ==', '2019-04-09 10:40:24');
INSERT INTO `django_session` VALUES ('ir59ol3q7d29gz2348ryh4gffofg9n4j', 'MjYzNjBhYTViYzBlNmM3ZDY0NzQ5ODFlYjQ0NTA4Y2M1MjVjNWM0ZDp7InVzZXIiOiJcdTVjMGZcdTczOGIiLCJpZCI6Mn0=', '2019-04-11 09:52:42');
INSERT INTO `django_session` VALUES ('iwncmgi9h0pd616tfpsnrrhfs4wk4uhh', 'MjYzNjBhYTViYzBlNmM3ZDY0NzQ5ODFlYjQ0NTA4Y2M1MjVjNWM0ZDp7InVzZXIiOiJcdTVjMGZcdTczOGIiLCJpZCI6Mn0=', '2019-04-05 05:43:03');
INSERT INTO `django_session` VALUES ('jxeuho1rvlbfvagxo2kyz0c5uy34iyge', 'OTdmOWE3MmE2MmQwM2MyMmU0NWI0OTMxYjQxYWE4OTM3NGM0OTYxZjp7ImlkIjoyLCJ1c2VyIjoiXHU1YzBmXHU3MzhiIn0=', '2019-04-05 01:51:13');
INSERT INTO `django_session` VALUES ('n5fqo59de7rtvtzds3l0ikqqc8kxntmk', 'MjYzNjBhYTViYzBlNmM3ZDY0NzQ5ODFlYjQ0NTA4Y2M1MjVjNWM0ZDp7InVzZXIiOiJcdTVjMGZcdTczOGIiLCJpZCI6Mn0=', '2019-04-05 06:25:25');
INSERT INTO `django_session` VALUES ('oeu17ukbv63g05vfjfpnsqc3hrmbzdpl', 'ZDJmODhlNDkyYjVhY2E4MmRhMDJmMTY3YjlmMWFjZWYwMWQxMDFmNDqABJWXAAAAAAAAAH2UKIwNX2F1dGhfdXNlcl9pZJSMATKUjBJfYXV0aF91c2VyX2JhY2tlbmSUjClkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZJSMD19hdXRoX3VzZXJfaGFzaJSMKGM0MzY2NTc4ODk1ZGM1ZmI4ODgxMGRmYTQ0MGU5NWI2NjMzZjJkMjGUdS4=', '2019-04-12 02:57:11');
INSERT INTO `django_session` VALUES ('p9gz2zgb54sz5sw24crxr3sazo1ztbzk', 'MjYzNjBhYTViYzBlNmM3ZDY0NzQ5ODFlYjQ0NTA4Y2M1MjVjNWM0ZDp7InVzZXIiOiJcdTVjMGZcdTczOGIiLCJpZCI6Mn0=', '2019-04-09 08:48:39');
INSERT INTO `django_session` VALUES ('r8db7evcsn5rsbsunth7aafsmnlhlbg1', 'MjYzNjBhYTViYzBlNmM3ZDY0NzQ5ODFlYjQ0NTA4Y2M1MjVjNWM0ZDp7InVzZXIiOiJcdTVjMGZcdTczOGIiLCJpZCI6Mn0=', '2019-04-10 08:47:10');
INSERT INTO `django_session` VALUES ('swkebpx4hipqxj6roitvlu5lurlq78j4', 'MjYzNjBhYTViYzBlNmM3ZDY0NzQ5ODFlYjQ0NTA4Y2M1MjVjNWM0ZDp7InVzZXIiOiJcdTVjMGZcdTczOGIiLCJpZCI6Mn0=', '2019-04-11 10:54:40');
INSERT INTO `django_session` VALUES ('v01aeo8fl7yfymu5sbpg8hrrwa3lo42x', 'MTlkZjc1OThjZDIwYmQ3OWU5YmNlZTZjOWM5NjNhYzE4NmM4N2NlNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJiMzdiZWZjYWY2YmJkMmY5ZTk1ZGJlOTBlY2EyNDQ0YWI4Yjk5M2EwIn0=', '2019-04-04 06:11:38');
INSERT INTO `django_session` VALUES ('ydroe2mdgzvfxe49apsy10kgfa9omc6d', 'MDc2Y2Y1ZTczNmIyNjFkNGMzNDg5ZDRkMjRmNTU3ODI1MjNhMzVmYzp7Il9hdXRoX3VzZXJfaWQiOiIyIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhZjdiMTJhMzhkYzc5YzY4OWExZDFlN2E5ZmUwNmZkNzAyNmZjNjUwIn0=', '2019-04-04 10:58:53');
INSERT INTO `django_session` VALUES ('zkmo7dsklkrpj09utt6cqd4c0yuigry3', 'MjYzNjBhYTViYzBlNmM3ZDY0NzQ5ODFlYjQ0NTA4Y2M1MjVjNWM0ZDp7InVzZXIiOiJcdTVjMGZcdTczOGIiLCJpZCI6Mn0=', '2019-04-05 05:43:02');
INSERT INTO `django_session` VALUES ('zs0btit77y0w5kjkb760rtkxa3l0qye3', 'NzNlNTAzODU1NDBjZTgwOWMyNTE5MTQzYWM0NTc5NmUxZDU1NzMzNDqABJUcAAAAAAAAAH2UKIwEdXNlcpSMBuWwj+eOi5SMAmlklEsCdS4=', '2019-04-11 12:02:22');

-- ----------------------------
-- Table structure for goods_bigtype
-- ----------------------------
DROP TABLE IF EXISTS `goods_bigtype`;
CREATE TABLE `goods_bigtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `create_time` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_bigtype
-- ----------------------------
INSERT INTO `goods_bigtype` VALUES ('1', '个护美妆', '2019-03-21');
INSERT INTO `goods_bigtype` VALUES ('2', '服装', '2019-03-21');
INSERT INTO `goods_bigtype` VALUES ('3', '电子产品', '2019-03-21');
INSERT INTO `goods_bigtype` VALUES ('4', '鞋子', '2019-03-21');
INSERT INTO `goods_bigtype` VALUES ('5', '零食', '2019-03-21');
INSERT INTO `goods_bigtype` VALUES ('6', '生活用品', '2019-03-21');
INSERT INTO `goods_bigtype` VALUES ('7', '背包', '2019-03-21');

-- ----------------------------
-- Table structure for goods_detail
-- ----------------------------
DROP TABLE IF EXISTS `goods_detail`;
CREATE TABLE `goods_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `size` varchar(500) NOT NULL,
  `color` varchar(500) NOT NULL,
  `goods_oprice` double NOT NULL,
  `goods_xprice` double NOT NULL,
  `goods_count` int(11) NOT NULL,
  `name_id` int(11) NOT NULL,
  `num` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_detail_name_id_9c9a7e04_fk_goods_goodsinfo_id` (`name_id`),
  CONSTRAINT `goods_detail_name_id_9c9a7e04_fk_goods_goodsinfo_id` FOREIGN KEY (`name_id`) REFERENCES `goods_goodsinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_detail
-- ----------------------------
INSERT INTO `goods_detail` VALUES ('1', '36码', '粉色', '398', '298', '42', '1', '3');
INSERT INTO `goods_detail` VALUES ('2', '36码', '蓝色', '398', '298', '60', '1', '3');
INSERT INTO `goods_detail` VALUES ('3', '36码', '黑色', '398', '298', '55', '1', '3');
INSERT INTO `goods_detail` VALUES ('4', '42码', '黑色', '500', '400', '96', '2', '3');
INSERT INTO `goods_detail` VALUES ('5', '43码', '黑色', '500', '400', '49', '2', '3');
INSERT INTO `goods_detail` VALUES ('6', '42码', '绿色', '500', '400', '93', '3', '3');
INSERT INTO `goods_detail` VALUES ('7', '43码', '绿色', '500', '400', '79', '3', '3');
INSERT INTO `goods_detail` VALUES ('8', '44码', '绿色', '500', '400', '19', '3', '3');

-- ----------------------------
-- Table structure for goods_goodsinfo
-- ----------------------------
DROP TABLE IF EXISTS `goods_goodsinfo`;
CREATE TABLE `goods_goodsinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_name` varchar(200) NOT NULL,
  `goods_method` varchar(100) NOT NULL,
  `goods_info` longtext NOT NULL,
  `goods_pic` varchar(100) NOT NULL,
  `goods_address` varchar(50) NOT NULL,
  `goods_content` longtext NOT NULL,
  `seller_id` int(11) NOT NULL,
  `type_id` int(11) DEFAULT NULL,
  `oprice` double NOT NULL,
  `xprice` double NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_goodsinfo_seller_id_7152dd0e_fk_auth_user_id` (`seller_id`),
  KEY `goods_goodsinfo_type_id_357bffcb_fk_goods_goodstype_id` (`type_id`),
  CONSTRAINT `goods_goodsinfo_seller_id_7152dd0e_fk_auth_user_id` FOREIGN KEY (`seller_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `goods_goodsinfo_type_id_357bffcb_fk_goods_goodstype_id` FOREIGN KEY (`type_id`) REFERENCES `goods_goodstype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_goodsinfo
-- ----------------------------
INSERT INTO `goods_goodsinfo` VALUES ('1', '乐途女士经典跑鞋', '不宜高温烫洗', '乐途女士经典跑鞋1+1时尚组', 'media/uploads/day_1.jpg', '北京', '这是一双适合运动的鞋，防滑防水，多种颜色可供挑选。', '2', '20', '400', '300');
INSERT INTO `goods_goodsinfo` VALUES ('2', '运动休闲鞋', '不宜高温烫洗', '本款鞋子质量轻，穿着非常舒适。', 'media/uploads/tui_1.jpg', '北京', '本款鞋子质量轻，穿着非常舒适。', '1', '17', '500', '400');
INSERT INTO `goods_goodsinfo` VALUES ('3', '跑步鞋', '不宜高温烫洗', '质量轻，适合跑步穿。', 'media/uploads/tui_4.jpg', '北京', '本款鞋子质量轻，穿着非常舒适。', '1', '17', '500', '400');

-- ----------------------------
-- Table structure for goods_goodstype
-- ----------------------------
DROP TABLE IF EXISTS `goods_goodstype`;
CREATE TABLE `goods_goodstype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(50) NOT NULL,
  `create_time` date NOT NULL,
  `type_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_goodstype_type_id_c99ab5ae_fk_goods_bigtype_id` (`type_id`),
  CONSTRAINT `goods_goodstype_type_id_c99ab5ae_fk_goods_bigtype_id` FOREIGN KEY (`type_id`) REFERENCES `goods_bigtype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of goods_goodstype
-- ----------------------------
INSERT INTO `goods_goodstype` VALUES ('1', '面部护肤', '2019-03-21', '1');
INSERT INTO `goods_goodstype` VALUES ('2', '洗发护发', '2019-03-21', '1');
INSERT INTO `goods_goodstype` VALUES ('3', '身体护理', '2019-03-21', '1');
INSERT INTO `goods_goodstype` VALUES ('4', '口腔护理', '2019-03-21', '1');
INSERT INTO `goods_goodstype` VALUES ('5', '女性个护', '2019-03-21', '1');
INSERT INTO `goods_goodstype` VALUES ('6', '香水彩妆', '2019-03-21', '1');
INSERT INTO `goods_goodstype` VALUES ('7', '电脑', '2019-03-21', '3');
INSERT INTO `goods_goodstype` VALUES ('8', '手机', '2019-03-21', '3');
INSERT INTO `goods_goodstype` VALUES ('9', '充电宝', '2019-03-21', '3');
INSERT INTO `goods_goodstype` VALUES ('10', '手环', '2019-03-21', '3');
INSERT INTO `goods_goodstype` VALUES ('11', '女士上衣', '2019-03-21', '2');
INSERT INTO `goods_goodstype` VALUES ('12', '男士上衣', '2019-03-21', '2');
INSERT INTO `goods_goodstype` VALUES ('13', '男士裤子', '2019-03-21', '2');
INSERT INTO `goods_goodstype` VALUES ('14', '女士裤子', '2019-03-21', '2');
INSERT INTO `goods_goodstype` VALUES ('15', '男士运动装', '2019-03-21', '2');
INSERT INTO `goods_goodstype` VALUES ('16', '女士运动装', '2019-03-21', '2');
INSERT INTO `goods_goodstype` VALUES ('17', '男士休闲鞋', '2019-03-21', '4');
INSERT INTO `goods_goodstype` VALUES ('18', '男士篮球鞋', '2019-03-21', '4');
INSERT INTO `goods_goodstype` VALUES ('19', '皮鞋', '2019-03-21', '4');
INSERT INTO `goods_goodstype` VALUES ('20', '女士运动鞋', '2019-03-21', '4');

-- ----------------------------
-- Table structure for seller_orders
-- ----------------------------
DROP TABLE IF EXISTS `seller_orders`;
CREATE TABLE `seller_orders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order` varchar(20) NOT NULL,
  `money` decimal(10,2) NOT NULL,
  `add_time` datetime NOT NULL,
  `address` varchar(150) NOT NULL,
  `contacts` varchar(30) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `pay_status` tinyint(1) NOT NULL,
  `pay_time` varchar(100) NOT NULL,
  `send_status` tinyint(1) NOT NULL,
  `send_time` varchar(100) NOT NULL,
  `receive_status` tinyint(1) NOT NULL,
  `receive_time` varchar(100) NOT NULL,
  `comment_status` tinyint(1) NOT NULL,
  `seller_id` int(11) NOT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `order` (`order`),
  KEY `seller_orders_seller_id_bdba4722_fk_auth_user_id` (`seller_id`),
  KEY `seller_orders_users_id_a25d3eac_fk_users_user_id` (`users_id`),
  CONSTRAINT `seller_orders_seller_id_bdba4722_fk_auth_user_id` FOREIGN KEY (`seller_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `seller_orders_users_id_a25d3eac_fk_users_user_id` FOREIGN KEY (`users_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of seller_orders
-- ----------------------------
INSERT INTO `seller_orders` VALUES ('13', '15537737181370926', '400.00', '2019-03-28 11:48:38', '河南省新乡市红旗区华兰大道东段河南科技学院', '小王', '18737307883', '0', '', '0', '', '0', '', '0', '1', '2');
INSERT INTO `seller_orders` VALUES ('14', '15537739134436333', '400.00', '2019-03-28 11:51:53', '河南省新乡市红旗区华兰大道东段河南科技学院', '张三', '18737307883', '0', '', '0', '', '0', '', '0', '1', '2');
INSERT INTO `seller_orders` VALUES ('15', '15537740673296316', '298.00', '2019-03-28 11:54:27', '河南省新乡市红旗区华兰大道东段河南科技学院', '小王', '18737307883', '0', '', '0', '', '0', '', '0', '2', '2');
INSERT INTO `seller_orders` VALUES ('16', '15537741293141742', '298.00', '2019-03-28 11:55:29', '河南省新乡市红旗区华兰大道东段河南科技学院', '小王', '18737307883', '0', '', '0', '', '0', '', '0', '2', '2');
INSERT INTO `seller_orders` VALUES ('17', '15537742609340806', '400.00', '2019-03-28 11:57:40', '河南省新乡市红旗区华兰大道东段河南科技学院', '小王', '18737307883', '0', '', '0', '', '0', '', '0', '1', '2');
INSERT INTO `seller_orders` VALUES ('18', '15537748993076546', '298.00', '2019-03-28 12:08:19', '河南省新乡市红旗区华兰大道东段河南科技学院', '小王', '18737307883', '0', '', '0', '', '0', '', '0', '2', '2');
INSERT INTO `seller_orders` VALUES ('19', '15537750713356388', '298.00', '2019-03-28 12:11:11', '河南省新乡市红旗区华兰大道东段河南科技学院', '小王', '18737307883', '0', '', '0', '', '0', '', '0', '2', '2');
INSERT INTO `seller_orders` VALUES ('20', '1553775121610677', '400.00', '2019-03-28 12:12:01', '河南省新乡市红旗区华兰大道东段河南科技学院', '小王', '18737307883', '1', '2019-03-28 20:16:28.677953', '1', '2019-03-29 10:35:56.483025', '1', '2019-03-29 14:12:48.238217', '0', '1', '2');

-- ----------------------------
-- Table structure for seller_order_info
-- ----------------------------
DROP TABLE IF EXISTS `seller_order_info`;
CREATE TABLE `seller_order_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `seller_order_info_goods_id_2ef31e7d_fk_goods_detail_id` (`goods_id`),
  KEY `seller_order_info_order_id_23717e00_fk_seller_orders_id` (`order_id`),
  CONSTRAINT `seller_order_info_goods_id_2ef31e7d_fk_goods_detail_id` FOREIGN KEY (`goods_id`) REFERENCES `goods_detail` (`id`),
  CONSTRAINT `seller_order_info_order_id_23717e00_fk_seller_orders_id` FOREIGN KEY (`order_id`) REFERENCES `seller_orders` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of seller_order_info
-- ----------------------------
INSERT INTO `seller_order_info` VALUES ('13', '1', '400.00', '8', '13');
INSERT INTO `seller_order_info` VALUES ('14', '1', '400.00', '6', '14');
INSERT INTO `seller_order_info` VALUES ('15', '1', '298.00', '1', '15');
INSERT INTO `seller_order_info` VALUES ('16', '1', '298.00', '1', '16');
INSERT INTO `seller_order_info` VALUES ('17', '1', '400.00', '4', '17');
INSERT INTO `seller_order_info` VALUES ('18', '1', '298.00', '1', '18');
INSERT INTO `seller_order_info` VALUES ('19', '1', '298.00', '1', '19');
INSERT INTO `seller_order_info` VALUES ('20', '1', '400.00', '7', '20');

-- ----------------------------
-- Table structure for users_address
-- ----------------------------
DROP TABLE IF EXISTS `users_address`;
CREATE TABLE `users_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `address` varchar(500) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_adress_user_id_f59ac048_fk_users_user_id` (`user_id`),
  CONSTRAINT `users_adress_user_id_f59ac048_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_address
-- ----------------------------
INSERT INTO `users_address` VALUES ('4', '张三', '河南省新乡市红旗区华兰大道东段河南科技学院', '18737307883', '2');
INSERT INTO `users_address` VALUES ('5', '小王', '河南省新乡市红旗区华兰大道东段河南科技学院', '18737307883', '2');

-- ----------------------------
-- Table structure for users_car
-- ----------------------------
DROP TABLE IF EXISTS `users_car`;
CREATE TABLE `users_car` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `count` int(11) NOT NULL,
  `goods_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_car_goods_id_a2296ddd_fk_goods_detail_id` (`goods_id`),
  KEY `users_car_user_id_18fa6566_fk_users_user_id` (`user_id`),
  CONSTRAINT `users_car_goods_id_a2296ddd_fk_goods_detail_id` FOREIGN KEY (`goods_id`) REFERENCES `goods_detail` (`id`),
  CONSTRAINT `users_car_user_id_18fa6566_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_car
-- ----------------------------

-- ----------------------------
-- Table structure for users_collection
-- ----------------------------
DROP TABLE IF EXISTS `users_collection`;
CREATE TABLE `users_collection` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `goods_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `users_collection_goods_id_2f3636db_fk_goods_detail_id` (`goods_id`),
  KEY `users_collection_user_id_ae26e729_fk_users_user_id` (`user_id`),
  CONSTRAINT `users_collection_goods_id_2f3636db_fk_goods_detail_id` FOREIGN KEY (`goods_id`) REFERENCES `goods_detail` (`id`),
  CONSTRAINT `users_collection_user_id_ae26e729_fk_users_user_id` FOREIGN KEY (`user_id`) REFERENCES `users_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_collection
-- ----------------------------
INSERT INTO `users_collection` VALUES ('2', '1', '2');

-- ----------------------------
-- Table structure for users_user
-- ----------------------------
DROP TABLE IF EXISTS `users_user`;
CREATE TABLE `users_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(32) NOT NULL,
  `is_activate` tinyint(1) NOT NULL,
  `birthday` date DEFAULT NULL,
  `sex` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of users_user
-- ----------------------------
INSERT INTO `users_user` VALUES ('1', 'admin', '3b1a08b61f3e214af72acf0b71f7501b', '1', null, '1');
INSERT INTO `users_user` VALUES ('2', '小王', '96e79218965eb72c92a549dd5a330112', '1', '1996-04-30', '1');
