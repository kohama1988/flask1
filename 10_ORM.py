from flask import Flask
from flask_sqlalchemy import SQLAlchemy

"""
ORM优点
- 对数据库的操作都转化成对类，属性和方法的操作
- 不用编写各种数据库的sql语句
- 不再关注使用的是mysql还是oracle等数据库
ORM缺点
- 相比较直接使用sql语句操作数据库有性能损失

pip install flask-mysqldb/pymysql 与MySQL的连接
设置数据库的配置信息
创建SQLAlchemy对象，关联app
编写模型类，继承自db.Model
操作数据库，增删改查

"""

app = Flask(__name__)

# 设置数据库的配置信息
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:aisin-aw23@127.0.0.1:3306/data36'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建SQLAlchemy对象，关联app
db = SQLAlchemy(app)

# 编写模型类，继承自db.Model
class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))

# 创建数据库的表, 创建的是继承自db.Model的表
db.create_all()

# 删除继承自db.Model的表
# db.drop_all()

@app.route('/')
def hello_world():
    return 'Hi, kohama!!'

if __name__ == '__main__':
    app.run(debug=True)