from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate
# 最新版本中不存在MigrateCommand，使用
# flask db init
# flask db migrate -m 'comment'
# flask db upgrade
# flask db downgrade -> 数据容易丢失，一般不使用
# 使用flask命令时需要将FLASK_APP指定到对象文件中  export FLASK_APP=d15_sqlMigrate.py

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lajdqer'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{}@localhost:3306/migrate36'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
manager = Manager(app)
Migrate(app, db)

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.Integer)

    def __repr__(self):
        return 'Student: name->{}, age->{}'.format(self.name, self.age)

# db.drop_all()
# db.create_all()
#
# stu1 = Student(name='kohama')
# stu2 = Student(name='hisae')
# db.session.add_all([stu1, stu2])
# db.session.commit()

@app.route('/')
def hello_world():
    return 'Hi, kohama!!'

if __name__ == '__main__':
    app.run()