# basic URL Configurations
from django.urls import include, path
# import routers
from rest_framework import routers
from main_app import views
from rest_framework.urlpatterns import format_suffix_patterns
 
# import everything from views
from .views import *
 
# specify URL Path for rest_framework
urlpatterns = [
    path('teachers/', views.all_teacher),
    path('group-teachers/', views.all_group_teacher),
    path('data/', views.all_data),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)