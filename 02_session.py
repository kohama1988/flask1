from flask import Flask,make_response,request,session

app = Flask(__name__)

app.config['SECRET_KEY'] = 'alkdjqwerq'

@app.route('/')
def hello_world():
    return 'Hi, kohama!!'

@app.route('/set_session/<path:name>')
def set_session(name):
    session['name'] = name
    return 'set session finished!'

@app.route('/get_session')
def get_session():
    value = session['name']
    return 'session["name"] = {}'.format(value)

if __name__ == '__main__':
    app.run(debug=True)
