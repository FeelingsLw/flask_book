/*
 Navicat MySQL Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 80012
 Source Host           : localhost:3306
 Source Schema         : book

 Target Server Type    : MySQL
 Target Server Version : 80012
 File Encoding         : 65001

 Date: 13/12/2018 23:44:43
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for t_admin
-- ----------------------------
DROP TABLE IF EXISTS `t_admin`;
CREATE TABLE `t_admin` (
  `admin_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '管理员id号',
  `admin_name` varchar(10) NOT NULL COMMENT '管理员姓名',
  `admin_password` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '管理员密码',
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_book
-- ----------------------------
DROP TABLE IF EXISTS `t_book`;
CREATE TABLE `t_book` (
  `book_num` int(11) NOT NULL AUTO_INCREMENT COMMENT '图书编号',
  `book_name` varchar(20) NOT NULL COMMENT '书名',
  `writer` varchar(10) NOT NULL COMMENT '作者',
  `sort_id` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '类加id',
  `price` decimal(5,0) DEFAULT NULL COMMENT '单价',
  `pub_company` varchar(20) DEFAULT NULL COMMENT '出版社',
  `pub_date` date DEFAULT NULL COMMENT '出版日期',
  `total_num` int(3) NOT NULL COMMENT '总数量',
  `current_num` int(3) NOT NULL COMMENT '当前数量',
  `buy_date` date NOT NULL COMMENT '入库日期',
  `brief` varchar(100) DEFAULT NULL COMMENT '内容摘要',
  PRIMARY KEY (`book_num`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_book
-- ----------------------------
BEGIN;
INSERT INTO `t_book` VALUES (1, 'Python', 'zs', '1', 1, '图灵', '2018-01-01', 2, 2, '2018-01-01', '100');
COMMIT;

-- ----------------------------
-- Table structure for t_book_student
-- ----------------------------
DROP TABLE IF EXISTS `t_book_student`;
CREATE TABLE `t_book_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'id号',
  `book_id` varchar(20) NOT NULL COMMENT '图书编号',
  `student_id` varchar(15) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '学号',
  `borrow_date` date NOT NULL COMMENT '借书日期',
  `return_date` date NOT NULL COMMENT '还书日期',
  `money` int(5) NOT NULL COMMENT '超期罚款',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_class
-- ----------------------------
DROP TABLE IF EXISTS `t_class`;
CREATE TABLE `t_class` (
  `class_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '学院id号',
  `class_name` varchar(30) NOT NULL COMMENT '学院姓名',
  `college_id` int(11) NOT NULL COMMENT '所属学院id',
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_college
-- ----------------------------
DROP TABLE IF EXISTS `t_college`;
CREATE TABLE `t_college` (
  `college_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '学院id号',
  `college_name` varchar(30) NOT NULL COMMENT '学院姓名',
  PRIMARY KEY (`college_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_sort
-- ----------------------------
DROP TABLE IF EXISTS `t_sort`;
CREATE TABLE `t_sort` (
  `sort_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '类别id',
  `sort_name` varchar(30) NOT NULL COMMENT '类别名',
  PRIMARY KEY (`sort_id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_sort
-- ----------------------------
BEGIN;
INSERT INTO `t_sort` VALUES (1, '计算机理论硬件');
INSERT INTO `t_sort` VALUES (2, '外部设备');
INSERT INTO `t_sort` VALUES (3, '维修操作系统/系统开发');
INSERT INTO `t_sort` VALUES (4, '数据库');
INSERT INTO `t_sort` VALUES (5, '程序设计');
INSERT INTO `t_sort` VALUES (6, '网络与数据通信');
INSERT INTO `t_sort` VALUES (7, '图形图像 多媒体');
INSERT INTO `t_sort` VALUES (8, 'CAD CAM CAE');
INSERT INTO `t_sort` VALUES (9, '软件工程/开发项目管理');
INSERT INTO `t_sort` VALUES (10, '行业软件及应用');
INSERT INTO `t_sort` VALUES (11, '人工智能');
INSERT INTO `t_sort` VALUES (12, '家庭与办公室用书');
INSERT INTO `t_sort` VALUES (13, '计算机考试');
INSERT INTO `t_sort` VALUES (14, '认证管理信息系统(MIS)');
INSERT INTO `t_sort` VALUES (15, '地理信息管理系统（GIS)');
INSERT INTO `t_sort` VALUES (16, '企业软件开发与实施');
INSERT INTO `t_sort` VALUES (17, '信息安全');
INSERT INTO `t_sort` VALUES (18, '项目管理IT人文');
INSERT INTO `t_sort` VALUES (19, '电脑杂志——合订本');
INSERT INTO `t_sort` VALUES (20, '计算机体系结构');
INSERT INTO `t_sort` VALUES (21, '数码全攻略');
INSERT INTO `t_sort` VALUES (22, '影印版');
INSERT INTO `t_sort` VALUES (23, '计算机教材');
INSERT INTO `t_sort` VALUES (24, '英文原版书-计算机');
COMMIT;

-- ----------------------------
-- Table structure for t_student
-- ----------------------------
DROP TABLE IF EXISTS `t_student`;
CREATE TABLE `t_student` (
  `student_num` int(11) NOT NULL AUTO_INCREMENT COMMENT '学号',
  `student_name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '姓名',
  `password` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '密码',
  `college_id` int(10) NOT NULL COMMENT '学院id',
  `class_id` int(10) NOT NULL COMMENT '班级id',
  `sex` varchar(2) DEFAULT NULL COMMENT '性别',
  `telephone` varchar(15) DEFAULT NULL COMMENT '电话',
  `email` varchar(20) DEFAULT NULL COMMENT 'email',
  `lended_num` int(11) NOT NULL COMMENT '已借书数量',
  `create_date` date NOT NULL COMMENT '创建日期',
  PRIMARY KEY (`student_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
