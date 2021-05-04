from rest_framework import serializers
from .models import *

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Song


class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Podcast


class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = AudioBook
