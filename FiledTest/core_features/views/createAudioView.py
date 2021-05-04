from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from core_features.models import Song, Podcast, AudioBook
from ..validators.validate_forms import SongValidatorForm, PodcastValidatorForm, AudiobookValidatorForm 

class CreateAudio(APIView):
    def post(self, request):
        try:
            audioFileType = request.data['audioFileType']
            audioFileMetaData = request.data['audioFileMetaData']

            if 'song' in audioFileType.lower():
                data = SongValidatorForm(audioFileMetaData)
                if data.is_valid():
                    Song.objects.create(audioFileMetaData)
                else:
                    return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_400_BAD_REQUEST)
            elif 'podcast' in audioFileType.lower():
                data = PodcastValidatorForm(audioFileMetaData)
                if data.is_valid():
                    Podcast.objects.create(audioFileMetaData)
                else:
                    return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_400_BAD_REQUEST)
            elif 'audiobook' in audioFileType.lower():
                data = AudiobookValidatorForm(audioFileMetaData)
                if data.is_valid():
                    AudioBook.objects.create(audioFileMetaData)
                else:
                    return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"data": [], "detail": "Successfully Created Audio", "status": True}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
