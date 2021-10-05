from flask import Blueprint

teacherBlue = Blueprint('teacher', __name__, url_prefix='/teacher')

from teacher import views #如果不导入views，此蓝图的视图与app之间无法建立联系