# import viewsets
from rest_framework import viewsets
 
# import local data
from .serializers import TeacherSerializer
from .models import TeacherModel
 
# create a viewset
 
 
class TeacherViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = TeacherModel.objects.all()
 
    # specify serializer to be used
    serializer_class = TeacherSerializer