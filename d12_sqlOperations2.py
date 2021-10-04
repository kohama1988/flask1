from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{}@127.0.0.1:3306/data37'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    users = db.relationship('User', backref='role', lazy='dynamic')
    """
    relationship方便数据库的关联查询
    用途: 知道了角色的情况下，快速查询出哪些用户扮演了该角色
    特点：不会再数据库中产生实体字段， 关系属性需要在一方添加，不是多方，本例中在Role中添加
    比如：查询role角色为1的所有用户
    Role.query.get(1).users 即可
    """
    """
    backref添加反向属性，快速查询
    用途: 知道用户的情况下，快速查询出哪些用户扮演了哪个角色
    User.query.get(1).role
    """
    """
    lazy属性 默认为subquery，如果不自动子查询，则设置为dynamic
    user = User.query.get(1)
    user.role 返回一个结果集，使用all()方法才返回一个结果列表
    
    """

    def __repr__(self):
        return '<roleName: {}>'.format(self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(20), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    def __repr__(self):
        return '<User: {}, {}, {}>'.format(self.id, self.name, self.email)

db.drop_all()
db.create_all()

# 创建测试数据
role1 = Role(name='admin')
role2 = Role(name='user')
db.session.add_all([role1, role2])
db.session.commit()

# 创建多条用户数据
u1 = User(name='wang', email='wang@126.com', password='123123', role_id=role1.id)
u2 = User(name='zhang', email='zhang@163.com', password='12452', role_id=role1.id)
u3 = User(name='chen', email='chen@126.com', password='346346', role_id=role2.id)
u4 = User(name='zhou', email='zhou@gmail.com', password='45647', role_id=role2.id)
u5 = User(name='tang', email='tang@126.com', password='348754', role_id=role1.id)
u6 = User(name='wu', email='wu@126.com', password='dfgert', role_id=role1.id)
u7 = User(name='qian', email='qian@nono.com', password='w45', role_id=role2.id)
u8 = User(name='liu', email='liu@126.com', password='dgj46u', role_id=role2.id)
u9 = User(name='sun', email='sun@haha.com', password='235dhfh', role_id=role1.id)
u10 = User(name='li', email='li@sina.com', password='rtyw356', role_id=role1.id)
db.session.add_all([u1,u2,u3,u4,u5,u6,u7,u8,u9,u10])
db.session.commit()

"""
查询数据
User.query 先使用查询过滤器，再使用查询执行器

查询过滤器
filter() 把过滤器添加到原查询上，返回一个新查询
filter_by() 把等值过滤器添加到原查询上，返回一个新查询
limit() 使用指定的值限定原查询返回的结果
offset() 偏移原查询返回的结果，返回一个新查询
order_by() 根据指定条件对原查询结果进行排序，返回一个新查询
group_by() 根据指定条件对原查询结果进行分组，返回一个新查询

查询执行器
all() 以列表形式返回查询的所有结果
first() 返回查询的第一个结果，如果未查到，返回None
first_or_404() 返回查询的第一个结果，如果未查到，返回404
get() 返回指定主键对应的行，如不存在，返回None
get_or_404()
count()
paginate()

"""

"""
查询所有用户数据
User.query.count()

查询有多少个用户
User.query.all()

查询第一个用户
User.query.first()

查询id为4的用户（3种方式）
User.query.get(4)
User.query.filter(User.id==4).first()
User.query.filter_by(id=4).first()

查询名字结尾字符为g的所有数据（开始/包含）
User.query.filter(User.name.endswith('g')).all() 结束
User.query.filter(User.name.startswith('g')).all() 开始
User.query.filter(User.name.contains('g')).all() 包含

查询名字不等于wang的所有数据
User.query.filter(User.name != 'wang').all()

查询名字和邮箱都以li开头的所有数据（2种方式）
User.query.filter(User.name.startswith('li'),User.email.startswith('li')).all()

查询password是123123或者email以gmail.com结尾的所有数据
from sqlalchemy import or_ # and_ not_都是其成员函数
User.query.filter(or_(User.password=='123123', User.email.endswith('gmail.com'))).all()

查询id为【1，3，5，7，9】的用户列表
User.query.filter(User.id.in_([1,3,5,7,9])).all()

查询name为liu的角色数据
Role.query.filter(Role.id ==  User.query.filter(User.name=='liu').first().role_id).first()

查询所有用户数据，并以邮箱排序
User.query.order_by(User.email).all()
User.query.order_by(User.email.desc()).all() # 降序

每页3个，查询第2页的数据
User.query.paginate(page, per_page, error_out)
 - page: 要查询的页数
 - per_page: 每页有多少条数据
 - error_out: 写成False，查不到不会报错
返回值为paginate
paginate.pages: 总页数
paginate.page: 当前页
paginate.items: 当前的对象列表

paginate = User.query.paginate(2,3,False)
paginate.items

"""


@app.route('/')
def hello_world():
    return 'Hi, kohama!!'

if __name__ == '__main__':
    app.run(debug=True)