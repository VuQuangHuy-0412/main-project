from main_app.models import TeacherModel
from main_app.dto.Teacher import Teacher

def get_all_teacher():
    teachers = TeacherModel.objects.all()
    data = list()
    for teacher in teachers:
        teacher_dto = Teacher(teacher.id, teacher.full_name, teacher.rank_and_degree, teacher.gd_time, teacher.hd_time, teacher.rating, teacher.start_time, teacher.birthday, teacher.created_at, teacher.updated_at)
        teacher_json = {
            'id': teacher_dto.id,
            'full_name': teacher_dto.full_name,
            'rank_and_degree': teacher_dto.rank_and_degree,
            'gd_time': teacher_dto.gd_time,
            'hd_time': teacher_dto.hd_time,
            'rating': teacher_dto.rating,
            'start_time': teacher_dto.start_time.strftime("%Y-%m-%d"),
            'birthday': teacher_dto.birthday.strftime("%Y-%m-%d"),
            'created_at': teacher_dto.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': teacher_dto.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        data.append(teacher_json)
    
    return data