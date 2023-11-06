# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import TeacherModel
 
# Create a model serializer
class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = TeacherModel
        fields = ('id', 'full_name', 'rank_and_degree', 'start_time', 'birthday', 'created_at', 'updated_at')