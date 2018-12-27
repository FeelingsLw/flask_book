import os
from datetime import timedelta

DEBUG = True

# 此处是配置SQLALCHEMY_DATABASE_URI, 前面的mysql+mysqlconnetor指的是数据库的类型以及驱动类型
# 后面的username,pwd,addr,port,dbname分别代表用户名、密码、地址、端口以及库名
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost:3306/book?charset=utf8'

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = os.urandom(24)  # 设置为24位的字符,每次运行服务器都是不同的，所以服务器启动一次上次的session就清除。
PERMANENT_SESSION_LIFETIME = timedelta(days=7)  # 设置session的保存时间。
