from main_app.models import LanguageTeacherMappingModel
from main_app.dto.LanguageTeacherMapping import LanguageTeacherMapping

def get_all_language_teacher_mapping():
    lt_mappings = LanguageTeacherMappingModel.objects.all()
    data = list()
    for item in lt_mappings:
        item_dto = LanguageTeacherMapping(item.id, item.teacher_id, item.language_id)
        item_json = {
            'id': item_dto.id,
            'teacher_id': item_dto.teacher_id,
            'group_id': item_dto.language_id,
        }
        data.append(item_json)
    
    return data