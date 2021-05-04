from django.db import models
from .utils import check_date
from django_mysql.models import ListCharField
# Create your models here.

class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    song_name = models.CharField(max_length=100, null=False, blank=False)
    song_duration = models.PositiveBigIntegerField(null=False, blank=False)
    uploaded_time = models.DateTimeField( validators=[check_date], auto_now_add=True, null=False, blank=False)

class Podcast(models.Model):
    podcast_id = models.AutoField(primary_key=True)
    audiobook_name = models.CharField(max_length=100, null=False, blank=False)
    podcast_duration = models.PositiveBigIntegerField(null=False, blank=False)
    uploaded_time = models.DateTimeField( validators=[check_date], auto_now_add=True, null=False, blank=False)
    audiobook_host = models.CharField(max_length=100, null=False, blank=False)
    participants = ListCharField(
        base_field = models.CharField(max_length=100),
        size=10,
        max_length=(10 * 101)
    )

class AudioBook(models.Model):
    audiobook_id = models.AutoField(primary_key=True)
    audiobook_title = models.CharField(max_length=100, null=False, blank=False)
    audiobook_author = models.CharField(max_length=100, null=False, blank=False)
    audiobook_narrator = models.CharField(max_length=100, null=False, blank=False)
    audiobook_duration = models.PositiveBigIntegerField(null=False, blank=False)
    uploaded_time = models.DateTimeField( validators=[check_date], auto_now_add=True, null=False, blank=False)
