from main_app.service import TeacherService, GroupTeacherService, ClassService, GroupTeacherMappingService, LanguageService, LanguageTeacherMappingService, StudentProjectService, SubjectService
import json

def read_data():
    data = dict()
    data['teachers'] = TeacherService.get_all_teacher()
    data['group_teachers'] = GroupTeacherService.get_all_group_teacher()
    data['classes'] = ClassService.get_all_class()
    data['gt_mappings'] = GroupTeacherMappingService.get_all_group_teacher_mapping()
    data['languages'] = LanguageService.get_all_language()
    data['lt_mappings'] = LanguageTeacherMappingService.get_all_language_teacher_mapping()
    data['students'] = StudentProjectService.get_all_student()
    data['subjects'] = SubjectService.get_all_subject()

    return data
    