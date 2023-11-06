# import viewsets
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse
 
# import local data
from .serializers import TeacherSerializer
from .models import TeacherModel
from .dto.teacher import Teacher
 
# create a viewset
@api_view(['GET'])
def teacher_list(request):
    teachers = TeacherModel.objects.all()
    data = list()
    for teacher in teachers:
        teacher_dto = Teacher(teacher.full_name, teacher.id)
        teacher_json = {
            'name': teacher_dto.name,
            'id': teacher_dto.id,
        }
        data.append(teacher_json)
    
    return JsonResponse(data, safe=False)