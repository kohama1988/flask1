from flask import Flask,Blueprint

app = Flask(__name__)

bluePrint = Blueprint('myBluePrint',__name__)

@bluePrint.route('/')
def hello_world():
    return 'Hi, kohama!!'

@bluePrint.route('/test1')
def test1():
    return 'TEST 1'

@bluePrint.route('/test2')
def test2():
    return 'TEST 2'

app.register_blueprint(bluePrint)

if __name__ == '__main__':
    app.run(debug=True)