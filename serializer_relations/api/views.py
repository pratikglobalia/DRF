from django.shortcuts import render
from .models import Song, Singer
from .serializers import SingerSerializer, SongSerializer
from rest_framework import viewsets

# Create your views here.
class SingerApiView(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer

class SongApiView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer