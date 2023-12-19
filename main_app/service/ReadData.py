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

    data['num_of_teachers'] = len(data['teachers'])
    data['num_of_languages'] = len(data['languages'])
    data['num_of_groups'] = len(data['group_teachers'])
    data['num_of_classes'] = len(data['classes'])
    data['num_of_subjects'] = len(data['subjects'])

    data['class_conflict'] = list()
    for i in range(0, data['num_of_classes']):
        conflict = list()
        for j in range(0, data['num_of_classes']):
            conf = 0
            if i != j:
                dayOfWeek1 = generateListFromString(data['classes'][i]['day_of_week'])
                dayOfWeek2 = generateListFromString(data['classes'][j]['day_of_week'])
                if arrayIsConflict(dayOfWeek1, dayOfWeek2) == 1:
                    timeOfDay1 = generateListFromString(data['classes'][i]['time_of_day'])
                    timeOfDay2 = generateListFromString(data['classes'][j]['time_of_day'])
                    if arrayIsConflict(timeOfDay1, timeOfDay2) == 1:
                        conf = 1
            conflict.append(conf)
        data['class_conflict'].append(conflict)

    return data

def generateListFromString(s: str):
    return s.split(",")

def arrayIsConflict(list1: list, list2: list):
    for i in range(0, len(list1)):
        for j in range(0, len(list2)):
            if list1[i] == list2[j]:
                return 1
    return 0