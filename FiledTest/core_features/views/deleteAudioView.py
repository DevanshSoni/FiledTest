from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from core_features.models import Song, Podcast, AudioBook


class DeleteAudioView(APIView):

    def delete(self, request, audioFileType, audioFileID):
        try:
            if 'song' in audioFileType.lower():
                records = Song.objects.filter(song_id = audioFileID)
                if records.exists():
                    records.delete()
                else:
                    return Response({"data": [], "detail": "AudioFileID is not Valid", "status": False}, status=status.HTTP_400_BAD_REQUEST)
            elif 'podcast' in audioFileType.lower():
                records = Podcast.objects.filter(podcast_id = audioFileID)
                if records.exists():
                    records.delete()
                else:
                    return Response({"data": [], "detail": "AudioFileID is not Valid", "status": False}, status=status.HTTP_400_BAD_REQUEST)
            elif 'audiobook' in audioFileType.lower():
                records = AudioBook.objects.filter(audiobook_id = audioFileID)
                if records.exists():
                    records.delete()
                else:
                    return Response({"data": [], "detail": "AudioFileID is not Valid", "status": False}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"data": [], "detail": "Successfully Deleted Audio", "status": True}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"data": [], "detail": "Failure", "status": False}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)