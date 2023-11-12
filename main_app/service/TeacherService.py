from main_app.models import TeacherModel
from main_app.dto.teacher import Teacher

def get_all_teacher():
    teachers = TeacherModel.objects.all()
    data = list()
    for teacher in teachers:
        teacher_dto = Teacher(teacher.full_name, teacher.id)
        teacher_json = {
            'name': teacher_dto.name,
            'id': teacher_dto.id,
        }
        data.append(teacher_json)
    
    return data