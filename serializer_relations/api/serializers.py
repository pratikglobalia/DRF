from rest_framework import serializers
from .models import Song, Singer


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'singer', 'duration']
        
        
class SingerSerializer(serializers.ModelSerializer):
    # song = serializers.StringRelatedField(many=True)
    song = SongSerializer(many = True, read_only = True)                   #######  nested serializer  #######
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']
