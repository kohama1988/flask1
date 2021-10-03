from flask import Flask, render_template, redirect, request, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:aisin-aw23@127.0.0.1:3306/data38'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 建立中间表
tb_student_course = db.Table(
    'tb_student_course', # 设置表名
    db.Column('student_id', db.Integer, db.ForeignKey('students.id')), # 新建student_id列，外键关联到students中的id
    db.Column('course_id', db.Integer, db.ForeignKey('courses.id')) # 新建course_id列，外键关联到courses中的id
)


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    # 关系属性, 多对多时需要设置secondary属性为关系表
    courses = db.relationship('Course', backref='students', secondary='tb_student_course')

    def __repr__(self):
        return 'Student name:{}'.format(self.name)


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))

    def __repr__(self):
        return 'Course name:{}'.format(self.name)

db.drop_all()
db.create_all()

@app.route('/')
def hello_world():
    return 'Hi, kohama!!'


if __name__ == '__main__':
    app.run(debug=True)
