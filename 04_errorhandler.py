from flask import Flask,abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    abort(404)
    return 'Hi, kohama!!'

@app.errorhandler(404) # <-传入从abort中传入的错误代码
def errorhandler(f):
    print(f)
    return f

if __name__ == '__main__':
    app.run(debug=True)