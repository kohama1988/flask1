from flask import Flask,make_response,request

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    print('before first request..')

@app.before_request
def before_request():
    print('before request..')

@app.after_request
def after_request(arg):
    print('after request')
    return arg

@app.teardown_request
def teardown_request(arg):
    print('teardown request')
    return arg


@app.route('/')
def hello_world():
    return 'Hi, kohama!!'


if __name__ == '__main__':
    app.run(debug=True)
