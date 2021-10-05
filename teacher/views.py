from teacher import teacherBlue

@teacherBlue.route('/')
def index():
    return 'teacher index'

@teacherBlue.route('/new')
def new():
    return 'teacher new'