from main_app.models import GroupTeacherMappingModel
from main_app.dto.GroupTeacherMapping import GroupTeacherMapping

def get_all_group_teacher_mapping():
    gt_mappings = GroupTeacherMappingModel.objects.all()
    data = list()
    for item in gt_mappings:
        item_dto = GroupTeacherMapping(item.id, item.teacher_id, item.group_id, item.role)
        item_json = {
            'id': item_dto.id,
            'teacher_id': item_dto.teacher_id,
            'group_id': item_dto.group_id,
            'role': item_dto.role,
        }
        data.append(item_json)
    
    return data