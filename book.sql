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

 Date: 13/12/2018 00:05:27
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for t_student
-- ----------------------------
DROP TABLE IF EXISTS `t_student`;
CREATE TABLE `t_student` (
  `student_num` int(11) NOT NULL AUTO_INCREMENT COMMENT '学号',
  `student_name` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '姓名',
  `password` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT '密码',
  `academy_id` int(10) NOT NULL COMMENT '学院id',
  `class_id` int(10) NOT NULL COMMENT '班级id',
  `sex` varchar(2) DEFAULT NULL COMMENT '性别',
  `telephone` varchar(15) DEFAULT NULL COMMENT '电话',
  `email` varchar(20) DEFAULT NULL COMMENT 'email',
  `lended_num` int(11) NOT NULL COMMENT '已借书数量',
  `create_date` date NOT NULL COMMENT '创建日期',
  PRIMARY KEY (`student_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

SET FOREIGN_KEY_CHECKS = 1;
