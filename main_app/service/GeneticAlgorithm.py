from main_app.service import TeacherService, GroupTeacherService
from main_app.dto.Data import Data

def genetic_algorithm():
    teachers = TeacherService.get_all_teacher()
    group_teachers = GroupTeacherService.get_all_group_teacher()

    data = Data(teachers, group_teachers)
    data_json = {
        'teachers': data.teachers,
        'group_teachers': data.group_teachers
    }
    return data_json

