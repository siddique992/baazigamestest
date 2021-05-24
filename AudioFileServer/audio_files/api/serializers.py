from rest_framework import serializers
from audio_files.models import *


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'  #('file', 'duration', 'upload_time')


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = '__all__'  #('file', 'duration', 'upload_time', 'host', 'participants')


class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = '__all__'  #('file', 'title', 'author', 'narrator', 'duration', 'upload_time')
