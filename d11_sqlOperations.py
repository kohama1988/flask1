from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{}@127.0.0.1:3306/data36'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __repr__(self):
        return '<roleName: {}>'.format(self.name)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    role_id = db.Column(db.ForeignKey(Role.id))

    def __repr__(self):
        return '<userName: {}>'.format(self.name)

db.drop_all()
db.create_all()

"""
以下代码在ipython中执行
In [6]: role1 = Role(name='admin')
In [7]: db.session.add(role1)
In [8]: db.session.commit()

In [10]: role2 = Role(name='user')
In [11]: db.session.add(role2)
In [12]: db.session.commit()

In [13]: user1 = User(name='kohama', role_id=1)
In [14]: user2 = User(name='hisae', role_id=2)
In [15]: db.session.add_all([user1,user2])
In [16]: db.session.commit()

"""

@app.route('/')
def hello_world():
    return 'Hi, kohama!!'

if __name__ == '__main__':
    app.run(debug=True)