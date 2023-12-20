# import viewsets
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
import time
# import local data
from .service import TeacherService, GroupTeacherService, ReadData, GeneticAlgorithm, HDGeneticAlgorithm

from asgiref.sync import sync_to_async
import asyncio
from django.http import HttpResponse
 
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
    data = ReadData.read_data()
    return JsonResponse(data, safe=False)

@sync_to_async
def genetic_algorithm(request):
    data = GeneticAlgorithm.execute()
    return Response({'message': 'done'})

@sync_to_async
def genetic_algorithm_hd(request):
    data = HDGeneticAlgorithm.execute()
    return Response({'message': 'done'})

async def async_view(request):
    start_time = time.time()
    await asyncio.gather(genetic_algorithm(request), genetic_algorithm_hd(request))
    total = time.time()-start_time
    return HttpResponse(f"time taken async {total}")