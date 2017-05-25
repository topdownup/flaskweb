/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50548
Source Host           : 192.168.50.237:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50548
File Encoding         : 65001

Date: 2017-05-25 17:29:13
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `user_type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '张三', 'zhangsan@hotmail.com', '1');
INSERT INTO `user` VALUES ('2', '李四', 'lisi@google.com', '1');
INSERT INTO `user` VALUES ('3', '王五', 'wangwu@sina.com', '2');
