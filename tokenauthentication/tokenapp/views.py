from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer
from tokenapp.customauth import CustomAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PersonApiView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]