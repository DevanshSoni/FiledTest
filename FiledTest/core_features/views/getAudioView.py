from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from core_features.models import Song, Podcast, AudioBook
from ..serializers import *

class allAudioList(generics.ListAPIView):
    lookup_url_kwarg_type = 'audioFileType'
    audioFileType = ''

    def get_queryset(self):
        self.audioFileType = self.kwargs.get(self.lookup_url_kwarg_type)
        if 'song' in self.audioFileType.lower():
            queryset = Song.objects.all()
            return queryset
        elif 'podcast' in self.audioFileType.lower():
            queryset = Podcast.objects.all()
            return queryset
        elif 'audiobook' in self.audioFileType.lower():
            queryset = AudioBook.objects.all()
            return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        if 'song' in self.audioFileType.lower():
            serializer = SongSerializer(queryset, many=True)
        elif 'podcast' in self.audioFileType.lower():
            serializer = PodcastSerializer(queryset, many=True)
        elif 'audiobook' in self.audioFileType.lower():
            serializer = AudioBookSerializer(queryset, many=True)
        else:
            return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"data": serializer.data, "message": "Success", "status": True}, status=status.HTTP_200_OK)
    
class audioList(generics.ListAPIView):
    lookup_url_kwarg_type = 'audioFileType'
    lookup_url_kwarg_id = 'audioFileID'
    audioFileType = ''
    audioFileId = ''

    def get_queryset(self):
        self.audioFileType = self.kwargs.get(self.lookup_url_kwarg_type)
        self.audioFileId = self.kwargs.get(self.lookup_url_kwarg_id)
        if 'song' in self.audioFileType.lower():
            queryset = Song.objects.filter(song_id = self.audioFileId)
            return queryset
        elif 'podcast' in self.audioFileType.lower():
            queryset = Podcast.objects.filter(podcast_id = self.audioFileId)
            return queryset
        elif 'audiobook' in self.audioFileType.lower():
            queryset = AudioBook.objects.filter(audiobook_id = self.audioFileId)
            return queryset

    def list(self, request):
        queryset = self.get_queryset(request)
        if 'song' in self.audioFileType.lower():
            serializer = SongSerializer(queryset, many=True)
        elif 'podcast' in self.audioFileType.lower():
            serializer = PodcastSerializer(queryset, many=True)
        elif 'audiobook' in self.audioFileType.lower():
            serializer = AudioBookSerializer(queryset, many=True)
        else:
            return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": serializer.data, "message": "Success", "status": True}, status=status.HTTP_200_OK)
    