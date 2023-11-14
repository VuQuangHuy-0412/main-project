from main_app.models import LanguageModel
from main_app.dto.Language import Language

def get_all_language():
    languages = LanguageModel.objects.all()
    data = list()
    for item in languages:
        item_dto = Language(item.id, item.name, item.created_at, item.updated_at)
        item_json = {
            'id': item_dto.id,
            'name': item_dto.name,
            'created_at': item_dto.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            'updated_at': item_dto.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        data.append(item_json)
    
    return data