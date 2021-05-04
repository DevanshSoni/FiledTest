from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from core_features.models import Song, Podcast, AudioBook
from ..validators.validate_forms import SongValidatorForm, PodcastValidatorForm, AudiobookValidatorForm 


class UpdateAudio(APIView):
    def put(self, request,  audioFileType, audioFileID):
        try:
            audioFileMetaData = request.data['audioFileMetaData']
            if 'song' in audioFileType.lower():
                data = SongValidatorForm(audioFileMetaData)
                if data.is_valid():
                    records = Song.objects.filter(song_id = audioFileID)
                    if records.exists():
                        records[0].song_name = audioFileMetaData['song_name']
                        records[0].song_duration = audioFileMetaData['song_duration']
                        records[0].uploaded_time = audioFileMetaData['uploaded_time']
                        records[0].save()
                    else:
                        return Response({"data": [], "detail": "AudioFileID is not Valid", "status": False}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_400_BAD_REQUEST)
            elif 'podcast' in audioFileType.lower():
                data = PodcastValidatorForm(audioFileMetaData)
                if data.is_valid():
                    records = Podcast.objects.filter(podcast_id = audioFileID)
                    if records.exists():
                        records[0].audiobook_name = audioFileMetaData['audiobook_name']
                        records[0].podcast_duration = audioFileMetaData['podcast_duration']
                        records[0].uploaded_time = audioFileMetaData['uploaded_time']
                        records[0].audiobook_host = audioFileMetaData['audiobook_host']
                        records[0].participants = audioFileMetaData['participants']
                        records[0].save()
                    else:
                        return Response({"data": [], "detail": "AudioFileID is not Valid", "status": False}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_400_BAD_REQUEST)
            elif 'audiobook' in audioFileType.lower():
                data = AudiobookValidatorForm(audioFileMetaData)
                if data.is_valid():
                    records = AudioBook.objects.filter(audiobook_id = audioFileID)
                    if records.exists():
                        records[0].audiobook_title = audioFileMetaData['audiobook_title']
                        records[0].audiobook_author = audioFileMetaData['audiobook_author']
                        records[0].audiobook_narrator = audioFileMetaData['audiobook_narrator']
                        records[0].audiobook_duration = audioFileMetaData['audiobook_duration']
                        records[0].uploaded_time = audioFileMetaData['uploaded_time']
                    else:
                        return Response({"data": [], "detail": "AudioFileID is not Valid", "status": False}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"data": [], "detail": "Successfully Updated Audio Record", "status": True}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
