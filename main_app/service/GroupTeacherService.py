from main_app.models import GroupTeacherModel
from main_app.dto.GroupTeacher import GroupTeacher

def get_all_group_teacher():
    group_teachers = GroupTeacherModel.objects.all()
    data = list()
    for group_teacher in group_teachers:
        group_teacher_dto = GroupTeacher(group_teacher.id, group_teacher.name, group_teacher.description, group_teacher.leader, group_teacher.created_at, group_teacher.updated_at)
        group_teacher_json = {
            'id': group_teacher_dto.id,
            'name': group_teacher_dto.name,
            'description': group_teacher_dto.description,
            'leader': group_teacher_dto.leader,
            'created_at': group_teacher_dto.created_at,
            'updated_at': group_teacher_dto.updated_at,
        }
        data.append(group_teacher_json)
    
    return data