from flask import Flask
from teacher import teacherBlue

app = Flask(__name__)
app.register_blueprint(teacherBlue)

@app.route('/')
def hello_world():
    return 'Hi, kohama!!'

if __name__ == '__main__':
    app.run(debug=True)