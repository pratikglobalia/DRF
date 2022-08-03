from django.shortcuts import render
from rest_framework.generics import ListAPIView 
from .models import Student
from .serializers import StudenySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

# Create your views here.
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby='user1')
    serializer_class = StudenySerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name','passby']
    
    # def get_queryset(self):
    # user = self.request.user
    # return Student.objects.filter(passby=user)
    
##############   search   ################    
    # filter_backends = [SearchFilter]
    # search_fields = ['name','city']
    
##############   ordering   ################  
    filter_backends = [OrderingFilter]
