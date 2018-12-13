DEBUG=True

# 此处是配置SQLALCHEMY_DATABASE_URI, 前面的mysql+mysqlconnetor指的是数据库的类型以及驱动类型
# 后面的username,pwd,addr,port,dbname分别代表用户名、密码、地址、端口以及库名
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost:3306/book?charset=utf8'

SQLALCHEMY_TRACK_MODIFICATIONS = True