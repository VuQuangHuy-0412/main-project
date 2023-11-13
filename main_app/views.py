# import viewsets
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse
 
# import local data
from .service import TeacherService, GroupTeacherService, GeneticAlgorithm
 
# create a viewset
@api_view(['GET'])
def all_teacher(request):
    data = TeacherService.get_all_teacher()
    
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def all_group_teacher(request):
    data = GroupTeacherService.get_all_group_teacher()
    
    return JsonResponse(data, safe=False)

@api_view(['GET'])
def all_data(request):
    data = GeneticAlgorithm.genetic_algorithm()
    
    return JsonResponse(data, safe=False)