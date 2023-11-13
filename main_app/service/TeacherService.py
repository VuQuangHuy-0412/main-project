from main_app.models import TeacherModel
from main_app.dto.Teacher import Teacher

def get_all_teacher():
    teachers = TeacherModel.objects.all()
    data = list()
    for teacher in teachers:
        teacher_dto = Teacher(teacher.id, teacher.full_name, teacher.rank_and_degree, teacher.start_time, teacher.birthday, teacher.created_at, teacher.updated_at)
        teacher_json = {
            'id': teacher_dto.id,
            'full_name': teacher_dto.full_name,
            'rank_and_degree': teacher_dto.rank_and_degree,
            'start_time': teacher_dto.start_time,
            'birthday': teacher_dto.birthday,
            'created_at': teacher_dto.created_at,
            'updated_at': teacher_dto.updated_at,
        }
        data.append(teacher_json)
    
    return data