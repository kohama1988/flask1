from flask import Flask,make_response,request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hi, kohama!!'

@app.route('/set_cookie')
def set_cookie():
    response = make_response("set response!")
    response.set_cookie('name','kohama',10)
    return response

@app.route('/get_cookie')
def get_cookie():
    name = request.cookies.get('name')
    return 'get cookie {}'.format(name)

if __name__ == '__main__':
    app.run()
