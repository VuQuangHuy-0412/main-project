from main_app.models import SubjectModel
from main_app.dto.Subject import Subject

def get_all_subject():
    subjects = SubjectModel.objects.all()
    data = list()
    for item in subjects:
        item_dto = Subject(item.id, item.name, item.code, item.group_id, item.created_at, item.updated_at)
        item_json = {
            'id': item_dto.id,
            'name': item_dto.name,
            'code': item_dto.code,
            'group_id': item_dto.group_id,
            'created_at': item_dto.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': item_dto.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        data.append(item_json)
    
    return data