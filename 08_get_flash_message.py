from flask import Flask,render_template,flash

app = Flask(__name__)
# 使用flash存储消息时要设置SECRET_KEY，因为设置与session有关
app.config['SECRET_KEY'] = 'slkjrqwe'

@app.route('/')
def hello_world():
    flash('登录成功')
    flash('登录成功')
    flash('登录成功')
    return render_template('08_get_flash_message.html')

if __name__ == '__main__':
    app.run(debug=True)