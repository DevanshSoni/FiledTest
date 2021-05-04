from django import forms
from core_features.models import Song, Podcast, AudioBook

class SongValidatorForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"

class PodcastValidatorForm:
    class Meta:
        model = Podcast
        fields = "__all__"

class AudiobookValidatorForm:
    class Meta:
        model = AudioBook
        fields = "__all__" 
