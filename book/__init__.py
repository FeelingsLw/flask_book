from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config



db = SQLAlchemy()

app = Flask(__name__)
# 加载配置文件
app.config.from_object(config)
db.init_app(app)



# 引用视图文件
from book import views
