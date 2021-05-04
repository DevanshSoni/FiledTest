from django.urls import path,include
from .views import createAudioView, deleteAudioView, updateAudioView, getAudioView

urlpatterns = [
    path('createAudio/', createAudioView.CreateAudio.as_view(), name = "createAudio"),
    path('deleteAudio/<str:audioFileType>/<int:audioFileID>/', deleteAudioView.DeleteAudioView.as_view(), name = "deleteAudio"),
    path('updateAudio/<str:audioFileType>/<int:audioFileID>/', updateAudioView.UpdateAudio.as_view(), name = "updateAudio"),
    path('getAudio/<str:audioFileType>/', getAudioView.allAudioList.as_view(), name = "getAllAudio"),
    path('getAudio/<str:audioFileType>/<int:audioFileID>/', getAudioView.audioList.as_view(), name = "getAllAudio"),
]
