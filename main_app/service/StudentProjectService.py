from main_app.models import StudentProjectModel
from main_app.dto.StudentProject import StudentProject

def get_all_student():
    students = StudentProjectModel.objects.all()
    data = list()
    for item in students:
        item_dto = StudentProject(item.id, item.name, item.student_code, item.class_id, item.is_assigned, item.created_at, item.updated_at, item.teacher_1_id, item.teacher_2_id, item.teacher_3_id, item.teacher_assigned_id)
        item_json = {
            'id': item_dto.id,
            'name': item_dto.name,
            'student_code': item_dto.student_code,
            'class_id': item_dto.class_id,
            'is_assigned': item_dto.is_assigned,
            'created_at': item_dto.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': item_dto.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            'teacher_1_id': item_dto.teacher_1_id,
            'teacher_2_id': item_dto.teacher_2_id,
            'teacher_3_id': item_dto.teacher_3_id,
            'teacher_assigned_id': item_dto.teacher_assigned_id
        }
        data.append(item_json)
    
    return data