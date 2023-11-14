from main_app.models import ClassModel
from main_app.dto.Class import Class

def get_all_class():
    classes = ClassModel.objects.all()
    data = list()
    for item in classes:
        class_dto = Class(item.id, item.name, item.code, item.semester, item.subject_id, item.week, item.day_of_week, item.time_of_day, item.is_assigned, item.teacher_id, item.created_at, item.updated_at)
        class_json = {
            'id': class_dto.id,
            'name': class_dto.name,
            'code': class_dto.code,
            'semester': class_dto.semester,
            'subject_id': class_dto.subject_id,
            'week': class_dto.week,
            'day_of_week': class_dto.day_of_week,
            'time_of_day': class_dto.time_of_day,
            'is_assigned': class_dto.is_assigned,
            'teacher_id': class_dto.teacher_id,
            'created_at': class_dto.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': class_dto.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        data.append(class_json)
    
    return data