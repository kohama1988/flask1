from flask import Flask,render_template,request
from flask_wtf.csrf import CSRFProtect

"""
创建CSRFProtector对象，保护app对象
设置SECRET_KEY，便于csrf_token加密
需要在表单中设置csrf_token

"""


app = Flask(__name__)
app.config['SECRET_KEY'] = 'lkjsdfwe'
CSRFProtect(app)

@app.route('/',methods=['GET','POST'])
def hello_world():
    if request.method == 'GET':
        return render_template('09_CSRFProtector.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if not all([username, password]):
            return '参数填写不全'
        return '注册成功'

if __name__ == '__main__':
    app.run(debug=True)