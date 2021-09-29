from flask import Flask,render_template

"""
1， 先定义好函数，再将函数添加到系统默认的过滤器列表
 - def定义函数
 - app.add_template_filter(函数名, '过滤器名字')
2. 定义函数时使用系统过滤器进行装饰
 @app.template_filter('过滤器名字')
 def 函数名

"""

app = Flask(__name__)

def get_oushu(li):
    return 'hello'
app.add_template_filter(get_oushu, 'oushu')

@app.template_filter('reverse')
def listReverse(li):
    li.reverse()
    return li

@app.route('/')
def hello_world():
    return render_template('06_customerFilter.html')

if __name__ == '__main__':
    app.run(debug=True)